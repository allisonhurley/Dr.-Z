import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

from subprocess import call

status = 0
while True:
	new_status = 0
	if (GPIO.input(11) == 1):
		new_status = 1

	if (GPIO.input(13) == 1):
		new_status = new_status + 2

	if new_status != status:
		status = new_status
	
		if status == 0:
			print("Everything is off")

		if status == 2:
			print("Driver is on their phone")
			call(["aplay", "-D", "hw:CARD=ALSA,DEV=0", "phone.wav"])

		if status == 1:
			print("Driver is out of their lane")
			call(["aplay", "-D", "hw:CARD=ALSA,DEV=0", "stay.wav"])

		if status == 3:
			print("Driver is sleeping")
			call(["aplay", "-D", "hw:CARD=ALSA,DEV=0", "wakeup.wav"])

	time.sleep(1)

