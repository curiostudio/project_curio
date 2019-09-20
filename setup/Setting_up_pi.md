# Setting up the Pi
Raspberry Pi acts as the CPU in this product, while arduino is a hub for all user input and communicates with the Pi. Follow the instructions below to setup the Pi and install the required scripts. 

1. Format a 8GB/16GB SD Card with FAT32 file system. You can do this either in My Computer, by right clicking the SD card drive and clicking on Format. Or, you can format using the Windows Disk Management utility

2. Download the latest Raspberry Pi OS here. I am currently using Raspbian Buster

3. Use Balena Etcher software to copy OS you just downloaded on to the SD card. Follow on-screen instructions to do so

4. Insert the SD card into the Raspberry Pi slot and power ON the Pi. Its advisable to use an external monitor (PC or Pi display) for the first time setup. If you do not have a display, you can follow this tutorial to setup the Pi

5. The on-screen instructions will guide you to setup things like country, Wi-Fi connection, keyboard layout etc. At the end of this, skip the restart request. Open the applications menu (Raspberry icon in top left of the screen) and go to preferences and then to Raspberry Pi configuration. Under the interfaces tab, enable SSH, SPI, I2C and Remote GPIO. Now restart the Pi. 

## Setting up libraries: 

For the product to run properly, you will need some libraries to be installed first. In the future versions, this could be automated with an Installer Script, so that non-technical users can install/ configure all the required steps with ease. 

1. Go to applications menu, then to Accessories and then open Terminal. 

2. Create a new folder by typing mkdir curio. Now open the newly created folder by typing cd curio. This will enable you to install all the following scrips to be installed in this folder. 

3. Install GPIO library, by typing pip install rpi.GPIO

4. Install Serial library, by typing pip install pyserial

5. Install GrovePi library, by typing 
    1.  sudo curl -kL [dexterindustries.com/update_grovepi](http://dexterindustries.com/update_grovepi) | bash 
    2. sudo pip install grovepi
    3. sudo reboot

## Getting the scripts:

Now, its time to get the script(s) to run the product. 

1. Open a new terminal, and go to the curio folder, by typing cd curio

2. Now type, nano main_program.py. A new GNU nano window opens. 

3. Copy the code from [https://github.com/curiostudio/project_curio/blob/master/code/stepper_control.py](https://github.com/curiostudio/project_curio/blob/master/code/stepper_control.py) and paste it into the nano window. Press Ctrl + x (windows) and then press Y.
