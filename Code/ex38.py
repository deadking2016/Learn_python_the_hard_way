ten_things = "Apples Oranges Crosws Telephone Light Sugar"

print "Wait there's not 10 things in that list"

stuff =  ten_things.split(" ")
more_stuff = ["Day", "Night" , "Song", "Frisbee", "Corn", "Banana","Girl","Boy"]

while len(stuff)!=10:
	next_one = more_stuff.pop()
	print "Adding:", next_one
	stuff.append(next_one)
	print "There is %d items now" %len(stuff)

print "There we go", stuff

print "Let's do something with stuff"

print stuff[1]
print stuff[-1]
print stuff.pop()
print " ".join(stuff)
print "#".join(stuff[3:5])
