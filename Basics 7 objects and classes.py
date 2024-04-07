#OBJECTS and CLASSES

""""
INTRO: Variables and objects all have a type (i.e. list, string, dictionary).
An object is an instance of a particular "type"
Every object has an internal data attributes or "blueprint", and a set of methods that are used to interact with it
You can create elaborate types by making "classes", and using the built in methods to modify instances of them or make them do things
"""

#Defining a class
class circle(object):

    #__init__ constructor is used to initialise the data attributes
    def __init__(self, radius, colour):
        self.radius = radius;
        self.colour = colour;

    #Define methods to interact with the objects
    def add_radius(self, r):
        #Increases the radius by input number, r
        self.radius = self.radius + r

#Creating an object
circle1 = circle(3, "red")
print("circle1 radius is ", circle1.radius)
print("circle1 colour is ", circle1.colour)
circle1.add_radius(3)
print("now circle1 has radius ", circle1.radius)



#dir() is useful for obtaining a list of all the attributes and methods in a class
print(dir(circle1))



