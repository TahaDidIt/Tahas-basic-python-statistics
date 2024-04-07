
#DICTIONARIES
#Dictionaries are like lists but declared with {} and the index can be characters (Called "keys")
D1 = {"Thriller": 1982, "Back in Black": 1980, "The Dark Side of the Moon": 1973, "The Bodyguard": 1992}

print(D1)
print("Thriller was from: ", D1["Thriller"])

#Add a value
D1["Graduation"] = 2007
print(D1)

#Delete a value
del(D1["Thriller"])
print(D1)

#Verify if an entry exists
print("")
print("The Bodyguard" in D1)
print("Starboy" in D1)

#See all keys or values
print("")
print(D1.keys())
print(D1.values())


################
#SETS
#Unlike lists and tuples, they are unordered, and they contain only unique items (no duplicates)
#sets done have an index, just unique items
#if you add a duplicate nothing changes

print("")
print("######")
print("SETS")
print("")
set1 = {"AC/DC", "Back in Black", "Thriller"}
print(set1)

#Add an element
set1.add("NSYNC")
print(set1)
#remove element
set1.remove("NSYNC")
print(set1)
#Verify an element
print("AC/DC" in set1)

set2 = {"AC/DC", "Back in Black", "The Dark Side of the Moon"}

#Intersection of set 1 and 2
set3 = set1 & set2
print(set3)

#Union of set 1 and 2
set4 = set1.union(set2)
print(set4)

#verify if one set is a subset of the others
print(set3.issubset(set2))

