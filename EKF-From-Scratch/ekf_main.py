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
from visual_utils import show_robot_estimate, show_landmark_location, show_measurements, show_landmark_estimate
import pygame

# < - - - - - - - - - - - EKF SLAM MATERIAL - - - - - - - - - - - >
# ---> Robot Parameters
n_state = 3 # state dimension of the robot (x, y, theta)
robot_fov = 3 # robot field of view in meters

# ---› Landmark parameters
landmarks = [(4,4),
(4,8),
(8,8),
(12,8),
(16,8),
(16,4),
(12,4)]

n_landmarks = len(landmarks)

# ---› Noise parameters
R = np.diag([0.002,0.002,0.0005]) # sigma_x, sigma_y, sigma_theta
Q = np.diag([0.003,0.00003]) # sigma_r, sigma_phi

# ---> EKF Estimation Variables
mu = np.zeros((n_state + 2*n_landmarks, 1)) # state estimate
sigma = np.zeros((n_state + 2*n_landmarks, n_state + 2*n_landmarks)) # covariance matrix

mu[:] = np.nan
np.fill_diagonal(sigma,100)

# ---> Helpful Matrices
Fx = np.block([[np.eye(n_state), np.zeros((n_state, 2*n_landmarks))]]) # state transition matrix

# Simulate Measurements
def sim_measurement(state,landmarks):
    '''
    This function simulates a measurement between robot and landmark
    Inputs:
     - state: robot state (3x1 numpy array)
     - landmarks: list of 2-tuples, each of (lx,ly) actual position of landmark
    Outputs:
     - zs: list of 3-tuples, each (r,phi,lidx) of range (r) and relative bearing (phi) from robot to landmark,
           and lidx is the (known) correspondence landmark index.
    '''
    rx, ry, rtheta = state[0], state[1], state[2]
    zs = [] # List of measurements
    for (lidx,landmark) in enumerate(landmarks): # Iterate over landmarks and indices
        lx,ly = landmark
        dist = np.linalg.norm(np.array([lx-rx,ly-ry])) # distance between robot and landmark
        phi = np.arctan2(ly-ry,lx-rx) - rtheta # angle between robot heading and landmark, relative to robot frame
        phi = np.arctan2(np.sin(phi),np.cos(phi)) # Keep phi bounded, -pi <= phi <= +pi
        if dist<robot_fov: # Only append if observation is within robot field of view
            zs.append((dist,phi,lidx))
    return zs

def prediction_update(mu, sigma, u, dt):
    rx, ry, theta = mu[0], mu[1], mu[2]
    v, w = u[0], u[1]
    # Update state estimate mu with model
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

def measurement_update(mu, sigma, zs):
	rx, ry, theta = mu[0][0], mu[1][0], mu[2][0]
	Ks = [np.zeros((mu.shape[0], 2)) for lidx in range(n_landmarks)]
	Hs = [np.zeros((2, mu.shape[0])) for lidx in range(n_landmarks)]
	delta_zs = [np.zeros((2,1)) for lidx in range(n_landmarks)]

	for z in zs:
		(dist, phi, lidx) = z
		mu_landmark = mu[n_state + 2*lidx: n_state + 2*lidx + 2]

		if np.isnan(mu_landmark[0]):
			mu_landmark[0] = rx + dist * np.cos(phi + theta)
			mu_landmark[1] = ry + dist * np.sin(phi + theta)
			mu[n_state + lidx*2 : n_state + lidx*2 + 2] = mu_landmark

		delta = mu_landmark - np.array([[rx], [ry]])
		q = np.linalg.norm(delta)**2 #Euclidean distance between the robot and the landmark

		dist_est = np.sqrt(q)
		phi_est = np.arctan2(delta[1, 0], delta[0, 0]) - theta
		phi_est = np.arctan2(np.sin(phi_est), np.cos(phi_est)) #the angle stays within the correct range of −π to π
		z_est_arr = np.array([[dist_est],[phi_est]])
		z_act_arr = np.array([[dist],[phi]])
		delta_zs[lidx] = z_act_arr - z_est_arr

		Fxj = np.block([[Fx],[np.zeros((2,Fx.shape[1]))]])
		Fxj[n_state:n_state+2,n_state+2*lidx:n_state+2*lidx+2] = np.eye(2)

		H = np.array([[-delta[0,0]/np.sqrt(q),-delta[1,0]/np.sqrt(q),0,delta[0,0]/np.sqrt(q),delta[1,0]/np.sqrt(q)],\
				[delta[1,0]/q,-delta[0,0]/q,-1,-delta[1,0]/q,+delta[0,0]/q]])
		H = H.dot(Fxj)
		Hs[lidx] = H
		S = H.dot(sigma).dot(H.T) + Q # the total uncertainty in the predicted measurement
		Ks[lidx] = sigma.dot(np.transpose(H)).dot(np.linalg.inv(S))
	# Offset and Batch Update
	mu_offset = np.zeros(mu.shape)
	sigma_factor = np.eye(sigma.shape[0])
	for lidx in range(n_landmarks):
		mu_offset += Ks[lidx].dot(delta_zs[lidx])
		sigma_factor -= Ks[lidx].dot(Hs[lidx])
	mu += mu_offset
	sigma = sigma_factor.dot(sigma)
	return mu, sigma


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
    sigma[2, 2] = 0

    # Initialize and display environment
    env = environment.Environment(map_image_path="./python_ugv_sim/maps/map_blank.png")

    running = True
    u = np.array([0.,0.]) # Controls
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                  if event.key == pygame.K_ESCAPE or event.key == pygame.K_q:
                        running = False
            u = robot.update_u(u,event) if event.type==pygame.KEYUP or event.type==pygame.KEYDOWN else u # Update controls based on key states
        robot.move_step(u,dt) # Integrate EOMs forward, i.e., move robot
        # Get measurements
        zs = sim_measurement(robot.get_pose(),landmarks)
        # EKF SLAM
        mu, sigma = prediction_update(mu, sigma, u, dt)
        mu, sigma = measurement_update(mu, sigma, zs)
        # Show ground truth
        env.show_map() # Re-blit map
        env.show_robot(robot) # Re-blit robot
        show_landmark_location(landmarks, env)
        show_measurements(robot.get_pose(), zs, env)
        # Show EKF estimates
        show_robot_estimate(env,sigma,mu)
        show_landmark_estimate(mu,sigma,env,n_landmarks,n_state)
        pygame.display.update() # Update display
