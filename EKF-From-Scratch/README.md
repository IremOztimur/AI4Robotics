# Kalman Filter
### Flowchart of a Simple Kalman Filter

<img width="861" alt="KF-Diagram" src="https://github.com/IremOztimur/AI4Robotics/assets/77894816/91938290-fa74-4658-8cbd-1b31d129ec7e">

### Kalman Gain Detailed Explanation
<img width="1077" alt="KalmanGain" src="https://github.com/IremOztimur/AI4Robotics/assets/77894816/a7e2e78d-b574-4d5e-a73d-95b3d2e467fb">

### Kalman Filter Calculations
<img width="878" alt="kalman-calculations" src="https://github.com/IremOztimur/AI4Robotics/assets/77894816/4ae636e7-46d5-4d4c-8063-e358255b1736">

## The Multi-Dimension Model
TO-DO: Create a workflow of multi-dimension kalman filter

## The Multi-Dimension Model - The State Matrix
<img width="835" alt="state-matrix-multi" src="https://github.com/IremOztimur/AI4Robotics/assets/77894816/410bfdcf-f374-409c-b9c9-3b319d7c3bc1">

<div style="display: flex; flex-direction: row; justify-content: space-around;">
  <div style="text-align: center;">
    <h3>State Matrix in 1D Example</h3>
    <img width="300" alt="state-matrix-examples" src="https://github.com/IremOztimur/AI4Robotics/assets/77894816/1c26321b-ef3d-4a9d-81b4-c6b7868f9605">
  </div>
  <div style="text-align: center;">
    <h3>Control Variable Matrix in 1D Example</h3>
    <img width="300" alt="control variable matrix" src="https://github.com/IremOztimur/AI4Robotics/assets/77894816/fb940ad2-c420-43cf-9a7d-2904fe719338">
  </div>
    <div style="text-align: center;">
    <h3>Control Variable Matrix in 2D Example</h3>
      <p>where 

$$
\mathbf{X_k} = \begin{bmatrix}
x \\
y \\
\dot{x} \\
\dot{y}
\end{bmatrix}
$$</p>
    <img width="300" alt="control variable matrix 2D" src="https://github.com/IremOztimur/AI4Robotics/assets/77894816/f5653133-887d-4e2f-a7ef-73a3aedbe657">
  </div>
</div>

### Conversion of State Matrix in 2D without Noice Matrix
<img width="500" alt="state-matrix-2D" src="https://github.com/IremOztimur/AI4Robotics/assets/77894816/65f741f9-91d2-43a6-a9c2-82dfa7ef8b2e">


