#Reading, writing files and data from panda
print("##################################")
print("")



##### READING



#We can open files into a file object and then use the object's methods to interact
File1 = open("C:/Taha/projects/Data Science Fundamentals with Python and SQL/Working directory/reading from files.txt", "r")

print("File name and location is: ", File1.name)
print("File mode: ", File1.mode)
File1.close()
print("Is File1 closed?: ", File1.closed)


#You should close files.
#Instead of doing that each time, we can use "with" statement to close it automatically
# and read the contents into a seperate variable to use outside of the "with"

with open("C:/Taha/projects/Data Science Fundamentals with Python and SQL/Working directory/reading from files.txt", "r") as File2:
    file_stuff = File2.read()

print("Is File2 closed?: ", File2.closed)
print(file_stuff)

#Say we want python to read the lines seperately
#As a list:
with open("C:/Taha/projects/Data Science Fundamentals with Python and SQL/Working directory/reading from files.txt", "r") as File2:
    file_stuff2 = File2.readlines()
    #Or just "readline()" (singular) for specific num of characters

print("Is File2 closed?: ", File2.closed)
print(file_stuff2)
#Note: idk why this doesn't split it into seperate elements and just adds a backslash before the \n



#### WRITING

with open("C:/Taha/projects/Data Science Fundamentals with Python and SQL/Working directory/writing to files.txt", "w") as File3:
    File3.write("This is line A\n")
    File3.write("This is line B\n")

#Or to put a list into a file
lines = ["This is line A\n", "This is line B\n", "This is line C\n"]
with open("C:/Taha/projects/Data Science Fundamentals with Python and SQL/Working directory/writing to files.txt", "w") as File4:
    for line in lines:
        File4.write(line)



#### APPEND



with open("C:/Taha/projects/Data Science Fundamentals with Python and SQL/Working directory/writing to files.txt", "a") as File5:
    File5.write("This is line D")


