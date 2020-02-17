# ros_adeept_mars_rover
This ros package is intended for the kit found here: https://www.adeept.com/adeept-mars-rover-picar-b-wifi-smart-robot-car-kit-for-raspberry-pi-3-model-b-b-2b-speech-recognition-opencv-target-tracking-stem-kit_p0117_s0030.html

The ds4_driver(PS4 ROS Driver) source and installation guides can be found here: http://wiki.ros.org/ds4_driver. 

The tele_ps4_joystick package was created by me to use the information coming from the ps4 controller to control the robot.

## Getting Started
- First make sure you follow the ds4_driver guides to connect the ps4 controller to your RPi or any SBC of your choice either by wireless or wire. 
- Then clone this tele_ps4_joystick package in your catkin/src path
- You should also clone the latest ds4_driver in your catkin/src 
- catkin_make, to compile everything 

### Demo Run
Open a terminal and Roslaunch the Joystick Driver:
```
roslaunch ds4_driver ds4_twist.launch
```
Then use rostopic list and find the topic related to the twist message of the joystick. Afterwards rostopic echo that topic and ensure that your getting new messages when your moving the Analog Joystick. 

Open a new terminal and navigate to the scripts folder in tele_ps4_joystick package and run this node in python3:
```
python3 JoyStickControl.py
```
Controls for the PS4 Joystick:
```
R2: Forward
L2: Back
Left Analog Stick: Steering Control
```

### Future Updates
- Using the Right Analog Stick to change the position of the camera.
- Tele-operation controls using a client keyboard. 
- Obstacle Detection and Identification of Objects using Deep Learning. Might use an edge product or cloud so i could offload my inference. 
- V-Slam using the RGB Camera and possible integration with Ultrasonic Sensor.


