import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Creating a sample dataset
data = {
    'Year': [2019, 2020, 2021, 2022, 2023],
    'Revenue': [50, 55, 60, 70, 80],
    'Profit': [5, 7, 8, 10, 12],
    'Customer_Satisfaction': [78, 82, 85, 88, 90]
}
df = pd.DataFrame(data)

# Line graph
plt.figure(figsize=(8, 5))
plt.plot(df['Year'], df['Revenue'], marker='o', label='Revenue')
plt.plot(df['Year'], df['Profit'], marker='s', label='Profit')
plt.title("Company Performance Over Years")
plt.xlabel("Year")
plt.ylabel("Amount (in millions)")
plt.legend()
plt.grid(True)
plt.show()

# Bar graph
plt.figure(figsize=(8, 5))
bar_width = 0.4
x = np.arange(len(df['Year']))
plt.bar(x - bar_width/2, df['Revenue'], width=bar_width, label='Revenue', color='skyblue')
plt.bar(x + bar_width/2, df['Profit'], width=bar_width, label='Profit', color='orange')
plt.xticks(x, df['Year'])
plt.title("Revenue and Profit Over Years")
plt.xlabel("Year")
plt.ylabel("Amount (in millions)")
plt.legend()
plt.show()

# Scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(df['Customer_Satisfaction'], df['Profit'], color='green', s=100)
plt.title("Profit vs Customer Satisfaction")
plt.xlabel("Customer Satisfaction (%)")
plt.ylabel("Profit (in millions)")
plt.grid(True)
plt.show()
