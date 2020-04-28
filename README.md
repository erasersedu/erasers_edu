# Simple RGBD Reader Template

The object of this repository is to create a template that students can use to use an RGBD camera

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
You should have install ROS.
You must Install turtlebot repository
You should have create a workspace
```

### Installing

You must install ros_numpy. If you are using other version of ROS, you just have to change to the distribution which you are using.

```
sudo apt-get install ros-kinetic-ros-numpy
```

Then get in the src folder of your workspace
```
cd ~/erasersedu_ws/src
```
After that clone the repository there
```
git clone https://github.com/erasersedu/erasers_edu.git
```
next step is to compile the new package even thoug you are now using CPP
```
touch ~/erasersedu_ws/src/erasers_edu/CMakeLists.txt
cd ~/erasersedu_ws/
catkin_make
```
End with an example of getting some data out of the system or using it for a little demo

## Running the tests

To create a test of the template working you should launch the turtlebot
```
roslaunch turtlebot_start robot_complete.launch
roslaunch turtlebot_start arm_head.launch
```

### Break down into end to end tests

To see if everything is working, you should run both codes that are giving by using the launch provided

```
roslaunch erasers_edu vision_test.launch
```

### And coding style tests

Now you just have to look for the comments in the nodes controlToPostion.py and kinect_reader.py for writing the code and make your part. They are located in the scripts folder of the vision package

## Authors

* **Victor Hugo Sanchez** - *Initial work* - [huguinsanchez](https://github.com/huguinsanchez)
* **Luis Contreras** - *Updates and maintenance*

