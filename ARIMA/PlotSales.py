import matplotlib.pyplot as plt
import numpy as py
import json

with open('SalesByDate.json', 'r') as file:
    salesByDate = json.load(file)

dates = list(salesByDate.keys())
sales = list(salesByDate.values())


plt.plot(dates, sales, marker='o', color='b', linestyle='-', label='Sales Jan - Mar')

plt.xlabel('Dates')
plt.ylabel('Sale')
plt.title('Sales Jan - Mar')

plt.xticks(rotation=45, fontsize=5)
plt.legend()

plt.tight_layout()
plt.show()