mport RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

from subprocess import call

while True:
	if (GPIO.input(11) ==0 and GPIO.input(13) ==0):
		print("Everything is off")
		time.sleep(5)
	if (GPIO.input(11) == 0 and GPIO.input(13) ==1):
		print("Driver is on their phone")
		call(["aplay",phone.wav])
		time.sleep(5)
	if (GPIO.input(11) ==1 and GPIO.input(13) ==0):
		print("Driver is out of their lane")
		call(["aplay", stay.wav])
		time.sleep(5)
	if (GPIO.input(11)==1 and GPIO.input(13) ==1):
		print("Driver is shleepin")
		call(["aplay", wakeup.wav])
		time.sleep(5)

