# SDC Fun

This is the `SDC Fun` team repo for the capstone project of Udacity's Self-Driving Car Engineer Nanodegree. 

The team members are:

 * Rajeev Kumar Sharma (rajeevsharma.phd@gmail.com)
 * Malik Khan ( )


### Building and running the project

The original project repo can be found.,
which has a lot of information about environment, simulator, etc.

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
