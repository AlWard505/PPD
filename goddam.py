from time import sleep as sleep
stage = 0
score = 0
def text():
	check = 0 
	file = open("dialog.txt","r")
	while check != 1
		line = file.readline()
		if line.str() == (stage.str()+score.str()):
		check = 1
	check = 0
	while check != 1:
		line = file.readline()
		if line == "decision":
			check = 1
		elif: 
			print(line)
		sleep(0.7)
	
	file.close
def decision():
	global score
	global stage
	x = "q"
	check = 0
	file = open("decision.txt","r")
	while check != 1:
		line = file.readline()
		if file.readline == (stage.str()+score.str()):
			check = 1
	des1 = file.readline()
	des2 = file.readline()
	while x != "a" or x != b":
		x = input("a) this choice\nb) this choice\n")
		x = x.lower()
	if a == "a":
		score += 1
	elif:
		score += -1
	stage += 1
	file.close
def game():
	text()
	decision()
