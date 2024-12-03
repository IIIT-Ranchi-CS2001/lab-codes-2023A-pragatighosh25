import pandas as pd

# Load the data set
data = pd.read_csv("AQI_Data.csv")

# Display all rows where the city is Delhi
delhi_data = data[data['City'] == 'Delhi']
print(delhi_data)
