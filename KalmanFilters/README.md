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
High Dimensional Gaussians, also known as Multivariate Gaussians, are a statistical concept used to model probability distributions in multidimensional spaces. Unlike the univariate Gaussian distribution, which describes single-variable distributions, Multivariate Gaussians extend this concept to describe the joint distribution of multiple variables simultaneously.

#### Simplified Kalman Filter Formula 
<img width="1242" alt="prediction-formula-simplification" src="https://github.com/IremOztimur/AI4Robotics/assets/77894816/712501bd-30ff-4240-a1e9-abde432065a7">

```python
def kalman_filter(x, P):
	for n in range(len(measurements)):

		# measurement update
		Z = matrix([[measurements[n]]])
		Y = Z - (H * x)
		S = H * P * H.transpose() + R
		K = P * H.transpose() * S.inverse()
		x = x + (K * Y)
		P = (I - (K * H)) * P
		 # prediction
		x = F * x + u
		P = F * P * F.transpose()
	return x,P
```

**Z**: It is the observed measurement from the environment or sensor at a specific time step


### Explanation:

1. **Measurement Update**:
   - Compute the measurement residual $\ y = Z - H \cdot x \$.
   - Compute the residual covariance $\ S = H \cdot P \cdot H^T + R \$.
   - Compute the Kalman gain $\ K = P \cdot H^T \cdot S^{-1} \$.
   - Update the state estimate $\ x = x + K \cdot y \$.
   - Update the uncertainty $\ P = (I - K \cdot H) \cdot P \$.

2. **Prediction**:
   - Predict the next state $\ x = F \cdot x + u \$.
   - Predict the next covariance $\ P = F \cdot P \cdot F^T + Q \$.

This Kalman filter will process the given measurements and predict the next state and covariance, iterating through all provided measurements.

