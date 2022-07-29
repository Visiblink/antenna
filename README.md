![antenna](https://user-images.githubusercontent.com/82686470/181785394-e0dab79e-95db-4a7d-8e19-ee3339c7ae11.png)


Antenna is a simple python player for internet radio streams.


Running the application:
------------------------

To run the script, you'll need Python 3.x installed. You'll probably also need to install the playsound module using pip. The script runs on Debian 11, but might require alteration to run on other distributions or Windows.


General:
--------

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

The station database is in a python dictionary file called "antennarc" in your ~/.config directory. The file can be edited directly.
