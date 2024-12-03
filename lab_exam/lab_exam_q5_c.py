import pandas as pd
import numpy as np

# Load the data set
data = pd.read_csv("AQI_Data.csv")

# Filter the data where AQI is greater than 300 and PM10 is greater than 200
filtered_data = data[(np.array(data['AQI']) > 300) & (np.array(data['PM10']) > 200)]

# Display the filtered data
print(filtered_data)
