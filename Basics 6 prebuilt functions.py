#FUNCTIONS


#examples of built-in functions

album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5]

#Len
L1 = len(album_ratings)
print("L1 is ", L1)

#Sum
S1 = sum(album_ratings)
print("S1 is ", S1)

#Sorted (creates a new variable, original unchagned)
sorted_album_ratings = sorted(album_ratings)
print("Sorted album rating is ", sorted_album_ratings)

#sort() method (original list is changed)
album_ratings.sort()
print("album_ratings.sort() used. album_ratings is now: ", album_ratings)
