# Reelsteady GO Bot!

Reelsteady GO's algorithm is amazing, but the UI is in no way optimised to handle bulk. Not wanting to wait for GoPro to help them out on the UI part (which they hopefully will!), I wrote this dirty piece of code to automate reelsteady.

This script will read a given folder with gopro files, automatically open reelsteady GO instances and use keyboard commands and mouse clicks to open files, configure smoothness settings and start rendering.

This program is meant to run when not using the PC. I run it on my pc at night, or on my laptop. Even when it's waiting for renders to complete, it will regularly switch through the open windows and check for completion.

It works based on the image-based mouse clicks from the PyAutoGUI library, which searches for small snippets of screenshots to find the correct buttons and locations to click inside Reelsteady. The text based controls build into the pywinauto library would have been way easier, but unfortunately the reelsteady go interface does not support this.

`Warning: this is extremely beta. It was only tested on my own pc, and even there it sometimes fails. It might fail just for slight display differences of your windows machine, or on a slower machine since some features are based on timing (for that last part, increase the delays in config.py) Please use for the purpose of testing only for now. `

With my lack of time to put into programming, pull-requests are very welcome!

## Preparation:
- Add all the gopro files to stabilise in one folder on your pc somewhere

## Usage:
- Download/checkout the folder
- Configure the base folder and project folder to point to your gopro files in config.json
- Set all the preferred stabilisation settings in config.json
- Close or minimise all other programs
- From the terminal, navigate to the reelsteady-bot folder
- Run 'py run.py'
- Touch nothing, let the program do its thing!

## Requirements:
- Windows
- Python3 + pip

### Install
Running `pip install -r requirements.tx` installs:
- pywinauto
- pyautogui
- pillow
- opencv-python


## Future ideas:
- Turn into actual serious code with proper naming, tests, documentation, error handling, and so on
- Make compatible with osx
- Build a UI on top of this script with queuing features, selection of files to stabilise, configuration of smoothness settings, progress management, pause feature, and so on
