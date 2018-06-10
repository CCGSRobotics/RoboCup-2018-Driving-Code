# FinalDrivingCodeForMontreal
This is the final edit of the code that the King's Legacy team will be using during the RoboCup Rapidly Manufactured Robotics League, Montreal, 2018 
-----------------------------------------------------------------------------------------------------------------------------
DRIVING CODE:
  ROBOT:
    Wireless code is put on the robot that is being controlled. It does not matter which robot it will be uploaded to, BUT you     will need to edit which mode each servo is at the beginning of the RoboCupServer-Current.py file.

  LAPTOP:
    The RoboCup-2018-Driving-Code (RCDC) is used by the laptop. You will need to access the file within RCDC that describes the robot you require to drive
  
  INSTRUCTIONS:
    1. Connect the robot to a power source and make sure it cannot damage itself or anything around in the rare occasion that the connection breaks and servos continue to move.
    2. Sign into the Laptop. Make sure you are connected to the correct robot's access point, this will take a few moments as the robot boots up and runs some preliminary files to establish an access point. It is important you access the right robot.
    3. Open one(1) terminal window. This is referred to as TW1.
    4. Within TW1 you will need to ssh into the robot. In this window, you will need to type "ssh pi@192.168.100.1". You will be prompted to enter a password. If you have not changed it on the raspberry pi within the robot, it will be "raspberry". NOTE: If an error occurs, in the middle of the error statement is a line of code. Run this code into the terminal command line and repeat this step
    5. Then enter "cd Desktop/Wless_code_RC18". This may be different depending on where you saved the file Wless_code_RC18
    6. After changing to the file Wless_code_RC18, you are required to run "python RoboCupServer-Current.py" to start the server code on the robot.
    7. On the laptop's desktop, you are required to open the RCDC file. Within this file are two more files, one for the EmuBot and one for the Flipper robot. Open the file coresponding to the robot you are driving.
    8. Within this file you will find a pythin script named client.py. Open this file and run the code. NOTE: You are required to have a controller connected to the laptop otherwise an error will be raised.
    9. See below for debugging statements.
  
  TROUBLESHOOTING:
    When running robot code:
      Incomplete packet:
        Make sure servos are recieving power and connected to the USB2AX
      Wrong Header:
        Source is unknown. Run the code multiple times until the error stops working. If repeated more than 10 times, reboot the robot, make sure all cables are plugged in and all hardware is recieving necesssary power requirements.
      Broken Joint or Broken Wheel:
        A number of servos would have broken. The ID will be displayed on the screen. The most common reason of this is if too much torque experienced by the servo. This is fixed by turning the servos on and off. If this error continues with no pressure on the servo, this servo will be required to be replaced.
    When running laptop code:
      Broken Pipe error:
        Make sure the robot's code is still running and does not contain print statments describing which joint or wheel is broken. See above "Broken Joint or Broken Wheel" after quitting the code and before repeating steps 6 and 8.
    
