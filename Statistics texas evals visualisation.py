# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 12:10:56 2024

@author: Taha
"""
##### SET-UP
from datetime import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy.stats import norm


#Loading texas evals dataset into pandas dataframe
csvPathEvals = "C:/Taha/projects/Data Science Fundamentals with Python and SQL/Working directory/evals.csv"
sourceData = pd.read_csv(csvPathEvals)
#.describe() for a basic summary of the dataset variables
print(sourceData[["rank", "ethnicity", "gender"]].describe())
print("")


#Loading Boston dataset into pandas dataframe
csvPathBoston = "C:/Taha/projects/Data Science Fundamentals with Python and SQL/Working directory/boston.csv"
bostonData = pd.read_csv(csvPathBoston)
print(bostonData.describe())




##### VISUALISATIONS

### Bar chart: counts, male and female
def barChart1():
    ax = sns.countplot(x = "gender", hue = "rank", data = sourceData)
    ax.set_title("Courses taught by gender")
    plt.show()


### SCATTER PLOT: age by eval, "row" for whether tenured or not, colour for gender
def scatter1():
    g = sns.FacetGrid(sourceData, row = "rank", hue = "gender")
    g.map(plt.scatter, "age", "score").add_legend()
    g.map(plt.grid, linestyle = "--", color = "gray")
    plt.savefig("scatter1output.png", dpi = 300)
    plt.show()


### BOX PLOT: age by gender
def boxPlot1():
    ax = sns.boxplot(x = "age", y = "rank", hue = "gender", data = sourceData)
    ax.grid(axis = "x", linestyle = "--")
    plt.show()


#### PIE CHART: female vs male sample size
def pieChart1():
    #Currently "sourceData" is a list of course_id, so professors are repeated
    #get list of unique professors
    profData = sourceData[["prof_id", "gender"]].drop_duplicates(subset = "prof_id")
    #get count-up of each gender
    sizes = [profData["gender"].value_counts()[1], profData["gender"].value_counts()[0]]
    
    #pie chart
    labels = ["females", "males"]
    fig1, ax = plt.subplots()
    ax.pie(sizes, labels = labels, autopct = "%1.1f%%")
    plt.show()


### NORMAL DISTRIBUTION: Draw a normal distribution graph
def norm1():
    x_axis = np.arange(-4, 4, 0.1)
    plt.plot(x_axis, norm.pdf(x_axis, 0, 1))
    plt.show()


### T-TEST: Test acerage score of genders (gives t-stat and p-value)
def tTest1():
    #get mean score of each gender via pandas groupby, purely for visualisation purposes
    genderMean = sourceData.groupby("gender")["score"].mean().reset_index()
    ax = sns.barplot(x = "gender", y = "score", data = genderMean)
    ax.set_title("Average evaluation score by gender")
    plt.show()
    print(genderMean)
    
    #"ttest_ind" to run t-test on whether the difference between means is significant
    #Note the assumption of equal variance can be set to false, but is true by default
    print("")
    print(scipy.stats.ttest_ind(sourceData[sourceData["gender"] == "female"]["score"],
                          sourceData[sourceData["gender"] == "male"]["score"],
                          equal_var = True))


### P-VALUE: Standardising data to a normal distribution and getting P-value of score
def pVal1():
    print("Testing likelihood of getting a score atleast as extreme as input")
    evalTest = float(input("Please input a score to test: "))
    print("")
    
    #find evaluations' mean and standard deviation, rounded to 3 d.p
    evalMean = round(sourceData["score"].mean(), 3)
    evalStd = round(sourceData["score"].std(), 3)
    print("Average evaluation score: ", evalMean)
    print("Standard deviation of evaluations: ", evalStd)
    
    #The code below effectively standardises or calculates the z-score
    #and then runs the scipy norm cdf function on it and subtracts it from 1
    #P-value is probability of getting a score atleast as extreme as input number
    #so P-value is 1 minus the probability of getting any score LESS than input number
    evalPValue = 1 - scipy.stats.norm.cdf((evalTest - evalMean)/evalStd)
    print("P-Value: ", evalPValue)


### LEVENE'S TEST: Test if the 2 comparison groups have equal/ unequal variances
#(Will impact test chosen/ whether t-test is done with "equal_var" set to true or false)
#ALSO INCLUDES bar and box plot comparisons of score and beauty for different age groups
def levene1():
    print(scipy.stats.levene(sourceData[sourceData["gender"] == "female"]["score"],
                             sourceData[sourceData["gender"] == "male"]["score"],
                             center = "mean"))


### ANOVA for using f-stat on score and beauty, by age group
def anova1():
    """
    NOTE: No standardisation of dataset implemented, unlike in course followed
    Could also do some visualisations- bar chart age groups vs beaty, eval
    """
    #get professors data without repeats
    profData = sourceData.drop_duplicates(subset = "prof_id")
    #create age groups in the dataframe, using .loc[(search label or criteria), (a label to change)]
    profData.loc[(profData["age"] < 40), "age_group"] = "young"
    profData.loc[(profData["age"] >= 40) & (profData["age"] < 60), "age_group"] = "middle"
    profData.loc[(profData["age"] >= 60), "age_group"] = "old"
    
    #can also split them up into seperate dataframes; whichever is easier for application
    profYoung = profData.loc[profData["age_group"] == "young"]
    profMiddle = profData.loc[profData["age_group"] == "middle"]
    profOld = profData.loc[profData["age_group"] == "old"]
    
    #eval score f-statistic anova using scipy.stats
    fStat1, pValue1 = scipy.stats.f_oneway(profYoung["score"], profMiddle["score"],
                                         profOld["score"])
    fStat2, pValue2 = scipy.stats.f_oneway(profYoung["bty_avg"], profMiddle["bty_avg"],
                                         profOld["bty_avg"])
    #print in a formatted fashion using a fancy method"
    print("Evaluation score:")
    print("F Statistic: {0},   P-value: {1}".format(fStat1, pValue1))
    print("Beauty score:")
    print("F Statistic: {0},   P-value: {1}".format(fStat2, pValue2))
    
    #Visualisations
    #create figure with 1 row, 2 columns
    fig, ax = plt.subplots(1, 2)
    #Bar: avg eval of age groups
    sns.barplot(x = "age_group", y = "score", data = profData, ax = ax[0],
                estimator = "mean", ci = None)
    ax[0].set_title("Average score of age groups")
    #Bar: avg beaty of age groups
    sns.barplot(x = "age_group", y = "bty_avg", data = profData, ax = ax[1],
                estimator = "mean", ci = None)
    ax[1].set_title("Average beauty of age groups")
    
    #add some horizontal space between the 2 plots and display them
    plt.subplots_adjust(wspace = 0.5)
    plt.show()
    
    #create figure with 2 rows, 1 column
    fig, ax = plt.subplots(2, 1)
    #Box: eval spread for age groups
    sns.boxplot(x = "score", y = "age_group", ax = ax[0], data = profData)
    ax[0].set_title("Spread of evaluation scores")
    #Box: beauty spread for age groups
    sns.boxplot(x = "bty_avg", y = "age_group", ax = ax[1], data = profData)
    ax[1].set_title("Spread of beauty scores")
    
    #add some vertical space between them and display
    plt.subplots_adjust(hspace = 1)
    plt.show()


### CHI-SQUARED test: for association between categorical variables
# Gender and Tenure status
def chiSquare1():
    #Lets get professor data
    profData2 = sourceData.drop_duplicates(subset = "prof_id")
    #I named profData "2" instead, as we're going to group the tenure statuses together
    #for simplicity
    profData2["rank"] = profData2["rank"].replace({"tenure track": "tenured or on track"})
    profData2["rank"] = profData2["rank"].replace({"tenured": "tenured or on track"})
    #The chi2_contingency function requires data in the form of a contingency table
    #Essentially a countup of quantities in each group or a "cross tabulation"
    contingencyTable = pd.crosstab(profData2["rank"], profData2["gender"])
    print(contingencyTable)
    
    print("")
    print(scipy.stats.chi2_contingency(contingencyTable, correction = False))


### PEARSON R CORRELATION: association between continuous variables
# eval score and average beauty score
def pearsonR():
    """NOTE: we do NOT want profData (dropping duplicate prof_id) as each COURSE
    has its own evaluation of the professors score and beauty"""
    #First lets see it visually
    plt.scatter("bty_avg", "score", data = sourceData)
    plt.show()
    #Pearson R function
    rValue, pValue = scipy.stats.pearsonr(sourceData["bty_avg"], sourceData["score"])
    print("R coefficient: {0}, P-Value: {1}".format(rValue, pValue))


### REGRESSION BASIC (T-test)
def reg1TTest():
    """ NOTE: We use sourceData not profData as each course has its own evaluation.
        You can ALSO use this same code for 2 continuous variables in place of
        a correlation (Pearson-R) test.
    """
    #create X variable of gender in regression (1 if female, 0 if male)
    X = (sourceData["gender"] == "female").astype(int)
    #y (dependant variable) is the list of evaluation scores
    y = sourceData["score"]
    
    #Add intercept property
    X = sm.add_constant(X)
    #Creating and fitting model
    model = sm.OLS(y, X).fit()
    predictions = model.predict(X)
    
    print(model.summary())
    print("")
    print(predictions)


### REGRESSION ANOVA (More than 2 groups)
def reg2Anova():
    #get age groups
    sourceData.loc[(sourceData["age"] < 40), "age_group"] = "young"
    sourceData.loc[(sourceData["age"] >= 40) & (sourceData["age"] < 60), "age_group"] = "middle"
    sourceData.loc[(sourceData["age"] >= 60), "age_group"] = "old"
    #Feels like I should do it to profdata, as each course doesnt have its own bty avg
    
    #Fit model
    lm = ols("bty_avg ~ age_group", data = sourceData).fit()
    table = sm.stats.anova_lm(lm)
    print(table)
    
    #Dummy variable method
    X = pd.get_dummies(sourceData[["age_group"]])
    """ Same thing follows as done in reg1() """





##### MAIN MENU

### Visualisations index
plotFunctions = {1: barChart1, 2: scatter1, 3: boxPlot1, 4:pieChart1, 5:norm1, 6:tTest1,
                 7: pVal1, 8: levene1, 9: anova1, 10: chiSquare1, 11: pearsonR,
                 12: reg1TTest, 13: reg2Anova}


### Menu
menuChoice = ""

while menuChoice != "0":
    #Time and spacer for ease of reading
    print("")
    print("")
    print("")
    print("########## ", "Current Time: ", datetime.now().strftime("%H:%M:%S"))
    print("")
    #Menu choices
    print("Main Menu:")
    for i in plotFunctions:
        print(i, ": ", plotFunctions[i])
    
    menuChoice = input("Please select a number from the options: ")
    if menuChoice == "0":
        pass
    elif int(menuChoice) in plotFunctions:
        print("")
        plotFunctions[int(menuChoice)]()
    else:
        print("Invalid choice, please try again.")
    






