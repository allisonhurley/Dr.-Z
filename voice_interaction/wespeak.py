from subprocess import call
import RPi.GPIO as GPIO
import time
import re
GPIO.setmode(GPIO.BOARD)
from tailf import tailf
GPIO.setup(7, GPIO.OUT)

def process_match(cmd):
	if cmd == "ON NOW":
		call(["aplay", "-D", "hw:CARD=ALSA,DEV=0", "okay.wav"])
		GPIO.output(7,1)
		print line	
	elif cmd == "JASPER":
		print "Hi Allison"

rex = re.compile("INFO:client.stt:Transcribed: \\['(.*)'\\]")

for line in tailf("/home/pi/jasper.log"):

 	match = rex.search(line)
	if match:
		process_match(match.group(1))

