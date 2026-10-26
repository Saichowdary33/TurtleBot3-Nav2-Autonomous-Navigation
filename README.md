TurtleBot3 Nav2 Autonomous Navigation

An autonomous mobile robot navigation project using ROS 2 Jazzy, Gazebo, and Nav2, featuring map-based navigation and obstacle avoidance.

Project Overview

This project aims to configure a TurtleBot3 robot to navigate autonomously in a simulated environment using ROS 2 and the Navigation2 (Nav2) stack.

Technologies Used

- ROS 2 Jazzy
- Gazebo
- Navigation2 (Nav2)
- TurtleBot3
- Python
- YAML configuration
- SLAM / Map-based Navigation

Project Structure

TurtleBot3-Nav2-Autonomous-Navigation/
├── config/
│   └── nav2_params.yaml
├── launch/
│   └── navigation.launch.py
├── office_map.pgm
├── office_map.yaml
└── README.md

Project Files

- config/nav2_params.yaml: Navigation configuration parameters.
- launch/navigation.launch.py: Launch file for starting the navigation setup.
- office_map.pgm: Occupancy-grid map image.
- office_map.yaml: Map metadata, including resolution and origin.

Prerequisites

Install and configure ROS 2 Jazzy, a compatible Gazebo installation, TurtleBot3 packages, and Nav2 on Ubuntu.

Setup

1. Create a ROS 2 workspace.
2. Place the project files in the appropriate package directory.
3. Install the required dependencies.
4. Build the workspace using "colcon build".
5. Source the workspace setup file.
6. Launch the navigation setup using the appropriate launch command for your package.

Note: Update the package name and launch command to match your actual ROS 2 package configuration.

Expected Outcome

The configured TurtleBot3 should be able to use a map for autonomous navigation in simulation. Obstacle avoidance depends on the robot model, sensor configuration, and Nav2 parameters.

Future Improvements

- Add simulation screenshots and demonstration videos.
- Document exact installation and launch commands.
- Add robot navigation results and obstacle-avoidance tests.
- Include a troubleshooting guide.

Author
Sai Chowdary
