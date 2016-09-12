#Animal is a object look at the extra credit
class Animal(object):
	print "New animal"

## is a
class Dog(Animal):
	def __init__(self,name):
		#has a
		self.name=name
	print "New dog"

# is a
class Cat(Animal):
	def __init__(self,name):
		#has a
		self.name=name
	print "New cat"

# is a
class Person(object):
	def __init__(self,name):
		#has a
		self.name=name
		self.pet = None
	print "New person"

## is a 
class Employee(Person):
	def __init__(self,name,salary):
		## has
		super(Employee,self).__init__(name)
		## has
		self.salary=salary
	print "New employee"

## is a 
class Fish(object):
	pass

class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

rover = Dog("Rover")
rover = Dog("Did")
satan = Cat("Satan")
#mary = Person("Mary")
#mary.pet = satan
frank = Employee("Frank",12000)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()
