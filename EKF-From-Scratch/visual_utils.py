# < - - - - - - - - - - - PLOTTING - - - - - - - - - - - >
import pygame
import numpy as np

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
