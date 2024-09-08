# < - - - - - - - - - - - PLOTTING - - - - - - - - - - - >
import pygame
import numpy as np

def show_uncertainty_ellipse(env,center,width,angle):
    '''
    Visualize an uncertainty ellipse
    Adapted from: https://stackoverflow.com/questions/65767785/how-to-draw-a-rotated-ellipse-using-pygame
    '''

    if width[0] <= 0 or width[1] <= 0:
        print("Invalid ellipse dimensions:", width)
        return
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

def show_landmark_location(landmarks,env):
    '''
    Visualize actual landmark location
    '''
    for landmark in landmarks:
        lx_pixel, ly_pixel = env.position2pixel(landmark)
        r_pixel = env.dist2pixellen(0.2)
        pygame.gfxdraw.filled_circle(env.get_pygame_surface(),lx_pixel,ly_pixel,r_pixel,(255,0,255)) #

def show_robot_estimate(env, sigma, mu):
	'''
	Show the robot estimate on the map
	'''
	rx, ry = mu[0], mu[1]
	center = env.position2pixel((rx,ry))
	eigenvals, angle = sigma2transform(sigma[0:2,0:2])
	width = env.dist2pixellen(eigenvals[0]), env.dist2pixellen(eigenvals[1])
	show_uncertainty_ellipse(env,center,width,angle)


def show_measurements(state,zs,env):
    '''
    Visualize measurements the occur between the robot and landmarks
    '''
    rx,ry = state[0], state[1]
    rx_pix, ry_pix = env.position2pixel((rx,ry)) # Convert robot position units from meters to pixels
    for z in zs: # For each measurement
        dist,theta,lidx = z # Unpack measurement tuple
        lx,ly = rx+dist*np.cos(theta+state[2]),ry+dist*np.sin(theta+state[2]) # Set the observed landmark location (lx,ly)
        lx_pix,ly_pix = env.position2pixel((lx,ly)) # Convert observed landmark location units from meters to pixels
        pygame.gfxdraw.line(env.get_pygame_surface(),rx_pix,ry_pix,lx_pix,ly_pix,(155,155,155)) # Draw a line between robot and observed landmark

def show_landmark_estimate(mu,sigma,env, n_landmarks, n_state):
    '''
    Visualize estimated position and uncertainty of a landmark
    '''
    for lidx in range(n_landmarks): # For each landmark location
        lx,ly,lsigma = mu[n_state+lidx*2], mu[n_state+lidx*2+1], sigma[n_state+lidx*2:n_state+lidx*2+2,n_state+lidx*2:n_state+lidx*2+2]
        if ~np.isnan(lx): # If the landmark has been observed
            p_pixel = env.position2pixel((lx,ly)) # Transform landmark location to pygame surface pixel coordinates
            eigenvals,angle = sigma2transform(lsigma) # Get eigenvalues and rotation angle of covariance of landmark
            if np.max(eigenvals)<15: # Only visualize when the maximum uncertainty is below some threshold
                sigma_pixel = max(env.dist2pixellen(eigenvals[0]),5), max(env.dist2pixellen(eigenvals[1]),5) # Convert eigenvalue units from meters to pixels
                show_uncertainty_ellipse(env,p_pixel,sigma_pixel,angle) # Show the ellipse
