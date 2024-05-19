# Basic 1D Kalman Filter

**measurements**: Represent the actual observed positions of the system. These are values obtained from sensors or observations.

**motions**: Represent the expected movements or control inputs that should change the system's position. These are values that describe how the system should move.

**Update Step**: Uses the measurement to correct the current state estimate. The update function combines the prior state estimate (mean and variance) with the new measurement to produce an updated state estimate. This step uses Bayes' theorem to update the estimate with the new information from the measurement.
```python
def update(mean1, var1, mean2, var2):
    new_mean = float(var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1./(1./var1 + 1./var2)
    return [new_mean, new_var]
```

**Predict Step**: Uses the motion to predict the next state. The predict function updates the state estimate by adding the motion to the mean and increasing the variance. This step uses the total probability to account for the effect of the motion and its uncertainty.
```python
def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]
```

## High Dimensional Gaussians (AKA Multivariate Gaussians)


