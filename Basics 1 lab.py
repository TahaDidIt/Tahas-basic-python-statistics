print("Hello Python!!") # This prints a string

#Check python version
import sys
print(sys.version)

x = 12
print(type(x)) #tells you the type of value x is
print(type(12.0))

print(int(1.2)) # converts 1.2 to an integer (truncates decimals)
print(str(1.2)) # converts to string

print(bool(1)) # converts 1 to a boolean (Always "True")
print(bool(0)) # converts 0 to a boolean (Always "False")


x = 43 + 60 + 16 + 41
print(x)

name = "Micheal Jackson"
print(name[0]) # index to retrieve first element (or character)
print(name[1])
print(name[-1]) # index backwards (from last to first) (gives last character)

print(name[::2]) #returns every other character
print(name[0:5:2]) #returns every other character between elements 0 and 5
print(len(name))

#Concatenation
statement = name + " is the best"
print(statement)
#Tuples
threetimes = 3 * name
print(threetimes)


# Backslash indicates the start of an esacpe sequence
#\n indicates a new line
print("Micheal \nJackson")
#\t represents a tab
print("Micheal\tJackson")
#if you actually want a backslash in your string use double backslashes
print("Micheal \\ Jackson")
#or put an e infront of the string
print(r"Micheal \ Jackson")



#string methods
A = "Micheal Jackson"
B = A.upper()
print(B)

C = A.replace("Micheal", "Michelle")
print(C)

#[].find("") outputs the first index in the string you asked to search for
#if nothing is found it returns -1
print(name.find("ic"))

y = 1/1
print(y)
print(type(y))


