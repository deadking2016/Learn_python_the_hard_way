#ex 31
print "You enter a dark room with two doors. Which to go? 1 or 2"

door = raw_input(">")

if door == "1":
	print "There is a giant bear with a cake. What do you do?"
	print "1. Take the cake"
	print "2. Scream at the bear"

	bear = raw_input(">")

	if bear == "1":
		print "The bear eats your face off"
	elif bear == "2":
		print "The bear eats your leg off"
	else:
		print "Doing %s is better,bear run away" %bear

elif door == "2":
	print "You stare into the abyss"
	print "1. Blueberries"
	print "2. Yellow jacket"
	print "3. Understanding"

	insanity = raw_input(">")

	if insanity == '1' or insanity == '2':
		print "Your body survive"
	else:
		print "You are insane"

else:
	print "You die"
