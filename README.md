# RoboCup-2018-Driving-Code
This is the final edit of the code that the King's Legacy team will be using during the RoboCup Rapidly Manufactured Robotics League, Montreal, 2018 
----------------------------------------------------------------------------------------------------------------------------

# Resetting a Dynamixel ID

1.	Navigate to RoboCup-2018-Driving-Code/Dynamixel-Utilities
2.	Run the file dxl_utils.py
3.	Follow the steps as outlined by the code

# Testing A Servo’s Capability

1.	Navigate to RoboCup-2018-Driving-Code/Dynamixel-Utilities
2.	Run the file testServo.py

# Driving the EmuBot with Camera Feed

1.	Go to any MacBook
2.	Enter the password (“raspberry”)
3.	Connect to WiFi called Kings_Legacy.Emubot.1 (or .2, depending on which emuBot is being used)
4. If prompted with password, enter “raspberry”
5.	Open a terminal window
6.	Enter ssh pi@192.168.100.1
7.	Enter the password (“raspberry”)
8.	Enter cd Desktop/Server-Code-2018/
9.	Enter python3 RoboCupServer-Current.py
10.	The server is now running, leave this terminal window be
11.	Navigate to Desktop/RoboCup-2018-Driving-Code/CurrentEmuBotCode2
12.	Make sure the gamepad is plugged in to the laptop
13.	Open client.py in IDLE3 and run
14.	Go to, under the linux control bar at the top Terminal > New Terminal
15.	In this new window, navigate to Desktop/RoboCup-2018-Driving-Code/CurrentEmuBotCode2 via terminal
16.	Enter Start_MacStream.sh
17.	Go to, under the linux control bar at the top Terminal > New Terminal
18.	In this new code window, follow steps 5-7
19.	Run Start_PiStream.sh
20.	Cache should fill up and have a camera stream via mplayer

# Driving the FlipperBot

1.	Go to any MacBook
2.	Enter the password (“raspberry”)
3.	Connect to WiFi called Kings_Legacy.Flipperbot (or .2, depending on which emuBot is being used) If prompted with password, enter “raspberry”
4.	Open a terminal window
5.	Enter ssh pi@192.168.100.1
6.	Enter the password (“raspberry”)
7.	Enter cd Desktop/Server-Code-2018/
8.	Enter python3 RoboCupServer-Current.py
9.	The server is now running, leave this terminal window be

10.	Navigate to Desktop/RoboCup-2018-Driving-Code/Client-Code-2018/CurrentFlipperCode
11.	Make sure the gamepad is plugged in to the laptop
12.	Open client.py in IDLE3 and run

13.	Go to, under the linux control bar at the top Terminal > New Terminal
14.	In this new window, navigate to Desktop/RoboCup-2018-Driving-Code/Client-Code-2018/CurrentEmuBotCode2 via terminal
15.	Enter bash Start_MacStream.sh

16.	Go to, under the linux control bar at the top Terminal > New Terminal
17.	In this new code window, follow steps 5-7
18.	Run Start_PiStream.sh
19.	Cache should fill up and have a camera stream via mplayer

# Sensors: CO2 and Temperature

1.	Follow Steps 1-5 under “Driving the EmuBot”
2.	Enter cd Desktop/Server-Sensor-Code
3.	Enter python3 sensors.py


# Sensors: Visual

1.	Follow Steps 1-5 under “Driving the EmuBot”
2.	Go to, under the linux control bar at the top Terminal > New Terminal
3.	Enter cd /Desktop/Sensory-Abilities-2018/Sensor-Code-2018/Vision-Code
4.	Run any of:
   a.	QR Code (my_motion_QRCode.py)
  b.	Rotation Code (my_motion_rotation_shadow.pyb)
With the command: bash Start_MacStreamSensors.sh | python <filename>
6.	Leave this terminal window be
7.	Connect to robot WiFi
8.	Go to, under the linux control bar at the top Terminal > New Terminal
9.	Enter ssh pi@192.168.100.1
10.	Enter the password (“raspberry”)
11.	Enter cd Desktop/Server-Code-2017/
12.	Run bash Start_PiStream.sh
13.	Cache should fill up and have a camera stream via python

