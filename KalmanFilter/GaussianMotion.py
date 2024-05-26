import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

def plot_covariance_ellipse(mean, cov, ax, nstd=2, **kwargs):
    """
    Plots an ellipse representing the covariance matrix.
    :param mean: Mean vector [x, y]
    :param cov: Covariance matrix [[var_x, cov_xy], [cov_yx, var_y]]
    :param ax: Matplotlib axis object
    :param nstd: Number of standard deviations
    :param kwargs: Additional arguments for Ellipse patch
    """
    eigvals, eigvecs = np.linalg.eigh(cov)
    order = eigvals.argsort()[::-1]
    eigvals, eigvecs = eigvals[order], eigvecs[:, order]
    angle = np.degrees(np.arctan2(*eigvecs[:, 0][::-1]))
    width, height = 2 * nstd * np.sqrt(eigvals)
    ellipse = Ellipse(xy=mean, width=width, height=height, angle=angle, **kwargs)
    ax.add_patch(ellipse)

mean = np.array([0, 0])
cov = np.array([[1., 0.], [0., 1.]])

# Create a figure and axis
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-5, 12)
ax.set_ylim(-5, 12)

# Plot initial state
plot_covariance_ellipse(mean, cov, ax, edgecolor='blue', alpha=0.5)

# Simulate motion and measurement updates
np.random.seed(42)
for _ in range(6):
    mean += np.array([1, 1])
    cov += np.array([[0.5, 0.], [0., 0.5]])

    plot_covariance_ellipse(mean, cov, ax, edgecolor='blue', alpha=0.5)

    measurement = mean + np.random.multivariate_normal([0, 0], [[0.5, 0], [0, 0.5]])
    measurement_cov = np.array([[0.5, 0], [0, 0.5]])
    K = cov @ np.linalg.inv(cov + measurement_cov)
    mean = mean + K @ (measurement - mean)
    cov = (np.eye(2) - K) @ cov

    plot_covariance_ellipse(mean, cov, ax, edgecolor='red', alpha=0.5)

plot_covariance_ellipse(mean, cov, ax, edgecolor='green', alpha=0.5)

ax.grid(True)
ax.set_xlabel('X Position')
ax.set_ylabel('Y Position')
ax.set_title('2D Gaussian Motion in Kalman Filter')

plt.show()
