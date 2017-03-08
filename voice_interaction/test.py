from subprocess import call

input = raw_input("Bench test: ")

call(["aplay",input])

