# Kalman Filter and EKF Implementation

This repository contains implementations of various Kalman Filter algorithms, including a basic Kalman Filter, Extended Kalman Filter (EKF), and localization examples. The code is written in Python and includes detailed explanations and visualizations.

## Repository Structure

```
.
├── EKF-From-Scratch/       # Extended Kalman Filter implementation
├── KalmanFilter/           # Basic Kalman Filter implementation
├── Localization/           # Robot localization examples
└── Notes/                  # Theoretical explanations and mathematical foundations
```

## Prerequisites

- Python 3.11 or higher
- pip package manager


## Installation

1. Clone the repository:
```bash
git clone https://github.com/IremOztimur/AI4Robotics.git
cd AI4Robotics
```

2. Create and activate a virtual environment:
```bash
cd EKF-From-Scratch
make virtual # or make install to only install the dependencies
```

## Usage

### Extended Kalman Filter (EKF) SLAM

The EKF SLAM implementation demonstrates simultaneous localization and mapping:

```bash
cd EKF-From-Scratch
python ekf_main.py
```

Controls:
- Arrow keys to move the robot
- ESC or Q to quit

### Basic Kalman Filter

Run the 1D Kalman Filter example:

```bash
cd KalmanFilter
python kalmanFilter1D.py
```

### Localization

Run the robot localization example:

```bash
cd Localization
python localization.py
```

## Testing

Run the test suite:

```bash
cd Localization
python test.py
```

## Documentation

- `Notes/Covariance.md` - Detailed explanation of covariance matrices and their role in Kalman Filters
- `Notes/Kinematics.md` - Overview of kinematic equations used in motion models
- `EKF-From-Scratch/README.md` - Extended Kalman Filter theory and implementation details

## Cleaning Up

Remove Python cache files:

```bash
make clean
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Acknowledgments

- Based on the AI for Robotics course materials
- Pygame library for visualization
- NumPy and SciPy for mathematical operations
