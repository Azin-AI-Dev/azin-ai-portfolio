import pandas as pd

Reading the data file you created
df = pd.read_csv('sales_data.csv')

Calculating total income for each row
df['Total_Revenue'] = df['Price'] * df['Quantity']

print("--- Taro's Sales Report ---") print(df) print("\nTotal Revenue for this period:") print(df['Total_Revenue'].sum(), "USD")
