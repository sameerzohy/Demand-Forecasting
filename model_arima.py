import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('data.csv', parse_dates=['Date'], index_col='Date')

# Split into train and test
train = data[:-12]
test = data[-12:]

# Fit the model
model = SARIMAX(train['Demand'], order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))
result = model.fit()

# Forecast
forecast = result.forecast(steps=12)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(data['Demand'], label='Actual')
plt.plot(forecast, label='Forecast', color='red')
plt.legend()
plt.show()
