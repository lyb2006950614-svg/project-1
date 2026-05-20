import numpy as np
import pandas as pd

stock1_list = [120, 80, None, 60, 95, None, 110]
stock1 = pd.Series(stock1_list)

index_labels = [
    "Apple",
    "Banana",
    "Orange",
    "Mango",
    "Grape",
    "Peach",
    "Melon",
]
stock2 = pd.Series(stock1_list, index=index_labels)

stock3 = stock2.to_dict()


print("stock1")
print(stock1)
print()

print("stock2")
print(stock2)
print()

print("stock3")
print(stock3)
print()

print(f"Banana 庫存： {stock2['Banana']}")
print()

print("缺失值檢查：")
null_check = stock2.isnull()
print(null_check)
print()

print(f"缺失值數量： {null_check.sum()}")

stock2.to_csv("0520_stock.csv", header=["Inventory"])