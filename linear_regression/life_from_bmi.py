import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import linear_model
import matplotlib.pyplot as plot

dataframe = pd.read_fwf('bmi_and_life_expectancy.csv')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

model = LinearRegression()
model.fit(x_values, y_values)

plt.scatter(x_values, y_values)
plt.plot(x_values, model.predict(x_values) )

model.predict(value)
