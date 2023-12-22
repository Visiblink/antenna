![antenna](https://user-images.githubusercontent.com/82686470/185515011-58f0385a-7e4b-47b2-aa74-863b33e22ab1.png)


Antenna is a console player for internet radio streams.

This script has been tested by me on Debian 11 "Bullseye" and Debian 12 "Bookworm" for over a year without problems.

Installing the application:
---------------------------

To install on an amd_64 Debian 11 system: 

1. download the .deb file associated with the version 0.1.2 release.
2. as root, enter the folder with the .deb file and execute the following command: ```apt install ./antenna_0.1.2_amd64.deb```
3. to start the program, type ```antenna```
4. to uninstall type ```apt remove antenna```

On other systems, you can install as follows:

1. download the antenna.py script. Rename it "antenna." As root, make the file executable by typing ```chmod +x antenna```
2. place the file in /usr/bin/
3. make sure that python3, gst123, and libatk-adaptor are installed on your system.
4. type ```antenna``` to start the program.
5. to uninstall simply delete /usr/bin/antenna.


General navigation:
-------------------

All commands must be followed by the ENTER key.

Some terminal clients will permit you to paste with the Shift-CTRL-v key combination. This is handy for entering URLs.


To add a station:
-----------------

Press "a" at the main menu and enter the station URL and name at the prompts. 

Two good sources of station URLs are https://radio-locator.com and https://www.radio-browser.info. 


To play a stream from the list:
-------------------------------

Enter the number of the stream at the main menu prompt.


To delete a station:
--------------------

Press "d" at the main menu and enter the station number at the prompt.


To edit a station:
------------------

Press "e" at the main menu and enter any new information at the prompts.


To move a station:
------------------

Press "m" at the main menu and choose the station number at the prompt. Then enter "u" for up or "d" for down at the prompt. You can enter "u" or "d" as many times as you like. Enter "m" to return to the main menu.


To play a stream URL without adding it to the list:
---------------------------------------------------

Press "p" at the main menu and enter the URL at the prompt.


Database Location:
------------------

The station database is in a python dictionary file called "antennarc" in the ~/.local/share/antenna/ directory.
