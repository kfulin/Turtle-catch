# Turtle-catch 🐢🎯

A fun and educational ROS 2 (Humble) project based on the **Turtlesim** simulator.  
This project simulates a turtle robot that catches randomly spawned turtles by navigating the shortest path to its target.  


---

## Project Overview

This project implements a small-scale simulation with three ROS 2 nodes:

- **`turtle_spawner`** – randomly spawns turtles and tracks their positions.
- **`turtle_controller`** – moves the main turtle (`turtle1`) using a proportional controller to catch others.
- **`turtlesim_node`** – provided by the `turtlesim` package to visualize turtle motion.

When the main turtle reaches a spawned turtle, the `turtle_controller` notifies the `turtle_spawner` to remove (catch) it.

---

## Features

- Turtle spawning at random positions.
- Live publishing of turtle positions via a custom message.
- Navigation to closest turtle using P-controller.
- Catching turtles via service communication.
- Parametrizable launch file support.

---

## Package Structure

```
turtle_catch_ws/
├── src/
│   ├── turtlesim_catch_them_all/    # Main logic (controller + spawner nodes)
│   ├── turtle_interfaces/         # Custom messages and services
│   └── turtle_bringup/            # Launch and param files
```

---

## Dependencies

Make sure you have the following installed:

- ROS 2 Humble
- `turtlesim` package

Install missing dependencies:

```bash
sudo apt update
sudo apt install ros-humble-turtlesim
```

---

## How to Run

### 1. Clone and build the workspace

```bash
mkdir -p ~/turtle_catch_ws/src
cd ~/turtle_catch_ws/src
git clone https://github.com/YOUR_USERNAME/Turtle-catch.git
cd ..
colcon build
source install/setup.bash
```

### 2. Launch the project

```bash
ros2 launch turtle_bringup turtlesim_catch_them_all.launch.xml
```

---

## Communication Overview

### Topics

| Topic | Type | Description |
|-------|------|-------------|
| `/turtle1/pose` | `turtlesim/msg/Pose` | Main turtle position |
| `/turtle1/cmd_vel` | `geometry_msgs/msg/Twist` | Control commands |
| `/alive_turtles` | `turtle_interfaces/msg/TurtleArray` | Active turtles list |

### Services

| Service | Role |
|---------|------|
| `/spawn` | Spawns a new turtle |
| `/kill` | Kills an existing turtle |
| `/catch_turtle` | Custom service to notify turtle has been caught |

---

## Parameters

You can customize behavior through parameters in the YAML config:

```yaml
# config.yaml
turtle_controller:
  ros__parameters:
    catch_closest_turtle_first: true

turtle_spawner:
  ros__parameters:
    spawn_frequency: 1.0
    turtle_name_prefix: "enemy_"
```

---

## Launch File

Located in `turtle_bringup/launch/turtlesim_catch_them_all.launch.xml`, it launches:

- turtlesim node
- turtle_controller
- turtle_spawner
- with parameter loading

---

## Screenshot / Demo

![image](https://github.com/user-attachments/assets/e7c40324-7f27-4340-bfcd-3f31656eb3b2)
![image](https://github.com/user-attachments/assets/6b72cb5a-8680-47c5-92cf-b2a5f3ea07a8)


<!--
---

## Credits

This project is based on the final course project from [ROS 2 for Beginners – Udemy Course](https://www.udemy.com/course/ros2-for-beginners/).
-->

---

## License

MIT License

