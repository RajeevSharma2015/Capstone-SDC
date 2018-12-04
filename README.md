# IndiConcept Team

This is the IndiConcept team repository for capstone project of Udacity's Self-Driving Car Engineer Nanodegree program. The key objective of this project is to do system integration around ROS framework. 

#### The team members are:

 * Rajeev Kumar Sharma ( rajeevsharma.phd@gmail.com )
 * Malik Khan ( mayk9999@gmail.com )
 
### Project Introduction
For this project, our team designed a fully autonomous vehicle system, initially to be tested out on a simulator, and then on Udacity’s real self-driving car. This project has three parts: 
(1) Traffic Light detection 
(2) Control 
(3) Waypoint Following

In Traffic Light Detection, we designed a detection node that would take the current waypoints of the car and an image taken from the car and determine if the closest traffic light was red or not. For Control, we designed a drive-by-wire (dbw) node that could take the target linear and angular velocities and publish commands for the throttle, brake, and steering of the car. 

Finally, the Waypoint Follower would take information from the traffic light detection and the current waypoints and update the target velocities for each waypoint based on this information


### Building and running the project

This project requires the GPU version of Tensorflow along with the CUDA and cuDNN libraries, python 2.7, as well as the following libraries defined more specifically in `requirements.txt`:

  * Flask
  * attrdict
  * eventlet
  * python-socketio
  * numpy
  * Pillow
  * scipy
  * keras
  * h5py
  * requests

These modules can be installed using: `pip install -r requirements.txt` from the root of the project.  

Traffic light classifier model is take from : 

Next go into the `/ros` directory and run `catkin_make` to build the ROS project. Be sure to source the project by running `. devel/setup.sh`.  At this point, if your environment is set up properly, you should be able to launch ROS with `roslaunch launch/styx.launch`.

Reference Video Links: 
(a) Project execution while CAMERA OFF and SDC running in autonomous mode
    Youtube link :  https://youtu.be/ZHrT34p2jiw.  
(b) Project execution wjile CAMERA ON, Traffic Light detection ON & Latency observed
    Youtube link : 

Reference Images: 
All reference images and project report kept in IMG-DOC folder 
