## Understanding Covariance

Here is a [Google Colab Notebook](https://colab.research.google.com/drive/1eqvk7VJShesmg6woNGNGX2OQg3DqHFfk) dedicated to covariance.

**Covariance** is a statistical measure that describes the extent to which two random variables change together. Fundamentally, it indicates whether an increase in one variable corresponds to an increase in the other (positive covariance), a decrease in the other (negative covariance), or no relationship at all (zero covariance).

Mathematically, for two random variables \(X\) and \(Y\), the covariance is defined as:

$\ \text{cov}(X, Y) = E[(X - E[X])(Y - E[Y])] \$

Where:
- \(E[X]\) is the expected value (mean) of \(X\).
- \(E[Y]\) is the expected value (mean) of \(Y\).
- \(E[(X - E[X])(Y - E[Y])]\) is the expected value of the product of their deviations from their respective means.

### Interpretation of Covariance:
- **Positive Covariance**: If $\( \text{cov}(X, Y) > 0 \)$, it indicates that as \(X\) increases, \(Y\) also tends to increase.
- **Negative Covariance**: If $\( \text{cov}(X, Y) < 0 \)$, it indicates that as \(X\) increases, \(Y\) tends to decrease.
- **Zero Covariance**: If $\( \text{cov}(X, Y) = 0 \)$, it suggests that there is no linear relationship between the variables.

### Covariance Matrix

A **covariance matrix** is a square matrix that contains the covariances between pairs of elements of a vector of random variables. For a vector of random variables $\(\mathbf{X} = [X_1, X_2, \ldots, X_n]^T\)$, the covariance matrix $\(\Sigma\)$ is defined as:

$$
\ \Sigma = \begin{bmatrix}
\text{cov}(X_1, X_1) & \text{cov}(X_1, X_2) & \cdots & \text{cov}(X_1, X_n) \\
\text{cov}(X_2, X_1) & \text{cov}(X_2, X_2) & \cdots & \text{cov}(X_2, X_n) \\
\vdots & \vdots & \ddots & \vdots \\
\text{cov}(X_n, X_1) & \text{cov}(X_n, X_2) & \cdots & \text{cov}(X_n, X_n) \\
\end{bmatrix} \
$$

### Covariance Matrix in the Kalman Filter

In the context of a **Kalman Filter**, the covariance matrix plays a crucial role in estimating the state of a system from noisy measurements. There are two primary covariance matrices in a Kalman Filter:

1. **Process Covariance Matrix \(Q\)**: This matrix represents the uncertainty in the process model. It accounts for the process noise, which refers to the inaccuracies in the model that describe how the state evolves over time.

2. **Measurement Covariance Matrix \(R\)**: This matrix represents the uncertainty in the measurements. It accounts for the measurement noise, which refers to the inaccuracies in the observations or sensor readings.

3. **Error Covariance Matrix \(P\)**: This matrix represents the uncertainty in the estimate of the system's state. It is updated at each step of the Kalman filter to reflect the reduction in uncertainty as new measurements are incorporated.

### Kalman Filter Equations

In a typical Kalman filter, the covariance matrices are used in the following equations:

- **Prediction Step**:
  - Predicted State: $\( \hat{x}_{k|k-1} = A \hat{x}_{k-1|k-1} + B u_{k-1} \)$
  - Predicted Error Covariance: $\( P_{k|k-1} = A P_{k-1|k-1} A^T + Q \)$


- **Update Step**:
  - Kalman Gain: $\( K_k = P_{k|k-1} H^T (H P_{k|k-1} H^T + R)^{-1} \)$
  - Updated State: $\( \hat{x}_{k|k} = \hat{x}_{k|k-1} + K_k (z_k - H \hat{x}_{k|k-1}) \)$
  - Updated Error Covariance: $\( P_{k|k} = (I - K_k H) P_{k|k-1} \)$

Where:
- $\( \hat{x}_{k|k-1} \)$ is the predicted state.
- $\( \hat{x}_{k|k} \)$ is the updated state estimate.
- $\( P_{k|k-1} \)$ is the predicted error covariance.
- $\( P_{k|k} \)$ is the updated error covariance.
- $\( K_k \)$ is the Kalman gain.
- $\( z_k \)$ is the measurement at time \(k\).
- $\( A \)$ is the state transition model.
- $\( B \)$ is the control-input model.
- $\( u_k \)$ is the control vector.
- $\( H \)$ is the observation model.
- $\( I \)$ is the identity matrix.

In summary, the covariance matrices \(Q\), \(R\), and \(P\) are essential for managing and updating the uncertainties in both the process model and the measurements within the Kalman filter framework.
