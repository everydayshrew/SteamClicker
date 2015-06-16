import win32api,win32con,win32gui,time,math

def Click(x,y):
	win32api.SetCursorPos((x,y))
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y)

def Question(value):
	if value == "y" or value == "Y":
		return True
	else:
		return False

def ChangeLane(lane):
	OFFSET = (100*lane) - 200
	x,y = lane_x+OFFSET, lane_y
	Click(x,y)

def Upgrade():
	x,y = a+200, b+75
	Click(x,y)
	time.sleep(0.1)
	x,y = a+200, b+175
	Click(x,y)
	time.sleep(0.1)
	x,y = a+200, b+225
	Click(x,y)
	time.sleep(0.1)
	x,y = a+200, b+255
	Click(x,y)
	time.sleep(0.1)

def DelayCheck(Delay):
	if Delay < 0.01:
		return 0.01
	else:
		return Delay

##################################################################

DISTANCE = 150
OFFSET = -100
MODE = 1
PAUSE = False
CYCLE = True
DELAY = 0.05

print "STEAM CLICKER V.1.0"
print "-------------------"
print "This program will cycle through lanes and click on enemies."
print
print "Please choose a mode:"
print "1) No-Upgrade Mode"
print "2) Auto-Upgrade Mode"

EXIT = False
while not EXIT:
	value = raw_input('Choice: ')
	value = str(value)
	if value == "1" or value == "2":
		if value == "1":
			if Question(raw_input("This will just do standard clicking/cycling. Are you sure? (Y/N) ")):
				MODE = 1
				EXIT = True
			else:
				print "Invalid Choice!"
		if value == "2":
			if Question(raw_input("This will try to upgrade your damage based on algorithms. Are you sure? (Y/N) ")):
				MODE = 2
				EXIT = True
			else:
				print "Invalid Choice!"
	else:
		print "Invalid Choice!"

print "Move your cursor to the center of the gold icon, then hit the 'x' key:",
while True:
	if win32api.GetAsyncKeyState(ord('X')):
		a, b = win32api.GetCursorPos()
		print " DONE!"
		break
time.sleep(0.5)

enemy_x = a + 600
enemy_y = b + 160
lane_x = a + 1100
lane_y = b

print ""
print "::: TO CHANGE LANES, HIT 1 2 OR 3 AT ANYTIME! :::"
print "::: TO STOP PROGRAM, HIT X WHILE UNPAUSED! :::"
print "::: TO PAUSE PROGRAM, HIT PAUSE KEY AT ANYTIME! :::"
print "::: TO STOP AUTO-CYCLING, HIT C WHILE UNPAUSED! :::"
print "::: + or - KEYS WILL CHANGE DELAY OF CLICKS :::"
time.sleep(2)

i = 0
k = 1

x,y = lane_x-OFFSET,lane_y
Click(x,y)

while True:

	if not PAUSE:
		i += 1
		if i < 25:
			x,y = enemy_x, enemy_y
			Click(x,y)
		elif i>=25 and i<50:
			x,y = enemy_x-DISTANCE, enemy_y+DISTANCE
			Click(x,y)
		elif i>=50 and i<75:
			x,y = enemy_x, enemy_y+DISTANCE*2-20
			Click(x,y)
		elif i>=75 and i<100:
			x,y = enemy_x+DISTANCE, enemy_y+DISTANCE
			Click(x,y)
		else:
			if CYCLE:
				ChangeLane(k)
				k += 1
				if k > 3:
					k = 1
			if MODE == 2:
				Upgrade()
			
			i = 0
			x,y = enemy_x, enemy_y+DISTANCE+10
			Click(x,y)

		if win32api.GetAsyncKeyState(ord('X')):
			break

		if win32api.GetAsyncKeyState(ord('C')):
			if CYCLE:
				CYCLE = False
				print "Cycle Change: OFF"
			else:
				CYCLE = True
				print "Cycle Change: ON"
			time.sleep(0.1)

		if win32api.GetAsyncKeyState(ord('1')):
			k = 1
			ChangeLane(1)
			time.sleep(0.1)

		if win32api.GetAsyncKeyState(ord('2')):
			k = 2
			ChangeLane(2)
			time.sleep(0.1)

		if win32api.GetAsyncKeyState(ord('3')):
			k = 3
			ChangeLane(3)
			time.sleep(0.1)

		if win32api.GetAsyncKeyState(0x6B):
			DELAY = DelayCheck(DELAY + 0.01)
			time.sleep(0.1)

		if win32api.GetAsyncKeyState(0x6D):
			DELAY = DelayCheck(DELAY - 0.01)
			time.sleep(0.1)

	if win32api.GetAsyncKeyState(0x13):		# Pause Button
		if PAUSE:
			PAUSE = False
			print "Unpaused"
		else:
			PAUSE = True
			print "Paused"
		time.sleep(0.1)

	time.sleep(DELAY)

print "Program successfully ended!  Enjoy your 'hard earned' rewards -shrew"
time.sleep(4)
