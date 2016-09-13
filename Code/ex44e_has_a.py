class OTHER(object):
	
	def override(self):
		print "Other override()"

	def implicit(self):
		print "Other implicit()"

	def altered(self):
		print "Other altered()"

class Child(object):

	def __init__(self):
		self.change = OTHER()
	
	def implicit(self):
		self.change.implicit()

	def override(self):
		print "Child override()"

	def altered(self):
		print "Child before other altered()"
		self.change.altered()
		print "Child, after other altered()"

son = Child()

son.implicit()
son.override()
son.altered()
