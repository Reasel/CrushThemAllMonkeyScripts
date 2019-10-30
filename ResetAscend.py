from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import random
import time
import math


def touch(x1, x2, y1, y2):
	startY = random.randrange(y1, y2)
	startX = random.randrange(x1, x2)
	endX = random.randrange(x1, x2)
	endY = random.randrange(y1, y2)
	device.drag((startX, startY),(endX, endY), 0.25,3)

def clickButtonByCords(buttonName, x1, x2, y1, y2):
	print "Click the " + buttonName + " button..."
	touch(x1, x2, y1, y2)
	time.sleep(2)

def clickButton(button):
	print "Click the " + button[2] + " button..."
	touch(button[0][0], button[0][1], button[1][0], button[1][1])
	time.sleep(2)

def wakeupPhone():
	print "Unlocking Phone..."
	print "   Waking up..."
	device.wake()

# Will need to configure this function for your specific lock.
def unlockPhone():
	print "   Swiping right..."
	device.drag((170, 1700),(1200, 1700), 1,3)
	time.sleep(1)
	print "   Entering Password..."
	touch(316, 1505)
	time.sleep(500 / 1000)

	touch(1111, 1530)
	time.sleep(500 / 1000)

	touch(1111, 1530)
	time.sleep(500 / 1000)

	touch(290, 1935)
	time.sleep(500 / 1000)

def betterSleep(n):
	minuteNum = int(math.floor(n / 60))
	secondNum = n % 60
	if minuteNum <= 9:
		minuteStr = "0" + str(minuteNum)
	else:
		minuteStr = str(minuteNum)
	if secondNum <= 9:
		secondStr = "0" + str(secondNum)
	else:
		secondStr = str(secondNum)
	total = "\rSleeping for " + minuteStr + ":" + secondStr + "..."
	print "Sleeping for " + minuteStr + ":" + secondStr + "...",
	time.sleep(1)
	n -= 1
	while (n > 0):
		minuteNum = int(math.floor(n / 60))
		secondNum = n % 60
		if minuteNum <= 9:
			minuteStr = "0" + str(minuteNum)
		else:
			minuteStr = str(minuteNum)
		if secondNum <= 9:
			secondStr = "0" + str(secondNum)
		else:
			secondStr = str(secondNum)
		print "\rSleeping for " + minuteStr + ":" + secondStr + "...",
		time.sleep(1)
		n -= 1
	print total
	print "Sleep complete                                                              "




# connection to the current device, and return a MonkeyDevice object
device = MonkeyRunner.waitForConnection(10000, "yourdevicenamehere")


# Configure these yourself
Cancel = ((420, 550),(1600, 1710), "cancel")
Ascend = ((45, 140),(66, 140), "ascend")
Normal = ((350, 620),(1980, 2100), "normal")
GreenCheck = ((900, 1030),(1600, 1700), "green check")
OK = ((573, 877),(2333, 2450), "OK")

while True:
	if "OFF" in device.shell("dumpsys nfc | grep 'mScreenState='"):
		wakeupPhone()

	if "ON_LOCKED" in device.shell("dumpsys nfc | grep 'mScreenState='"):
		unlockPhone()

	print "Should be in the phone..."
	betterSleep(15)

	print "Spamming the back key..."
	device.shell("input keyevent 4")
	device.shell("input keyevent 4")
	device.shell("input keyevent 4")
	device.shell("input keyevent 4")
	device.shell("input keyevent 4")
	device.shell("input keyevent 4")

	clickButton(Cancel)

	clickButton(Ascend)

	clickButton(Normal)

	clickButton(GreenCheck)

	print "Waiting for rewards screen..."
	time.sleep(6)

	clickButton(OK)

	print "Skipping reward start button..."
	device.shell("input keyevent 4")


	print "Skipping reward confirmation..."
	device.shell("input keyevent 4")

	print "Locking phone..."
	device.shell("input keyevent 26")
	# Do the math on how long you want to wait for each Ascend. For me I did 12 minutes which was roughly to stage 140 with a dream active.
	# It is in seconds
	betterSleep(720)
