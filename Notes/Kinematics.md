# Kinematic Equations
Kinematic equations describe the motion of objects under constant acceleration. These equations are crucial in predicting the future state of moving objects, which is essential for applications like the Kalman filter.

**Key Variables**

* _s_: Displacement
* _u_: Initial velocity
* _v_: Final velocity
* _a_: Acceleration
* _t_: Time

## Kinematic Equation for Displacement
The equation for displacement, given initial velocity and constant acceleration, is:

$\ s = ut + \frac{1}{2}at^2 \$

### Explanation

1. **Initial Velocity ( _u_ )**: The velocity of the object at the start of the time period.
2. **Acceleration ( _a_ )**: The rate at which the object's velocity changes over time.
3. **Time ( _t_ )**: The duration over which the object is moving.

This equation provides a way to calculate the displacement of an object when you know its initial velocity, the constant acceleration, and the time period over which it is moving.

### Application in Kalman Filter
The Kalman filter is an algorithm that uses a series of measurements observed over time, containing statistical noise and other inaccuracies, and produces estimates of unknown variables. In the context of kinematics, the Kalman filter can predict the future position and velocity of an object.

### Kalman Filter Prediction Step

The Kalman filter has two main steps: **prediction** and **update**. During the prediction step, the filter uses the kinematic equations to estimate the object's next state (position and velocity).

1. **State Vector**: Represents the object's current state, typically including position and velocity.
   
$$\
   \mathbf{x}_k = \begin{bmatrix}
   x_k \\
   v_k \\
   \end{bmatrix}
$$
   
   where $\( x_k \)$ is the position and $\( v_k \)$ is the velocity at time \( k \).


2. **State Transition Model**: Describes how the state evolves from one time step to the next. For constant acceleration, this can be represented as:
   
$$\
   \mathbf{F} = \begin{bmatrix}
   1 & \Delta t \\
   0 & 1 \\ 
   \end{bmatrix}
$$

   where $\( \Delta t \)$ is the time step.

3. **Prediction Equation**

The prediction for the next state is given by:
$$\[
\mathbf{x}_{k+1|k} = \mathbf{F} \mathbf{x}_k
\]$$

Using our kinematic equation for displacement:

1. **Displacement (position) prediction**:
   $$\[
   x_{k+1} = x_k + v_k \Delta t + \frac{1}{2} a \Delta t^2
   \]$$

2. **Velocity prediction** (assuming constant acceleration):
   $$\[
   v_{k+1} = v_k + a \Delta t
   \]$$

In matrix form:

$$\
\mathbf{x}_{k+1|k} = \begin{bmatrix}
1 & \Delta t \\
0 & 1 \\
\end{bmatrix} \begin{bmatrix}
x_k \\
v_k \\
\end{bmatrix} + \begin{bmatrix}
\frac{1}{2} a \Delta t^2 \\
a \Delta t \\
\end{bmatrix}
\$$
