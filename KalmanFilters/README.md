# Basic 1D Kalman Filter

measurements: represent the actual observed positions of the system. These are values obtained from sensors or observations.

motions: represent the expected movements or control inputs that should change the system's position. These are values that describe how the system should move.

Update Step: Uses the measurement to correct the current state estimate. The update function combines the prior state estimate (mean and variance) with the new measurement to produce an updated state estimate. This step uses Bayes' theorem to update the estimate with the new information from the measurement.

Predict Step: Uses the motion to predict the next state. The predict function updates the state estimate by adding the motion to the mean and increasing the variance. This step uses the total probability to account for the effect of the motion and its uncertainty.

## High Dimensional Gaussians (AKA Multivariate Gaussians)


