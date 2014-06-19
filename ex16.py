from sys import argv

script, filename = argv

print ("we're going to erase %r." % (filename))
print ("If you don't want to do that, hit Ctrl-C (^C).")
print ("If you do want to do that, hit RETURN")

input ('?')

print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line_1 = input("Line 1: ")
line_2 = input("Line 2: ")
line_3 = input("Line 3: ")

print ("I'm going to write these to the file.")

target.write(line_1)
target.write("\n")
target.write(line_2)
target.write("\n")
target.write(line_3)
target.write("\n")

print ("And finally, we close it.")
target.close()
