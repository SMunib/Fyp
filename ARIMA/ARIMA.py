import pandas as pd
import json
from pandas.plotting import autocorrelation_plot
from matplotlib import pyplot
from datetime import datetime
from statsmodels.tsa.arima.model import ARIMA

with open('SalesByDate.json', 'r') as file:
    salesByDate = json.load(file)

sales = pd.DataFrame(list(salesByDate.items()), columns=['Date', 'Sales'])

sales['Date'] = pd.to_datetime(sales['Date']).dt.strftime('%Y-%m-%d')
sales['Date'] = pd.to_datetime(sales['Date'])
sales['Sales'] = pd.to_numeric(sales['Sales'], errors='coerce')

salesAsSeries = sales['Sales']

# autocorrelation_plot(sales['Sales'])
# pyplot.show()

model = ARIMA(salesAsSeries, order=(15,1,0))
model_fit = model.fit()
# print(model_fit.summary())

residualsPatterns = pd.DataFrame(model_fit.resid)
residualsPatterns.plot()
pyplot.show()

residualsPatterns.plot(kind='kde')
pyplot.show()

print(residualsPatterns.describe())