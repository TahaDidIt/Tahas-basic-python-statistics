#MAKING FUNITONS
print("##########################")
print("")




#Basic funcition notation
def mult(a,b):
    """
    This function multiplies 2 input numbers
    """
    c = a * b
    return c

a = 5
b = 2
c = mult(a,b)
print("c is ", c)

#You can get help on a function by using "help([function name])"
""" Also note: the functions a,b,c defined in the function are different 
 to the global ones defined after, and local to the variable. If python does not find
 a variable defined locally within the function, it will look globally after.
 
 Also: if [a] were to be a string, times by 2 would write that string twice, not return an error"""





#Function with no "return" (It will return the Python "None" value if plugged into a variable)
def MJ():
    print("Micheal Jackson")

MJ()


def DoNothing():
    #(Python doesn't like an empty function body, so we use "pass" instead)
    pass

useless_variable = DoNothing()
print(useless_variable)





#A cooler function, which takes a list of album ratings
# and lists the rating (s) for every index (i)
def printstuff(stuff):
    for i,s in enumerate(stuff):
        print("Album ", i, " has a rating of: ", s)

album_ratings = [10.0, 8.5, 9.5]
printstuff(album_ratings)





#Function has an asterisk (*) in the input, which takes and combines multiple inputs into
# a single tuple
def artistnames(*names):
    for name in names:
        print(name)

artistnames("Micheal Jackson", "AC/DC", "Pink Ployd")


