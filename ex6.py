x = ("There are %d types of people." % 10)# string inside
binary = ("binary")
do_not = ("don't")
y = ("Those who know %s and those %s." % (binary, do_not)) # string inside

print (x) # prints x with 10 inside - binary for 2
print (y) # prints y with binary and do_not inside

print ("I said: %r." % x) # string inside / prints x as above but with single quotes
print ("I also said: '%s'." % y) # string inside / prints y as above

hilarious = False
joke_evaluation = ("Isn't that joke so funny?! %r")# fifth string inside - 

print (joke_evaluation % hilarious) # finds the % inside 'joke_evaluation' and places 'hilarious' inside

w = ("This is the left side of...")
e = ("a string with a right side.")

print (w + e) #self explanatory
