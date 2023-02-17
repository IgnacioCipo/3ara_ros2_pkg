# 3ara_ros2_pkg
I have created a ROS package named "3ara_ros2_pkg" 

Repo to store the second version of the software of my robotic arm.
## Requierments
* Ubuntu 22.04 Jammy Jellyfish
* ROS2 Humble Hawksbill
* Python3.

## How to run
1) Open a terminal and source your ROS distro:
```
source /opt/ros/humble/setup.bash
```

2) Move to your ROS workspace path and run:
```
. install/setup.bash
```
3) In order to give your user permission to use the serial port run:

```
sudo chmod 666 /dev/rfcomm0
```

3) Run publisher node:
```
ros2 run 3ara_ros2_pkg publisher
```
4) Open another terminal and repeat steps 1 and two

5) Run publishToSTM32 node:

```
ros2 run 3ara_ros2_pkg publishToSTM32
```

