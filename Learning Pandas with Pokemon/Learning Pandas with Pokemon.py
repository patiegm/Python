import pandas as pd #importing pandas for dataframe manipulation
#https://pandas.pydata.org/pandas-docs/stable/10min.html
#API Documentation https://pandas.pydata.org/pandas-docs/stable/index.html
#pandas is a Python package providing fast, flexible, and expressive data structures designed 
#to make working with “relational” or “labeled” data both easy and intuitive. 
#It aims to be the fundamental high-level building block for doing practical, 
#real world data analysis in Python. 
#import numpy as np #importing numpy for number analysis
import matplotlib.pyplot as plt #importing matplotlib.pyplot for visualisations
#import seaborn as sns
plt.style.use('fivethirtyeight')


##
##Data Science Process
##Step 1 - Prepare the Data
##Source, clean & prepare the data for analysis. Check for completeness, resolve anomolies and perform QA
##

##Getting our data, and performing some basic operations to familiarise outselves with the dataset

#read file and save to a pandas dataframe, a two-dimensional, size-mutatable, potentially heterogeneous data structure 
df = pd.read_csv("C:/Users/jammy/OneDrive/Documents/Developments/Python/Pokemon/Pokemon.csv")

#df.head(n) returns a DataFrame holding the first n rows of df.
df.head(n=5)

#df.tail returns a DataFrame holding the bottom n rows of df.
df.tail(n=5)

#Show the columns contained within the dataframe
df.columns

#Show the shape of the dataframe
df.shape

#change column names into upper case and remove white space
df.columns = df.columns.str.upper().str.replace(' ', '') 

#Show the data type for each column in the dataframe
df.dtypes

#Show the index of the dataframe
df.index

 #set the index to the named attribute in the dataframe
df = df.set_index('NAME')

#Show the index, which will now be NAME
df.index

#sort values by the index, and append .head() to return only our head records
df.sort_index().head()

#Show 5 Pokemon with lowest Attack Stat. Sort values by Attack attribute, default is ascending
df.sort_values(by='ATTACK').head(n=5)

#Show 5 Pokemon with highest Attack Stat. Sort values by Attack attribute, default is ascending
df.sort_values(by='ATTACK').tail(n=5)

#Sort values by TYPE2 attribute, this time we want descending, and show the NaN last
df.sort_values(by='TYPE2', ascending=False, na_position='last')

#Select a single column to return a Series
df['TYPE1'].head(n=5)

#Slice rows starting at row 10 up to row 15
df[10:15]

#retrieves all data for index label Bulbasaur
df.loc['Bulbasaur'] 

#Same return, but using index position key value
df.iloc[0] 

#Selecting on a multi-axis using label and attribute name
df.loc['Bulbasaur':'Venusaur',['TYPE1','TYPE2']]

#Alternatively, Selecting on a multi-axis using integers
df.iloc[0:3,1:3]

#Showing how to return all attributes for a multi-axis subset
df.iloc[0:3,:]

##
##Cleaning the Data
##

#Before we maniuplate, it might be prudent to create a copy of our data so we can return to it if needed
df2 = df.copy()

#drop the columns with axis=1;axis=0 is for rows
df2=df.drop(['#'],axis=1) 

#Showing that # Column is now dropped
df2.head(n=5)         

#pandas primarily uses the np.nan to represent missing data. It is by default not included in computations

#Get the boolean mask where values are nan            
pd.isna(df2)
             
#Again, take a copy. This time genuinley we will revert as the next step is just a demonstration
df3 = df2.copy()

#Drop any rows containing NaN values
df3.dropna(how='any')    
pd.isna(df3)
             
#We will replace NaN values in TYPE2 attribute with that present in TYPE1
df2['TYPE2'].fillna(df['TYPE1'], inplace=True) 

# The new index of Names contains erroneous text. We want to remove all the text before "Mega"
df2.index = df.index.str.replace(".*(?=Mega)", "")

df2.head(10)

##
##Data Science Process
##Step 2 - Data Exploration
##Build models, perform data mining, run text analysis and much more!
##

#Return data by filtering on a columns integer value   
df2[df.HP > 150]

#Give us a distinct list of TYPE1 values
df2['TYPE1'].unique()

#Show us the results where we've filtered for a specific value in an attribute
df2[df2['TYPE1']=='Dragon'].head(5) 

#Return data by filtering on multiple columns
df2[((df2['TYPE1']=='Fire')  & (df2['TYPE2']=='Dragon'))]

#Alternatively via boolean indexing we can use isin() method to filter 
df2[df2['TYPE1'].isin(['Dragon'])].head(n=5)

#Return index value with highest value
df2['DEFENSE'].idxmax()

#Return index value with lowest value
df2['ATTACK'].idxmin()

#Take a look at some of the averages of each attribute
df2.mean(axis=0)

#Show a brief statistical summary of the data frame
df2.describe()

#Get mean value of a specific column
df2['HP'].mean()
df2['ATTACK'].mean()
df2['DEFENSE'].mean()

#Histogramming, getting the counts of values in our data
df2['TYPE1'].value_counts()
df2['TYPE2'].value_counts()


##
##Data Science Process
##Step 3 - Visualise the Data
##Translate complex insights into easy-to-digest visuals
##

plt.scatter(df2['ATTACK'], df2['DEFENSE'])

data = (g1, g2, g3)

colors = ("red", "green", "blue")

groups = ("coffee", "tea", "water") 

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, axisbg="1.0")
 
for data, color, group in zip(data, colors, groups):
    x, y = data
    ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none', s=30, label=group)
 
plt.title('Matplot scatter plot')
plt.legend(loc=2)
plt.show()






num = 1000
ax.scatter(x1, y1, color='r', s=2*s, marker='^', alpha=.4)
ax.scatter(x2, y2, color='b', s=s/2, alpha=.4)
ax.scatter(x3, y3, color='g', s=s/3, marker='s', alpha=.4)

bins=range(0,200,20) #they act as containers
plt.hist(df2["ATTACK"],bins,histtype="bar",rwidth=1.2,color='#0ff0ff') #hist() is used to plot a histogram
plt.xlabel('Attack') #set the xlabel name
plt.ylabel('Count') #set the ylabel name
plt.plot()
plt.axvline(df2['ATTACK'].mean(),linestyle='dashed',color='red') #draw a vertical line showing the average Attack value
plt.axvline(df2['ATTACK'].median(),linestyle='dashed',color='green') #draw a vertical line showing the average Attack value

plt.show()
