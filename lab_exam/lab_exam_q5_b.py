import pandas as pd

data = pd.read_csv("AQI_Data.csv")

#display first 10 rows showing columns City, AQI and PM2.5 
print(data[["CITY", "AQI", "PM2.5"]].head(10))
