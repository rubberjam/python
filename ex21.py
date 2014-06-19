def add(a, b):
	print ("ADDING %d + %d" % (a, b))
	return a + b
	
def subtract(a, b):
	print ("SUBTRACTING %d - %d" % (a, b))
	return a - b
	
def multiply(a, b):
	print ("MULTIPLYING %d * %d" % (a, b))
	return a * b
	
def divide(a, b):
	print ("DIVIDING %d / %d" % (a, b))
	return a / b
	

print ("Let's do some maths with just functions!")

age = add(30, 7)
height = subtract(78, 4)
weight = multiply(45, 2)
iq = divide(100, 2)

print ("Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq))

# A puzzle for extra credit.
print ("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print ("What is: add(age, subtract(height, multiply(weight, divide(iq, 2))))?")
print ("That becomes: ", what, "Can you do that in your head?")
