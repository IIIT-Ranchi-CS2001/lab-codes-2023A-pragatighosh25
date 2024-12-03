import pandas as pd

data = pd.read_csv("AQI_Data.csv")

numeric_columns = data.select_dtypes(include=['int64', 'float64']).columns
summary_stats = data[numeric_columns].describe()
print ("Summary statistics for numeric columns: \n", summary_stats)
