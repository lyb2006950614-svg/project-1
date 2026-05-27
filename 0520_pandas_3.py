import pandas as pd


file_path = 'SuperMarket Analysis.csv'
df = pd.read_csv(file_path)

print("=== 檢視資料筆數與前 3 筆內容 ===")
print(f"總資料筆數: {len(df)} 筆")
print(df.head(3))
print("\n" + "="*50 + "\n")


df.columns = df.columns.str.strip()
if df['Branch'].dtype == 'O': df['Branch'] = df['Branch'].str.strip()
if df['Customer type'].dtype == 'O': df['Customer type'] = df['Customer type'].str.strip()


filtered_df = df[df['Branch'].str.startswith('A') & (df['Customer type'] == 'Member')].copy()

print("=== 篩選後的交易資料筆數 ===")
print(f"符合條件的資料共有: {len(filtered_df)} 筆")
print("\n" + "="*50 + "\n")



product_analysis = filtered_df.groupby('Product line').agg(
    Total_Sales=('Sales', 'sum'),
    Average_Rating=('Rating', 'mean')
).round(2)  # 計算皆至小數後2位

print("=== 各產品線的總銷售額與平均評分 ===")
print(product_analysis)
print("\n" + "="*50 + "\n")



city_gender_analysis = filtered_df.groupby(['City', 'Gender']).agg(
    Average_Sales=('Sales', 'mean'),
    Transaction_Count=('Invoice ID', 'count')
).round(2)

print("=== 依 City 與 Gender 分組的分析結果 ===")
print(city_gender_analysis)
print("\n" + "="*50 + "\n")



best_product_line = product_analysis['Total_Sales'].idxmax()
max_sales_value = product_analysis['Total_Sales'].max()

print("=== 總銷售額最高的產品線 ===")
print(f"最高銷售額產品線: {best_product_line}，總銷售額為: ${max_sales_value}")
print("\n" + "="*50 + "\n")



output_file = '0520_pandas_3OK.CSV'
product_analysis.to_csv(output_file, encoding='utf-8-sig')

print(f"🎉 任務完成！彙總結果已成功輸出至：{output_file}")