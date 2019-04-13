# Calling module argv
from sys import argv

# Taking a filename
script, filename = argv

# Explaining in text what's about to happen
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Waiting for input
input("?")

# Open the file with the value 'w' for writing and truncating
print("Opening the file...")
target = open(filename, 'w')

# Truncate the file (emptying it)
print("Truncating the file. Goodbye!")
target.truncate()

# Requesting input
print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

# Taking that input and writing it to the file we have open in python
print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# Keeping things neat by closing the file.
print("And finally, we close it.")
target.close()

print("Next we are going to read the file!")
txt = open(filename)

print(f"{filename} is now open. Press enter to continue...")
input()

# Displaying the new file.
print(txt.read())
print("Press any key to end program and close file...")
input()
txt.close()
