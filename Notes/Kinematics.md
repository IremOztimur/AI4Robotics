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
