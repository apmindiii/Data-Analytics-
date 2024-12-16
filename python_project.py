import pandas as pd

customers_df = pd.read_csv('customers.csv')
#'custno','firstname','lastname','gender','age','profession','contactNo',
#'emailId','city','state','isActive','createdDate','UpdatedDate'
pro_columns = ['productno','productName','Description','isActive','createdDate','UpdatedDate']
products_df = pd.read_csv('products.csv', header=None, names=pro_columns)
tran_columns = ['txnno','txndate','custno','amount','productno','spendby']
transactions_df = pd.read_csv('transactions.csv', header=None, names=tran_columns)
print("----------- UseCase 1 -----------------------------------------------------")
print(" ")
print("Customers Data (first 5 records in csv):")
print(customers_df.head())

print("Products Data (first 5 records in csv):")
print(products_df.head())

print("Transactions Data (first 5 records in csv):")
print(transactions_df.head())

print(" ")
print("------------ UseCase 2 -----------------------------------------------------")

customer_purchases = transactions_df.groupby('custno')['productno'].count()
customers_more_than_3 = customer_purchases[customer_purchases > 3].index
filtered_customers = customers_df[customers_df['custno'].isin(customers_more_than_3)]
print("\nCustomers who purchased more than 3 products:")
print(filtered_customers.head(5))

print(" ")
print("------------ UseCase 3 -----------------------------------------------------")

top_products = transactions_df.groupby('productno').size().sort_values(ascending=False)
print("\nTop 5 most demanded products:")
print(top_products.head(5))

print(" ")
print("------------ UseCase 4 -----------------------------------------------------")

top_transactions = transactions_df.sort_values(by='amount', ascending=False)

print("\nTop 5 transactions by amount:")
print(top_transactions[['custno', 'amount']].head(5))

print(" ")
print("------------ UseCase 5 -----------------------------------------------------")

distinct_professions = customers_df['profession'].unique()
print("\nDistinct professions:")
print(distinct_professions)

print(" ")
print("------------ UseCase 6 -----------------------------------------------------")

max_age = customers_df['age'].max()
print("\nHighest age in the customer dataset:")
print(max_age)

print(" ")
print("------------ UseCase 7 -----------------------------------------------------")

merged_df = pd.merge(customers_df, transactions_df, on='custno')
customer_923_data = merged_df[merged_df['custno'] == 923]
print(customer_923_data[['custno', 'gender', 'age', 'profession', 'contactNo', 'productno', 'txndate', 'spendby', 'amount']])


print(" ")
print("------------ UseCase 8 -------- Psv File ---------------------------------------------")
print(" ")
print("Customer psv file-------------------------------------")
psv_cust_df = pd.read_csv('customers.txt', sep='|')
print(psv_cust_df.head())

print(" ")
print("Product psv file-------------------------------------")
psv_pro_df = pd.read_csv('products.txt', sep='|')
print(psv_pro_df.head())

print(" ")
print("Transaction psv file-------------------------------------")
psv_tran_df = pd.read_csv('transactions.txt', sep='|')
print(psv_tran_df.head())

print(" ")
print("------------ UseCase 9 ----- Xml File ------------------------------------------------")
print(" ")
print("Customer xml file-------------------------------------")
xml_cust_df = pd.read_xml('customers.xml')
print(xml_cust_df.head())

print(" ")
print("Product xml file-------------------------------------")
xml_pro_df = pd.read_xml('products.xml')
print(xml_pro_df.head())

print(" ")
print("Transaction xml file-------------------------------------")
xml_tran_df = pd.read_xml('transactions.xml')
print(xml_tran_df.head())

print(" ")
print("------------ UseCase 10 ----- Json File ------------------------------------------------")
print(" ")
print("Customer json file-------------------------------------")
json_cust_df = pd.read_json('customers.json')
print(json_cust_df.head())

print(" ")
print("Product json file-------------------------------------")
json_pro_df = pd.read_json('products.json')
print(json_pro_df.head())

print(" ")
print("Transaction json file-------------------------------------")
json_tran_df = pd.read_json('transactions.json')
print(json_tran_df.head())