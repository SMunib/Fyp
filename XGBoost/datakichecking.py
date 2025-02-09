import pandas as pd


items = pd.read_csv("items.csv")
trainData = pd.read_csv("train_subset_2015.csv")
holidays = pd.read_csv("holidays_2015.csv")
oil = pd.read_csv("oil_2015.csv")
weather = pd.read_csv("weather_2015.csv")

# print(items.head())
# print(trainData.head())
# print(holidays.head())
# print(oil.head())
# print(weather.head())

weather.rename(columns={'Date': 'date'}, inplace=True)

trainData = trainData.merge(items[['item_nbr', 'family', 'class', 'perishable']], on='item_nbr', how='left')
trainData = trainData.merge(oil[['date', 'dcoilwtico']], on='date', how='left')
trainData = trainData.merge(holidays[['date', 'type', 'locale', 'transferred']], on='date', how='left')
trainData = trainData.merge(weather[['date', 'Avg Temperature (C)']], on='date', how='left')

def NanWAvg(df, col):
    for i in range(len(df)):
        if pd.isna(df.loc[i, col]):
            start = max(0, i - 3)
            end = min(len(df), i + 4)

            values = df[col][start:end]
            avg = values.dropna().mean()

            df.loc[i, col] = avg

def NanWNaN(df, col):
    for i in range(len(df)):
        if pd.isna(df.loc[i, col]):
            df.loc[i, col] = None

trainData.rename(columns={'Avg Temperature (C)': 'avg_temp'}, inplace=True)
# print(trainData)

# NanWAvg(trainData, 'avg_temp')
# NanWAvg(trainData, 'dcoilwtico')

# NanWNaN(trainData, 'type')
# NanWNaN(trainData, 'locale')
# NanWNaN(trainData, 'transferred')

trainData.to_csv("train_data_2015.csv")