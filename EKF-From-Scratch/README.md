# Extended Kalman Filter

To understand where the "extended" part comes, let's talk about linear and non-linear models.

## Linear and Non-Linear Models

### What is a Linear System?
A system is considered linear if it satisfies the properties of superposition and homogeneity.

**Superposition (Additivity):** 

$\ S(x1+x2)=S(x1)+S(x2)\$

**Homogeneity (Scaling):**

$\ S(αx)\=αS(x)\$

---

### Linear Transformations
Linear transformations are functions between vector spaces that preserve the operations of vector addition and scalar multiplication.

---

### Matrices as Linear Transformations
Matrices naturally represent linear transformations. If A is an m×n matrix and x is an n-dimensional vector, then the product Ax is an m-dimensional vector. This product satisfies both additivity and homogeneity, making it a linear transformation.

--- 

### Linear Models

A linear model is one in which the relationship between variables is a straight line when plotted on a graph. In mathematical terms, a linear model can be expressed as:

$\ y = ax+b \$
where:
- $\ y\$ is the dependent variable.
- $\ x\$ is the independent variable.
- $\ a\$ and $\ b\$ are constants.

In the context of dynamic systems (like those used in Kalman Filters), a linear model means the state transition and observation models can be expressed as linear equations:
1. **State Transition Model:** 
   $\ x_k = A_{k-1} x_{k-1} + B_{k-1} u_{k-1} + w_{k-1} \$
2. **Observation Model:** 
   $\ z_k = H_k x_k + v_k \$

Both of these models are linear because they involve matrix-vector multiplication and addition of noise vectors, which are linear operations.

---

## Non-Linear Models

Non-linear models do not have these straightforward properties. When the state transition or observation models are non-linear, they cannot be simply represented as matrix operations. This is where the Extended Kalman Filter (EKF) comes into play, which approximates these non-linear models as linear ones around the current state estimate using  **_Jacobian Matrices_**.

A **non-linear model** is one in which the relationship between variables cannot be represented as a straight line. These models can include polynomials, exponentials, trigonometric functions, etc. Mathematically, they can be represented as:

$\ y = f(x) \$

where $\ f(x)\$ is a non-linear function.

For dynamic systems, non-linear models for state transition and observations are:
1. **State Transition Model:** $\ x_k=f(x_{k−1},u_{k−1})+w_{k-1} \$
2. “**Observation Model:** $\ z_k= h(x_k) + v_k​ \$

Here, *f* and *h* are non-linear functions.
