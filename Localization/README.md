## Localization Problem
The robot localization problem involves determining the position and orientation of a robot within a known environment based on sensor measurements and prior knowledge.

### A simple illustration of the Localization steps
In this cycle, the robot follows these functions in order:
- Motion: The robot executes a motion command (e.g., moves to a new position).
- Sensing: After the motion, the robot senses its surroundings (e.g., detects the color of the current cell).

This cycle of motion and sensing is repeated iteratively as the robot moves through the environment and updates its belief about its position. 


<img width="1039" alt="localization-code-2" src="https://github.com/IremOztimur/AI4Robotics/assets/77894816/b1b63a0f-9dfa-42f0-8bc2-bfed4f83bd1b">
