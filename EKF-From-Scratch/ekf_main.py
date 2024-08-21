'''
EKF SLAM Logic:
mu: state estimate, where our best quess of the state is
sigma: covariance matrix aka state uncertainty, how uncertain we are of our best guess

Two steps to the EKF:
- Prediction Update
    - From the control inputs u and some model, how does our state estimate change?
    - Moving only affects the state estimate of the robot
    - Moving affects uncertainty of the system
    - Model noise also affects uncertainty
- Measurement Update
	- From what the robot oberverves, how does our state estimate change?
    - We mix current uncertainty with measurement uncertainty
'''

from python_ugv_sim.utils import vehicles, environment
import numpy as np
import pygame

# < - - - - - - - - - - - EKF SLAM MATERIAL - - - - - - - - - - - >
# ---> Robot Parameters
n_state = 3 # state dimension of the robot (x, y, theta)
n_landmarks = 1 # DEFAULT: 1 landmark

# ---› Noise parameters
R = np.diag([0.002,0.002,0.0005])

# ---> EKF Estimation Variables
mu = np.zeros((n_state + 2*n_landmarks, 1)) # state estimate
sigma = np.zeros((n_state + 2*n_landmarks, n_state + 2*n_landmarks)) # covariance matrix

# ---> Helpful Matrices
Fx = np.block([[np.eye(n_state), np.zeros((n_state, 2*n_landmarks))]]) # state transition matrix

def prediction_update(mu, sigma, u, dt):
    rx, ry, theta = mu[0], mu[1], mu[2]
    v, w = u[0], u[1]
    # Ipdate state estimate mu with model
    state_model_mat = np.zeros((n_state, 1))
    state_model_mat[0] = -(v/w)*np.sin(theta) + (v/w)*np.sin(theta + w*dt) if np.abs(w) >= 0.01 else v*dt*np.cos(theta)
    state_model_mat[1] = (v/w)*np.cos(theta) - (v/w)*np.cos(theta + w*dt) if np.abs(w) >= 0.01 else v*dt*np.sin(theta)
    state_model_mat[2] = w*dt
    mu += np.transpose(Fx).dot(state_model_mat)
    # Update state uncertainty with model + noise
    state_jacobian_mat = np.zeros((n_state, 3))
    state_jacobian_mat[0][2] = -(v/w)*np.cos(theta) + (v/w)*np.cos(theta + w*dt) if np.abs(w) >= 0.01 else -v*dt*np.sin(theta)
    state_jacobian_mat[1][2] = -(v/w)*np.sin(theta) + (v/w)*np.sin(theta + w*dt) if np.abs(w) >= 0.01 else v*dt*np.cos(theta)
    I = np.eye(sigma.shape[0])
    G = I + np.transpose(Fx).dot(state_jacobian_mat).dot(Fx)
    sigma = G.dot(sigma).dot(np.transpose(G)) + np.transpose(Fx).dot(R).dot(Fx)
    return mu, sigma

def measurement_update(mu, sigma):
    return

# < - - - - - - - - - - - PLOTTING - - - - - - - - - - - >

def show_uncertainty_ellipse(env,center,width,angle):
    '''
    Visualize an uncertainty ellipse
    Adapted from: https://stackoverflow.com/questions/65767785/how-to-draw-a-rotated-ellipse-using-pygame
    '''

    target_rect = pygame.Rect(center[0]-int(width[0]/2),center[1]-int(width[1]/2),width[0],width[1])
    shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
    pygame.draw.ellipse(shape_surf, env.red, (0, 0, *target_rect.size), 2)
    rotated_surf = pygame.transform.rotate(shape_surf, angle)
    env.map.blit(rotated_surf, rotated_surf.get_rect(center = target_rect.center))

def sigma2transform(sigma_sub):
	'''
	2x2 state uncertainty in the x and y position
	'''
	[eigenvals, eigenvecs] = np.linalg.eig(sigma_sub)
	angle = 180*np.arctan2(eigenvecs[1,0],eigenvecs[0,0])/np.pi
	return eigenvals, angle


def show_robot_estimate(env, sigma, mu):
	'''
	Show the robot estimate on the map
	'''
	rx, ry = mu[0], mu[1]
	center = env.position2pixel((rx,ry))
	eigenvals, angle = sigma2transform(sigma[0:2,0:2])
	width = env.dist2pixellen(eigenvals[0]), env.dist2pixellen(eigenvals[1])
	show_uncertainty_ellipse(env,center,width,angle)

# < - - - - - - - - - - - EKF PLOTTING - - - - - - - - - - - >


if __name__=='__main__':

    # Initialize pygame
    pygame.init()

    # Initialize robot and time step
    x_init = np.array([1,1,np.pi/2])
    robot = vehicles.DifferentialDrive(x_init)
    dt = 0.01

    # Initialize state estimate
    mu[0:3] = np.expand_dims(x_init, axis=1)
    sigma[0:3,0:3] = 0.05*np.eye(3)

    # Initialize and display environment
    env = environment.Environment(map_image_path="./python_ugv_sim/maps/map_blank.png")

    running = True
    u = np.array([0.,0.]) # Controls
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False
            u = robot.update_u(u,event) if event.type==pygame.KEYUP or event.type==pygame.KEYDOWN else u # Update controls based on key states
        robot.move_step(u,dt) # Integrate EOMs forward, i.e., move robot
        mu, sigma = prediction_update(mu, sigma, u, dt)
        env.show_map() # Re-blit map
        env.show_robot(robot) # Re-blit robot
        show_robot_estimate(env,sigma,mu) # Show EKF estimates
        pygame.display.update() # Update display
