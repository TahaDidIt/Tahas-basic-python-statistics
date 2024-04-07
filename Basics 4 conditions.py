###### CONDITIONS AND BRANCHING

#a == 3, b!=4, i>5, j>=6  etc. return true or false


# if elif and else
age = 18

if age > 18:
    print("You can enter the AC/DC concert")
elif age == 18:
    print("You're not old enough, but you can go see Pink Floyd instead")
else:
    print("Go walk buddy")
print("Alright NEEXTTTT")


###### OPERATORS
print("######")
print("")

#NOT
bool1 = True
print(not(bool1))

album_year = 1990
if (album_year < 1980) or (album_year > 1989):
    print("The album wasn't made in the 80s ")
else:
    print("Album was made in the 80s")


#AND 
if (album_year > 1979) and (album_year < 1990):
    print("This album was made in the 80's")
else:
    print("This aint no damn 80s album boy")





