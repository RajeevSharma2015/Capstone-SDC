# IndiConcept Team

This is the IndiConcept team repository for capstone project of Udacity's Self-Driving Car Engineer Nanodegree program. The key objective of this project is to do system integration around ROS framework. 

#### The team members are:

 * Rajeev Kumar Sharma ( rajeevsharma.phd@gmail.com , Delhi INDIA)
 * Malik Khan ( mayk9999@gmail.com , Adelaide Australia)
 
### Project Introduction
For this project, our team designed a fully autonomous vehicle system, initially to be tested out on a simulator, and then on Udacity’s real self-driving car. This project has three parts: 
(1) Traffic Light detection 
(2) Control 
(3) Waypoint Following

In Traffic Light Detection, we designed a detection node that would take the current waypoints of the car and an image taken from the car and determine if the closest traffic light was red or not. For Control, we designed a drive-by-wire (dbw) node that could take the target linear and angular velocities and publish commands for the throttle, brake, and steering of the car. 

Finally, the Waypoint Follower would take information from the traffic light detection and the current waypoints and update the target velocities for each waypoint based on this information

### Installation 
* Be sure that your workstation is running Ubuntu 16.04 Xenial Xerus or Ubuntu 14.04 Trusty Tahir. [Ubuntu downloads can be found here](https://www.ubuntu.com/download/desktop).
* If using a Virtual Machine to install Ubuntu, use the following configuration as minimum:
  * 2 CPU
  * 2 GB system memory
  * 25 GB of free hard drive space

The Udacity provided virtual machine has ROS and Dataspeed DBW already installed, so you can skip the next two steps if you are using this.

* Follow these instructions to install ROS
  * [ROS Kinetic](http://wiki.ros.org/kinetic/Installation/Ubuntu) if you have Ubuntu 16.04.
  * [ROS Indigo](http://wiki.ros.org/indigo/Installation/Ubuntu) if you have Ubuntu 14.04.
* [Dataspeed DBW](https://bitbucket.org/DataspeedInc/dbw_mkz_ros)
  * Use this option to install the SDK on a workstation that already has ROS installed: [One Line SDK Install (binary)](https://bitbucket.org/DataspeedInc/dbw_mkz_ros/src/81e63fcc335d7b64139d7482017d6a97b405e250/ROS_SETUP.md?fileviewer=file-view-default)
* Download the [Udacity Simulator](https://github.com/udacity/CarND-Capstone/releases/tag/v1.2).

### Usage
1. Clone the project repository
```bash
git clone https://github.com/udacity/CarND-Capstone.git
```
2. Install python dependencies
```bash
cd CarND-Capstone
pip install -r requirements.txt
```
3. Make and run styx
```bash
cd ros
catkin_make
source devel/setup.sh
roslaunch launch/styx.launch
```

### Simulation & Reference Video Links: 
(a) Project simulation test (video recording) - while CAMERA (Untick) & Manual (Untick). 
* Here SDC running in autonomous mode, camera OFF and TL detection is disabled. 

    Youtube link :  https://youtu.be/ZHrT34p2jiw.
    
    ##### Conculsion - Partial Feature Testing 
    Base_waypoint updator & follower is able to publish point on lane, and controller able to drive SDC smoothly on track. This simulation is tried on Udacity workspace. In this mode no latency observed. 
   
(b) Project simulation test (video recording) - while Manual (Untick), CAMERA (Untick) & TL classifier loaded
* Here SDC running in autonomous mode, Camera ON & Traffic light detection active
* Setup - Udacity GPU workspace 
* VGG16 - TL trained classifier used

    Youtube link : https://youtu.be/2t5HuuquY-8
    
    #### Conclusion - Fully Loaded Feature Testing
    * SDC start normally and initiate following waypoints
    * RED light detection happens, SDC usages braking to stop car
    * Traffic light change state GREEN, SDC able to detect and manage throttle to drive vehicle
    * Meanwhile setup latency seems plays significant role and final_waypoint update and following seems get disturbs
    * Submission and a final trial on Carla seems to be a way forward to test final result.

### Reference Images: 
Reference images and a project report is kept in IMG-DOC folder.

### References :
* 1. 
* 2. 
* 3. 
* 4. 
