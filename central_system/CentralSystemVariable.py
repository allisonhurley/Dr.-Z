#Declare Inputs Pin Variables
Phone_PIN = 26 #Pin number for Phone Activation input
#DistFace1_PIN = 27 ##Pin number for Facial Distraction Activation input
#DistFace2_PIN = 17 ##Pin number for Facial Distraction Activation 2 input
#Lane_PIN = 20 #Pin number for Departed Lane Signal Out of Lane input
#DrwFace1_PIN = 22 #Pin number for Facial Drowsy Activation input
#DrwFace2_PIN = 13 #Pin number for Facial Drowsy Activation 2 input
Voice_PIN = 16 #Pin number for Voice System User Request input
#FaceLane_PIN = 15 #Pin number for Facial and Lane system Activation input


#Declare Output Pin Variables
Hazards_PIN = 23 #Pin number for Hazards Activation output
Vibration_PIN = 5 #Pin number for Vibration Activation output
Voice1_PIN = 12 #Pin number for Activate Voice System output
Voice2_PIN = 6  #Pin number for Activate Voice System 2 output
Atomizer_PIN = 19 #Pin number for Atomizer Activation output

import RPi.GPIO as GPIO
import time 
import serial

GPIO.setwarnings(False)
'''
ser = serial.Serial(

	port='/dev/ttyS0' ,
	baudrate=115200,
	parity=serial.PARITY_NONE,
	stopbits=serial.STOPBITS_ONE,
	bytesize=serial.EIGHTBITS,
	timeout=1
)
'''
GPIO.setmode(GPIO.BCM)
GPIO.setup(Phone_PIN, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) #Create input pin for Phone Signal with pull down resistor
#GPIO.setup(DistFace1_PIN, GPIO.IN, pull_up_down =GPIO.PUD_DOWN)#Create input pin for Facial Distraction Signal with pull down resistor
#GPIO.setup(DistFace2_PIN, GPIO.IN, pull_up_down =GPIO.PUD_DOWN)#Create input pin for Facial Distraction 2 Signal with pull down resistor
#GPIO.setup(Lane_PIN, GPIO.IN, pull_up_down =GPIO.PUD_DOWN)#Create input pin for Lane Signal with pull down resistor
#GPIO.setup(DrwFace1_PIN, GPIO.IN, pull_up_down =GPIO.PUD_DOWN)#Create input pin for Facial Drowsy Signal with pull down resistor
#GPIO.setup(DrwFace2_PIN, GPIO.IN, pull_up_down =GPIO.PUD_DOWN)#Create input pin for Facial Drowsy 2 Signal with pull down resistor
#GPIO.setup(FaceLane_PIN, GPIO.IN, pull_up_down =GPIO.PUD_DOWN) #Create input pin for Facial and Lane Signal with pull down resistor
GPIO.setup(Voice_PIN, GPIO.IN, pull_up_down =GPIO.PUD_DOWN)#Create input pin for Voice Signal with pull down resistor
GPIO.setup(Hazards_PIN, GPIO.OUT) #Create Output pin for Hazards signal
GPIO.setup(Vibration_PIN, GPIO.OUT)#Create Output pin for Vibration signal
GPIO.setup(Voice1_PIN, GPIO.OUT)#Create Output pin for Voice signal
GPIO.setup(Voice2_PIN, GPIO.OUT)#Create Output pin for Voice 2 signal
GPIO.setup(Atomizer_PIN, GPIO.OUT)#Create Output pin for Atomizer signal


out_Hazards = 0
out_Atomizer = 0
out_Vibration = 0
out_Voice1 = 0
out_Voice2 = 0

def resetOutputs():
	global out_Hazards, out_Atomizer,out_Vibration,out_Voice1,out_Voice2
	out_Hazards = 0
	out_Atomizer = 0
	out_Vibration = 0
	out_Voice1 = 0
	out_Voice2 = 0

count=0 

in_Phone=0
in_distFace1=0
#in_DistFace2=0
in_Lane=0
#in_DrwFace1=0
#in_DrwFace2=0
in_Voice=0
 

