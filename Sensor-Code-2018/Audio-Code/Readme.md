# Speaker Code
**Last updated on 12/6/2018**

Welcome to the King's Legacy 2018 Speaker Code - an implementation of Python 3's pyaudio module using sockets and a callback function to ensure a smooth and clear transfer of live audio from one device to another.

This file serves as a documentation which explains:
* The User Guide
* Known issues and practical solutions
* How the Code is constructed
* Future plans to improve the code

Currently, this code has been written in a basic, low level manner and is considerably tedious to run. At some point it will be updated so that it will be easier to use.
## User Guide
**Setting up the Microphone**
1. Plug the USB microphone into one of the USB sockets on the pi.
2. On the taskbar at the top, click the top left icon, hover over **Preferences** and click **Audio Settings**
3. Click on the **Sound Card** dropdown menu at the top and click the USB PnP OOOOOOOOO
4. If a separate window with tickboxes appears, **check all the boxes**.
	* If not, then please click on the **Select Controls** button and ensure that **all boxes are ticked**.
5. A vertical slider should appear. This indicates the volume of the microphone input. Drag this slider to full (all the way to the top).
6. Click the **Make Default** button to ensure that the pi does not revert back to its original soundcard settings.

At this point, your microphone is ready to go!

**How to start the Pyaudio Server**
1. On the server side of the potential connection, run the code that is named "audioServer.py". The code should not output anything.
	- If the code complains about anything to do with ALSA, please ignore them.
	- As long as the code has not crashed, then everything is working correctly.
2. On the client side of the potential connection, run the code that is named "audioClient.py". The code should not output anything.
	- Please input the IP address of the server when asked.
	- If the code complains about anything to do with ALSA, please ignore them.
	- As long as the code has not crashed, then everything is working correctly.

At this point, you are all good to go!

## Known issues and Practical Solutions
1. The audio output is garbled (extremely unclear):
	- This is most likely because the internet connection between the client and the server is poor.
	- It is also possible that the microphone is spoilt or broken. In which needs to be checked with code that is not reliant on internt.
	- The speaker output is going back into the microphone (because they are close together) and is causing a loop. This may spoil both the speaker and the microphone.
	- The code has some overlooked bugs which MUST BE REPORTED IMMEDIATELY.
2. The audio output is too quiet:
	- Turn the volume up on your laptop or desktop.
	- Earphones/Headphones may be an issue
	- Ensure that the USB microphone is properly configured on the pi (refer to the user guide at **Setting up the Microphone**)
	- Try to bend the USB (not too hard of course). If you can easily bend it, then it's 200% broken.
	- The code has some overlooked bugs which MUST BE REPORTED IMMEDIATELY.
3. There is no audio output:
	- Ensure that you have followed the steps regarding **Setting up the Microphone** and **How to start the Pyaudio Server** in the user guide.

## How the code is constructed
**Server Code** - *audioServer.py*

The server code uses TCP sockets - this ensures that the audio is always sent without problems and if there are problems, it will keep trying to send the data until it succeed.
**Client Code** - *audioClient.py*

**Constants** - *constants.py*

**Audio Class** - *audioPlayer.py*

