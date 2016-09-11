from sys import exit

def gold_room():
	print "This room is full of gold. How much do you take?"

	next = raw_input(">")
	if "0" in next or "1" in next:
		how_much = int(next)

	else:
		dead("Man learn to type a number")

	if how_much < 50:
		print "Nice ,you're not greedy"
		exit(0)
	else:
		dead("You greedy bustard")

def bear_room():
	print "There is a bear here"
	print "The bear has a bunch of honey"
	print "The fat bear is in front of another door"
	print "How are you going to move the bear"
	bear_moved = False

	while True:
		next = raw_input(">")

		if next == "take honey":
			dead("The bear slap your face off")
		elif next == "taunt bear" and not bear_moved:
			print "You can go now"
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear chews your leg off")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I don't understand"

def cthulhu_room():
	print "Here you see the evil Cthulhu"
	print "He, it , whatever stares at you and you go insane"
	print "Do you flee or eat your head"

	next = raw_input(">")

	if "flee" in next:
		start()
	elif "head" in next:
		dead("That's tasty")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good Job"
	exit(0)

def start():
	print "You are in a dark room"
	print "There is a door to you right and left"
	print "Which one do you take"

	next = raw_input(">")

	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_room()
	else:
		dead("You starve")

start()
