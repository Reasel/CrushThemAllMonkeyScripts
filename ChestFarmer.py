from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import commands
import sys
import random
import time
import math

TotalAds = 0

def touchRange(x1, x2, y1, y2):
	startY = random.randrange(y1, y2)
	startX = random.randrange(x1, x2)
	endX = random.randrange(x1, x2)
	endY = random.randrange(y1, y2)
	device.drag((startX, startY),(endX, endY), 0.05,3)

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


def clickChestRange(chestRange):
	print "Clicking chest area..."
	for x in range(chestRange[0][0], chestRange[0][1], 30):
		#touch((x + random.randrange(-5, 5)), random.randrange(chestRange[1][0], chestRange[1][1]))
		touchRange((x + random.randrange(-5, -1)), (x + random.randrange(1, 5)), chestRange[1][0], chestRange[1][1])

def CheckWatchAd():
	global TotalAds
	print "Checking for ad..."
	pixel = device.takeSnapshot().getRawPixel(811, 1283)
	if pixel[1] == 74 and pixel[2] == 223 and pixel[3] == 255:
		StartAd = ((534, 911),(1185, 1364), "start ad")
		GetFlooz = ((645, 850),(1666, 1760), "get flooz")
		print "Ad found starting!!!!"
		clickButton(StartAd)
		time.sleep(35)
		print "Backing out after the ad is done..."
		device.shell("input keyevent 4")
		time.sleep(3)
		clickButton(GetFlooz)
		TotalAds +=1
		print "Watched a total of " + str(TotalAds) + " ads so far!"


# connection to the current device, and return a MonkeyDevice object
device = MonkeyRunner.waitForConnection(10000, "a60e0c51")

ChestRange = ((480, 1392), (565, 575))

while True:
	clickChestRange(ChestRange)
	CheckWatchAd()
	time.sleep(2)





#578 1519
#875 1635


# CTA package is com.godzilab.idlerpg
# Width  is: 1440
# Height is: 2560
# Chests are 50 wide

# Height 550-570
# Width 480-1370

#device.wake()
#result = device.takeSnapshot()
#
#result.writeToFile('C:/Users/tmjelde/Documents/AndroidDev/screenshots/lockscreen.png','png')
#device.drag((170, 1700),(1200, 1700), 1,3)
#device.type('TESTING')
print "end of script"