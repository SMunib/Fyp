import pandas as pd
from datetime import datetime
import json

#variables
sales = pd.read_csv('supermarket_sales.csv')
salesByDate = {}


#function to check and add sales per every date
def addData(date, sale):
    
    if date in salesByDate:
        salesByDate[date] += sale
    else:
        salesByDate[date] = sale


for x in range(len(sales)):
    date = sales.iloc[x]['Date']
    sale = sales.iloc[x]['Total']
    addData(date, sale)

# sorting dictionary based on key i.e. dates
salesByDate = {k: v for k, v in sorted(salesByDate.items(), key=lambda item: datetime.strptime(item[0], '%m/%d/%Y'))}

# saving the sales info per day in a json file
# with open('SalesByDate.json', 'w') as jsonFile:
#     json.dump(salesByDate, jsonFile, indent=4)