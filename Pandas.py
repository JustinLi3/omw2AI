import pandas as pd 

#Pandas offers series and dataframes which, unlike lists, handle missing data, suitable for
#Pandas algorithms, Indexing, and alignment  

#Series (1D)
data1 = [1,4,3,5] 
series = pd.Series(data1) 
print(series) 

#DataFrame (2D dict) 
data2 = {'Colors': ["Blue","Green,","Red"], 
        'Frequency': [24,90,34],
        'Example': ["Sky", "Grass", "Fox"]}  
dataFrame = pd.DataFrame(data2)  
print(dataFrame)


#Data Cleaning & Preprocessing 
data3 = {'Name': ['John', 'Anna', 'Peter', 'Linda', None, None],
        'Age': [28, 24, None, 32, 45, None],
        'City': ['New York', None, 'Berlin', 'London', 'Tokyo', None]}
df = pd.DataFrame(data3)

# Check for missing values
print(df.isnull())

# Drop rows with missing values
df_cleaned = df.dropna() # Returns boolean is none?
print(df_cleaned)

# Fill missing values
df_filled = df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean(), 'City': 'Unknown'})
print(df_filled) 


#Data Filtering 
df_filtered = df[df['Age']>30] #Iterating each row, if the age section is greater than 30
print(df_filtered) 


#Transforming Data  
#Searches for the "New Column" Column, makes new one if not there and sets it equal to another column
df['New Column'] = df['Age']*12 
print(df) 

#Data Aggregation & Grouping  
#Summarize and analyze data by grouping similar values and applying  

data = {'Name': ['John', 'Anna', 'Peter', 'Linda', 'John'],
        'Age': [28, 24, 35, 32, 28],
        'City': ['New York', 'Paris', 'Berlin', 'London', 'New York'],
        'Score': [85, 90, 78, 92, 88]} 
dataFrame = pd.DataFrame(data) 

#Group by column and aggregate 
grouped = dataFrame.groupby('City')  
agg = grouped['Age'].mean()
print(agg) 


# Group by multiple columns and aggregate
multi_grouped = dataFrame.groupby(['Name', 'City'])
multi_agg = multi_grouped['Score'].mean()
print(multi_agg) 

#Joining Data Frames  

# Create two DataFrames
data1 = {'Name': ['John', 'Anna', 'Peter'],
         'Age': [28, 24, 35]}
df1 = pd.DataFrame(data1)

data2 = {'Name': ['John', 'Anna', 'Linda'],
         'City': ['New York', 'Paris', 'London']}
df2 = pd.DataFrame(data2)

# Merge DataFrames on 'Name'
merged_df = pd.merge(df1, df2, on='Name')
print(merged_df) 

#Summary 
#DataFrames and Series are the core data structures in Pandas 
#Data Cleaning and Preprocessing to ensure quality data (handling missing values, filtering, transforming) 
#Data Aggregation and Grouping to summarize data and extract meaningful insights by grouping similar data 

