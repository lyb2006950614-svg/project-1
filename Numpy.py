import csv
import numpy as np


file_path = 'grocery_inventory_and_sales_dataset.csv'

product_names = []
stock_levels = []
unit_prices = []
sales_volumes = []

with open(file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        product_names.append(row['Product_Name'])
        stock_levels.append(int(row['Stock_Quantity']))
        clean_price = row['Unit_Price'].replace('$', '').strip()
        unit_prices.append(float(clean_price))
        sales_volumes.append(int(row['Sales_Volume']))

names_arr = np.array(product_names)
stock_arr = np.array(stock_levels)
price_arr = np.array(unit_prices)
sales_arr = np.array(sales_volumes)


inventory_values = stock_arr * price_arr

print("=== (1) 每個商品的總庫存價值 ===")
for i in range(min(990, len(names_arr))):
    print(f"商品: {names_arr[i]} | 庫存價值: ${inventory_values[i]:.2f}")
print("\n")



best_seller_index = np.argmax(sales_arr)
best_seller_name = names_arr[best_seller_index]
best_seller_volume = sales_arr[best_seller_index]

print("=== (2) 最暢銷商品 ===")
print(f"最暢銷商品為: {best_seller_name}，銷量高達: {best_seller_volume} 件")
print("\n")


revenue_per_item = sales_arr * price_arr

total_discounted_revenue = np.sum(revenue_per_item) * 0.9

print("=== (3) 9 折後的總收入 ===")
print(f"所有商品銷售金額打 9 折後，總收入為: ${total_discounted_revenue:,.2f}")