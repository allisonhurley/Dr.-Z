import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
from tailf import tailf
GPIO.setup(7, GPIO.OUT)

for line in tailf("jasper.log"):
	
	def process_matches(matchtext):
		while True:
			line = (yield) 
			if matchtext in line:
				call(["aplay", okay.wav]) 
				GPIO.output(7,1)

	list_of_matches = ['ON NOW']	
	matches = [process_matches(string_match) for string_match in list_of_matches]

	for m in matches: 
		m.next()

	while True: 
		auditlog = tail( open(log_file_to_monitor) )
		for line in auditlog:
			for m in matches:
				m.send(line)
done
