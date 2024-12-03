import pandas as pd

data = pd.read_csv("AQI_Data.csv")

#display the last 6 rows
print("The Last 6 rows are :- ")
print(data.tail(6))
