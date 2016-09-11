#ex33
def whileTest(limit):
	i = 0
	numbers =[]

	while i < limit:
		print "At the top i is %d" %i
		numbers.append(i)

		i=i+1
		print "Numbers now: ", numbers
		print "At the bottom i is %d" %i

	print "The numbers: "

	for num in numbers:
		print num

a = raw_input("Input a positive number:")
whileTest(int(a))
