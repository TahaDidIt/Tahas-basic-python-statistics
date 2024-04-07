#Working with dataframes using Panda

#Note, I have currently not installed panda as it requires Anaconda service
#But for instructional purposes, the code should be okay

import pandas

#You can also say import pandas as [] to prevent having to type
#pandas over and over again later i.e pandas.read_csv() 





##### Reading data
"""
csv_path = "[a csv file path]"
#This is to save you from typing it over and over again

#Into a dataframe
df = pandas.read_csv(csv_path)
df.head() # Allows you to examine the first 5 rows of a data frame

#Read an excel file
xlsx_path = "[file path]"
df = pd.read_excel(xlsx_path)
# Vice Versa....
"""



#### MAKING a Dataframe

#Making a dictionary first
songs = {"Album": ["Thriller", "Back in Black", "The Dark Side of the Moon", "The Bodyguard", "Bat Out of Hell"], 
         "Released": [1982, 1980, 1973, 1992, 1977],
         "Length": ["00:42:19", "00:42:11", "00:42:49", "00:57:44", "00:46:33"]}

#Turn it into a dataframe with the pandas dataframe function
songs_frame = pandas.DataFrame(songs)

#Can also extract columns into a new dataframe
x = songs_frame[["Artist", "Length"]]

#How to all unique values for release years
unique_years = songs_frame["Released"].unique()
#The result is all of unique elements from just the released column




##### Let's say we want all rows in the dataframe where the year >= 1980

#Firstly, note that the code below gives a bunch of true and false values for the entries in the dataframe
songs_frame["Released"] >= 1980

#We can acchieve our goal in one single line in pandas.
new_dataframe = songs_frame[songs_frame["Released"] >= 1980]
#We now have a new datafram where all entries were released after 1979




#### WRITE dataframe to csv
new_dataframe.to_csv("new_songs.csv")
