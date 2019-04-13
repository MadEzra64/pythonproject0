# Calling modules for use in our script
from sys import argv

# Using argv to obtain the file
script, filename = argv

# Declaring txt is our filename variable and opening it
txt = open(filename)

# Displaying the name of the opened file.
print(f"Here's your file {filename}: ")
# Reading and printing the text from the file
print(txt.read())
txt.close()

# Asking for input
print("Type the filename again: ")
# Taking input for the filename again aqain and calling it variable file_again
file_again = input("> ")

# Opening the file
txt_again = open(file_again)

# Displaying the file :)
print(txt_again.read())
txt_again.close()
