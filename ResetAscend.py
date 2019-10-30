from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import random
import time
import math


def touchRange(x1, x2, y1, y2):
	startY = random.randrange(y1, y2)
	startX = random.randrange(x1, x2)
	endX = random.randrange(x1, x2)
	endY = random.randrange(y1, y2)
	device.drag((startX, startY),(endX, endY), 0.25,3)

def touch(x, y):
	#rint "Touching " + str(x) + ", " + str(y)
	device.touch(x, y, 'DOWN_AND_UP')

#def touchRange(x1, x2, y1, y2):
#	touch(random.randrange(x1, x2), random.randrange(y1, y2))

def clickButtonByCords(buttonName, x1, x2, y1, y2):
	print "Click the " + buttonName + " button..."
	touchRange(x1, x2, y1, y2)
	time.sleep(2)

def clickButton(button):
	print "Click the " + button[2] + " button..."
	touchRange(button[0][0], button[0][1], button[1][0], button[1][1])
	time.sleep(2)

def dragLeftRange(y1, y2):
	startY = random.randrange(y1, y2)
	startX = random.randrange(1250, 1320)
	endX = random.randrange(1100, 1300)
	endY = random.randrange(y1, y2)
	device.drag((startX, startY),(endX, endY), 1,3)

def clickChestRange(x1, x2, y1, y2):
	for x in range(x1, x2, 50):
		touch((x + random.randrange(-5, 5)), random.randrange(y1, y2))
		time.sleep(100 / 1000)
	manyClickRange(578, 875, 1519, 1635, random.randrange(2, 5))

def manyClickRange(x1, x2, y1, y2, numClick):
	baseX = random.randrange(x1, x2)
	baseY = random.randrange(y1, y2)
	for i in range(numClick):
		touch(baseX + random.randrange(-5, 5), baseY + random.randrange(-5, 5))
		time.sleep(200 / 1000)

def wakeupPhone():
	print "Unlocking Phone..."
	print "   Waking up..."
	device.wake()

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
device = MonkeyRunner.waitForConnection(10000, "a60e0c51")


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

	#clickButton("cancel", 420, 550, 1600, 1710)
	clickButton(Cancel)

	#clickButton("ascend", 45, 140, 66, 140)
	clickButton(Ascend)

	#clickButton("normal", 350, 620, 1980, 2100)
	clickButton(Normal)

	#clickButton("green check", 900, 1030, 1600, 1700)
	clickButton(GreenCheck)

	print "Waiting for rewards screen..."
	time.sleep(6)

	#clickButton("ok", 573, 877, 2333, 2450)
	clickButton(OK)

	print "Skipping reward start button..."
	device.shell("input keyevent 4")
	#clickButton("play", 604, 850, 2018, 2131)

	print "Skipping reward confirmation..."
	device.shell("input keyevent 4")

	print "Locking phone..."
	device.shell("input keyevent 26")
	betterSleep(720)

	#ButtonSearchAndClick("gains", 775, 1791, (0, 190, 214), 592, 850, 1761, 1865)
	#print "Checking for gains button..."
	#if (isPixel(775, 1791, (0, 190, 214))):
	#	print "Click the gains since last login button..."
	#	clickButton(592, 850, 1761, 1865)

	#ButtonSearchAndClick("news", 405, 131, (41, 24, 8), 1260, 1265, 66, 70)
	#print "Checking for news button..."		
	#if (isPixel(405, 131, (255, 0, 0))):
	#	print "Click the x button for the news..."
	#	clickButton(1260, 1265, 66, 70)

	#ButtonSearchAndClick("limited offer", 800, 2000, (255, 0, 0), 1265, 1275, 485, 495)
	#print "Checking for the limited offer button"
	#if (isPixel(800, 2000, (255, 0, 0))):
	#	print "Click the limited offer stuff..."
	#	clickButton(1265, 1275, 485, 495)