def updateInput():
	global in_Phone, in_Voice, in_Lane , in_DistFace1, in_DistFace2, in_DrwFace1, in_DrwFace2
	in_Phone = GPIO.input(Phone_PIN)
	#in_DistFace1 = GPIO.input(DistFace1_PIN)
	#in_DistFace2 = GPIO.input(DistFace2_PIN)
	#in_Lane = GPIO.input(Lane_PIN)
	#in_DrwFace1 = GPIO.input(DrwFace1_PIN)
	#in_DrwFace2 = GPIO.input(DrwFace2_PIN)
	in_Voice = GPIO.input(Voice_PIN)
	#readInputLane()
	#readInputFace()

def printStates():
		#print " P F1 F2 F3 F4 Vo L | A Vb Vo1 Vo2 H "
		#print " {} {} {} {} {} {} {} | {}  {}  {}  {}  {} ".format(in_Phone, in_Voice, readInputLane(), out_Atomizer, out_Vibration, out_Voice1, out_Voice2, out_Hazards) #in_DistFace, in_DistFace2, in_DrwFace, in_DrwFace2,
		print " P F Vo L | A Vb Vo1 Vo2 H "
		print " {} {} {} {} | {}  {}  {}  {}  {} ".format(in_Phone, in_distFace1 ,in_Voice, in_Lane, out_Atomizer, out_Vibration, out_Voice1, out_Voice2, out_Hazards)
		print "\n"
		
'''
def readInputLane():
	input=ser.readline()
	if input[0:6]=="LANE_1":
		in_Lane=1
		return in_Lane
	elif input[0:6]=="LANE_0":
		in_Lane=0
		return in_Lane
		
	
			
		
def readInputFace():
	input=ser.readline()
	if input[0:6]=="DIST_1":
		in_distFace1=1
		return in_distFace1
	elif input[0:6]=="DIST_0":
		in_distFace1=0
		return in_distFace1
	
'''			

def updateLogic():

	global out_Hazards, out_Voice1, out_Voice2, out_Vibration, out_Atomizer

	'''
	if in_Phone and in_distFace1 and in_distFace2:
		out_Hazards=1
		out_Voice2=1 
	'''
	if in_distFace1:
		out_Voice1=1
	'''
	if in_distFace2:
		out_Hazards=1
		out_Voice1=1 
	'''
	if in_Lane:
		out_Vibration=1
	if in_Voice:
		out_Atomizer=1
	if in_Voice and in_Lane: 
		out_Voice1=1
		out_Vibration=1
		out_Atomizer=1
	if in_Phone:
		out_Hazards=1
		out_Voice2=1
	'''
	if in_Phone and in_Lane and in_distFace1 and in_distFace2:
		out_Hazards=1
		out_Voice1=1
		out_Vibration=1
	'''
	'''
	if in_drwFace1:
		out_Atomizer=1
	if in_drwFace2:
		out_Vibration=1	
		out_Voice1=1
		out_Voice2=1
	'''
	if in_Voice and in_Lane:
		out_Vibration=1
		out_Voice1=1
		out_Voice2=1
		out_Hazards=1
	'''
	if in_drwFace2 and in_Lane:
		out_Vibration=1
		out_Voice1=1
		out_Voice2=1
		out_Hazards=1
	if in_drwFace1 and in_Lane:
		out_Vibration=1
		out_Voice1=1
		out_Voice2=1
	'''
	'''
	if in_Voice: and in_drwFace2:
		out_Vibration=1
		out_Voice1=1
		out_Voice2=1
	'''
	'''
	if in_Phone and in_drwFace1  and in_drwFace2 and in_Lane:
		out_Vibration=1
		out_Voice1=1
		out_Voice2=1
		out_Hazards=1
	'''
	'''
	if in_Voice: #and in_drwFace2:
		out_Vibration=1
		out_Voice1=1
		out_Voice2=1
	'''

def updateOutput():
	GPIO.output(Hazards_PIN, out_Hazards)
	GPIO.output(Vibration_PIN, out_Vibration)
	GPIO.output(Voice1_PIN, out_Voice1)
	GPIO.output(Voice2_PIN, out_Voice2)
	GPIO.output(Atomizer_PIN, out_Atomizer)
	


#ser.flushInput()
while True:
	'''
	in_Lane=1
	in_Voice=1
	in_distFace1=1
	in_Phone=1
	'''
	resetOutputs()
	updateInput()
	updateLogic()
	updateOutput()
	printStates()
	#in_distFace2=0
	#in_drwFace1=1
	#in_drwFace2=1
	#out_Voice1=1
	#out_Vibration=1
	
		
