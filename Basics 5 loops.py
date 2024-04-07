###### Range function
# range(N) or range(0, N) outputs sequence [ 0, ..., N-1]



###### FOR LOOPS
colours = ["red", "yellow", "green", "purple", "blue"]
print(colours)
print("")

for i in range(0,5):
    colours[i] = "white"
print(colours)

#For loops with enumerate function
for i, colour in enumerate(colours):
    print(colour)
    print(i)



###### WHILE LOOPS
colours[4] = "red"
newcolours = []

i = 0
while(colours[i] == "white"):
    newcolours.append(colours[i])
    colours[i] = "red"
    i = i + 1
print(colours)
print(newcolours)

