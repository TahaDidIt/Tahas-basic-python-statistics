# -*- coding: utf-8 -*-
##### API BASICS - NBA api and Watson language translator worked example
""" Note: Next course video also did an IBM language translator example. I have skipped
    this due to it needing an API key, which will take time to acquire and
    I currently need to get moving through the material quicker. Just know
    that there is a second example for future reference."""



#!pip install nba_api     if not installed already
from nba_api.stats.static import teams
import pandas as pd
#For the gamefinder example section
from nba_api.stats.endpoints import leaguegamefinder

print("###############################")
print("")



#### NBA EXAMPLE


#Communicate with NBA web service via API's methods (Just like a class or object)
nba_teams = teams.get_teams()
print(nba_teams[:4])

#Let's convert those individual dictionaries that get output
# into 1 dictionary/table

def one_dict(list_dict):
    #Take a list of the "keys" or variable names out of one of the dictionaries
    keys = list_dict[0].keys()
    #Prepare a new dictionary with each of the keys being a (currently) empty list
    output_dict = {key:[] for key in keys}
    #Going through each team's dictionary one at a time,
    # it adds each value to the respective key, populating the empty lists
    for dict_ in list_dict:
        for key, value in dict_.items():
            output_dict[key].append(value)
    
    return output_dict

""" Notes on the function above:
    .keys() is a built-in method that grabs all the keys
    .items() is also a built-in method, it grabs key-value pairs from dictionaries
"""

#Call function on the nba_teams dictionaries we called earlier
dict_nba_teams = one_dict(nba_teams)
#Convert into a table (a dataframe)
df_teams = pd.DataFrame(dict_nba_teams)
#Display a brief view of the table
df_teams.head()



#### SELECT OR FIND AN ENTRY
print("")

#Let's say you want to find the Warriors' entry
df_warriors = df_teams[df_teams["nickname"] == "Warriors"]
print("Warriors info: ", df_warriors)
#Get one element
id_warriors = df_warriors[["id"]].values[0][0]

""" Note about the line selecting one element:
    "df_warriors[["id"]].values" does the actual selecting of data.
    Because it produces a 2D NumPy array, the [0][0] is just for selecting
    the first (and only) row and first (and only) element of that row.
    
    Double square brackets "[[ ]]" are Pandas convenient notation for accessing
    a column in a Pandas data frame object
"""



#### GAMEFINDER 
print("")

#bro what the hell are these methods and variables I was given them with no explanation
gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable = id_warriors)
games = gamefinder.get_data_frames()[0]
games.head()


