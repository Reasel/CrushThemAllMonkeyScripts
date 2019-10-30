# Crush Them All Scripts run through [Monkey Runner](https://developer.android.com/studio/test/monkeyrunner)
Welcome! This is the scripts that I made to do things in the game Crush Them All.

You will need to configure either Android Debug Bridge to a physical device OR have it connect to a emulated device.
Either way this runs through using monkeyrunner.bat to run a python script on your device.

All scripts will be coded to my device so you will need to configure that for each script

Will need to configure `device = MonkeyRunner.waitForConnection(10000, "a60e0c51")` to your device id found by command `adb devices` in powershell or cmd.

All scripts were run on a Galaxy S7 on Android 8.0. If you are running something different then you will need to adjust the coordinates used in the various scripts.


## [Chest Farmer](https://github.com/Reasel/CrushThemAllMonkeyScripts/blob/master/ChestFarmer.py)
This script is designed to do a series of drag events in the area where chests are found. This is to avoid having to do 'touches' which I found were not very reliable.

You will need to configure the ChestRange variable to your specific area. I would recommend using the developer option in your device to find these.

You will also need to configure your CheckWatchAd function for the exact pixel to search for the color of the watch ad button. For this you will want to again use the developer tools to pick a point inside the button and then use `device.takeSnapshot().getRawPixel(811, 1283)` to find the color of the pixel. It will be in the form `(a, r, g, b)` then replace the values of the if statement for that function to match what you found.

Then you will have to configure the coord of the StartAd button and GetFlooz button as well. This is so the script knows the bounds of the buttons.


## [Ascension Reset](https://github.com/Reasel/CrushThemAllMonkeyScripts/blob/master/ResetAscend.py)
This script is designed to ascend and then wait a certain amount of time before doing so again.

Read through the scripts code and configure where required.
