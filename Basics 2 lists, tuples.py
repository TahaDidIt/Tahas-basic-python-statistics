#lists, tuples


#Creating a list
list1 = ["Fernando Alonso", 10.1, 1982]
#retrieving elements
print(list1[0])
print(list1[-1])

print(type(list1))
print(type(list1[1]))

#Nesting lists
list2 = ["Fernando Alonso", 10.1, 1982, [1, 2], ("A", 1)]
#retrieve elements (same thing)
print(list2[3])
print(list2[4])
#retrieving individual nested elements
print(list2[3][0])
print(list2[4][0])
#list slicing NOTE: first number is inclusive, second number is exclusive (note that element 4 not included)
print(list2[2:4])

#Unlike tuples which are immuatable, lists can be changed

#delete element
print("######")
print("list2 before: ", list2)
del(list2[0])
print("list2 after: ", list2)
#extend 
print("######")
print("list2 before: ", list2)
list2.extend(["a", "b"])
print("list2 after: ", list2)
#append (add just one element, good for nests)
print("######")
print("list2 before: ", list2)
list2.append(["c", "d"])
print("list2 after: ", list2)
#change element based on index
print("######")
print("list2 before: ", list2)
list2[0] = "Max Verstappen"
print("list2 after: ", list2)

#copying lists
A = ["hard rock", 10, 1.2]
print("######")
print("list A is ", A)
#this method links the new list to the orignal, so when one changes, the other does too
B = A
#this method clones the original list into a new, unlinked list
C = A[:]
#Test for proof:
del(A[0])
print("New A: ", A)
print("B: ", B)
print("C: ", C)




