import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data.csv', parse_dates=['Date'], index_col='Date')

# Plot the data
data['Demand'].plot(title='Product Demand Over Time', figsize=(10, 6))
plt.show()
