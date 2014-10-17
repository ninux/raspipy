# tell what libraries to load
import fileinput

# define a function to print prersonalized welcome message
def hello(s):
    print("Welcome " + str(s))

#define a function to ask for your name
def askName():
    hello(input("What's your name?\n> "))

# the main program
askName()
