import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Creating a Series
city_series=pd.Series(["Tokyo","Los Angeles","London"], name= "City") #Creating a Series with a list of city names and assigning it the name "City"
print(f"Pandas Series:\n{city_series}\n")

#Creating a DataFrame
data ={
    "City" : ["Tokyo","Los Angeles","London"],
    "Latitude" : [35.6895, 34.0522, 51.5074],
    "Longitude" : [139.6917, -118.2437, -0.1278],
}
df = pd.DataFrame(data)
print(f"Pandas DataFrame:\n{df}\n")

#******Difference between Series and DataFrame:**********
#A Series is a one-dimensional array that can hold any data type, while a DataFrame is a two-dimensional table that can hold multiple Series (columns) of data. A Series has a single index, while a DataFrame has both row and column indices. A Series is typically used for a single column of data, while a DataFrame is used for tabular data with multiple columns.

#Basic Operations on DataFrame

#Selecting a specific column
latitudes = df['Latitude']
print(f"Selected Column (Latitude):\n{latitudes}\n")

#Filtering rows based on a condition
df_filtered = df[df["Longitude"] < 0] #Filtering the DataFrame to include only rows where the Longitude is less than 0
print(f"Filtered DataFrame (Longitude < 0):\n{df_filtered}\n")

#Adding a new column with a calculation
df["Lat_Radians"]=np.radians(df["Latitude"]) #Adding a new column "Lat_Radians" to the DataFrame by converting the Latitude values from degrees to radians using the numpy radians function
print(f"DataFrame with New Column (Lat_Radians):\n{df['Lat_Radians']}\n")
print(f"Updated DataFrame:\n{df}\n")

#******Grouping and Aggregation:**********
# Creating a DataFrame
data = {
    "City": ["Tokyo", "Los Angeles", "London", "Paris", "Chicago"],
    "Country": ["Japan", "USA", "UK", "France", "USA"],
    "Population": [37400068, 3970000, 9126366, 2140526, 2665000],
}
df = pd.DataFrame(data)
print(f"Grouped DataFrame:\n{df}\n")

# Grouping by Country and calculating the total population
df_grouped = df.groupby("Country")["Population"].sum() #Grouping the DataFrame by the "Country" column and calculating the sum of the "Population" column for each country using the groupby and sum functions (sum of USA)
print(f"Total Population by Country:\n{df_grouped}\n")

#***Merging DataFrames:***
# Creating two DataFrames
df1= pd.DataFrame(
    {
        "City": ["Tokyo", "Los Angeles", "London"],
        "Country": ["Japan", "USA", "UK"],
    }
)
df2= pd.DataFrame(
    {
        "City": ["Tokyo", "Los Angeles", "London"],
        "Population": [37400068, 3970000, 9126366],
    }
)
print(f"DataFrame 1:\n{df1}\n")
print(f"DataFrame 2:\n{df2}\n")

df_merged=pd.merge(df1, df2, on="City") #Merging the two DataFrames (df1 and df2) based on the common "City" column using the merge function
print(f"Merged DataFrame:\n{df_merged}\n")

#***Handling Missing Data:***
# Creating a DataFrame with missing values
data_with_nan = {
    "City": ["Tokyo", "Los Angeles", "London", "Paris"],
    "Population": [37400068, None, 9126366, 2140526], #Introducing a missing value (None) for the population of Los Angeles in the DataFrame
}
df_nan = pd.DataFrame(data_with_nan)
print(f"DataFrame with Missing Values:\n{df_nan}\n")

# Filling missing values with a specific value 
df_filled = df_nan.fillna(df_nan["Population"].mean()) #Filling the missing value in the "Population" column with the mean of the existing population values using the fillna function
print(f"DataFrame with Filled Missing Values:\n{df_filled}\n")

#****Reading Geospatial Data from a CSV File:****
url = "https://github.com/opengeos/datasets/releases/download/world/world_cities.csv"
df= pd.read_csv(url) #Reading a CSV file containing geospatial data about world cities from the provided URL using the read_csv function
print(df.columns) #Displaying the column names of the DataFrame to understand the structure of the data and identify the relevant columns for analysis

print(f"Geospatial Data from CSV:\n{df.head()}\n") #Displaying the first few rows of the DataFrame to verify that the data has been loaded correctly using the head function

#Calculate the total population of all cities in the dataset using NumPy and Pandas
np.sum(df["population"]) #Calculating the total population of all cities in the dataset by summing the values in the "Population" column using the numpy sum function

df["population"].sum() #Calculating the total population of all cities in the dataset by summing the values in the "Population" column using the pandas sum function. Panda Method

#both method difference: The main difference between using NumPy and Pandas for summing the population is that the Pandas method (df["Population"].sum()) is more efficient and optimized for handling missing values (NaN) in the data, while the NumPy method (np.sum(df["Population"])) may not handle NaN values properly and could return an incorrect result if there are any missing values in the "Population" column. Additionally, the Pandas method provides more functionality and options for handling different data types and structures compared to NumPy.

#******CREATING PLOTS USING PANDAS****
# Workflow:
#1. Load the dataset from a source
#2. Display the first few rows of the dataset

url= "https://raw.githubusercontent.com/pandas-dev/pandas/main/doc/data/air_quality_no2.csv"
air_quality=pd.read_csv(url)

airShow= air_quality.head()

print(f"Air Quality Data:\n{airShow}\n")
air_quality.plot() #Creates the graph
plt.show()# Display

#Note: print(air_quality.plot()) will not print graph it will give Axes(0.125,0.11;0.775x0.77), which is the object representation of the plot.  

air_quality['station_paris'].plot()
plt.show()

air_quality.plot.scatter(x='station_london', y='station_paris',alpha=0.5) #Creating a scatter plot to visualize the relationship between NO2 levels in London and Paris using the scatter function, with the x-axis representing NO2 levels in London and the y-axis representing NO2 levels in Paris, and setting the transparency of the points to 0.5 using the alpha parameter

air_quality.plot.area(figsize=(12, 4), subplots=True)#Creating area plots for each station's NO2 levels over time using the area function, with a specified figure size of 12x4 inches and creating separate subplots for each station using the subplots parameter
plt.show()

#*****Analyzing Geospatial Data*******
#Define the Haversine formula using NumPy

def hav_np(lat1,long1,lat2,long2):
    R=6371.0 #earth radius in m
    dlat=np.radians(lat2-lat1)
    dlong=np.radians(long2-long1)
    a=(np.sin(dlat/2)**2+np.cos(np.radians(lat1))*np.cos(np.radians(lat2)*np.sin(dlong/2)**2)
       )
    c=2*np.arctan2(np.sqrt(a),np.sqrt(1-a))
    distance=R*c
    return distance

#Create a new DataFrame with city pairs
city_pairs=pd.DataFrame(
    {
        "City1": ["Tokyo", "Tokyo", "Los Angeles"],
        "City2": ["Los Angeles", "London", "London"],
        "Lat1": [35.6895, 35.6895, 34.0522],
        "Lon1": [139.6917, 139.6917, -118.2437],
        "Lat2": [34.0522, 51.5074, 51.5074],
        "Lon2": [-118.2437, -0.1278, -0.1278],
    }
)
print(city_pairs)

#Calculate distance between city pairs
city_pairs['Distance_km']=hav_np(
    city_pairs['Lat1'],city_pairs['Lon1'],city_pairs['Lat2'],city_pairs['Lon2']
)
print(city_pairs)