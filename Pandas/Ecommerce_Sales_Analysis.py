import pandas as pd
import random
random.seed(42)

# Define data parameters
regions = ['North', 'South', 'East', 'West']
categories = ['Electronics', 'Clothing', 'Home & Garden', 'Sports', 'Books']
salespersons = ['Alice', 'Bob', 'Carol', 'David', 'Emma', 'Frank']

# Generate 200 sales transactions
data ={
    "transaction_id" : range(1001, 1201),
    "region" : [random.choice(regions) for _ in range(200)],
    "category" : [random.choice(categories) for _ in range(200)],
    "salesperson" : [random.choice(salespersons) for _ in range(200)],
    "sales_amount" : [round(random.uniform(50, 5000), 2) for _ in range(200)],
    "customer_id" : [random.randint(5000, 5100) for _ in range(200)]
}

df = pd.DataFrame(data) 

# print (df)
# print(df.head(5))
# print(f"\n Dataset Shape: {df.shape}")

# Task 1: Basic Grouping and Single Aggregations
# Perform the following grouping operations:
# Calculate total sales amount for each region using groupby() and sum()
# For each result, use reset_index() to convert the result into a clean DataFrame
sales__region = df.groupby("region")["sales_amount"].sum().sort_values(ascending=False).reset_index()
sales__region__renamed = sales__region.rename(columns={"region":"Region","sales_amount":"Total Sales"})
print(sales__region__renamed)


# Count the number of transactions for each product category using groupby() and count()
# For each result, use reset_index() to convert the result into a clean DataFrame
trans__category = df.groupby("category")["transaction_id"].count().reset_index()
trans__category_renamed = trans__category.rename(columns={"category":"Product Category","transaction_id":"Total Transactions"})
print(trans__category_renamed)


# Calculate the average sales amount per salesperson using groupby() and mean()
# For each result, use reset_index() to convert the result into a clean DataFrame
person__avg_sale = round(df.groupby("salesperson")["sales_amount"].mean(),2).reset_index()
person__avg_sale__renamed = person__avg_sale.rename(columns={"salesperson":"Sales Person","sales_amount":"Average Sales"})
print(person__avg_sale__renamed)


# Sort the regional sales results in descending order using sort_values(ascending=False) to identify the top-performing region






# Task 2: Multi-Column Grouping and Multiple Aggregations
# Perform advanced grouping analysis:
# Group by both region AND category to calculate total sales for each combination using:
# df.groupby(['region', 'category'])['sales_amount'].sum().reset_index()
# For each salesperson, calculate three metrics simultaneously using the agg() method:
# Total sales ('sum')
# Average sales ('mean')
# Number of transactions ('count')
# Use this syntax:
# df.groupby('salesperson')['sales_amount'].agg(['sum', 'mean', 'count']).reset_index()
# Sort the salesperson results by total sales in descending order to identify the top performer
# Use .idxmax() on the grouped category sales to find which category has the maximum total revenue

region__categoty__sales = df.groupby(["region","category"])["sales_amount"].sum().reset_index()
print(region__categoty__sales)

person__metrics = df.groupby("salesperson").agg({
                                "sales_amount" : ["sum", "mean"],
                                "transaction_id" : "count"
                                }).round(2).reset_index()
print(person__metrics)


person__metrics__sorted = person__metrics.sort_values(by=("sales_amount","sum"),ascending=False).reset_index()
print(person__metrics__sorted)

print(df.loc[region__categoty__sales.idxmax()])


# Task 3: Custom Aggregation and Complete Sales Report
# Create a comprehensive sales analysis report:
# Define a custom aggregation function that calculates the sales range (max - min) for each group:
# def sales_range(x):
#     return x.max() - x.min()
# Apply this custom function along with standard aggregations to analyze sales by region:
# df.groupby('region')['sales_amount'].agg(['sum', 'mean', 'min', 'max', sales_range]).reset_index()
# Create a final summary report that shows for each region:
# Total number of transactions (using customer_id with count)
# Total sales amount
# Average transaction value
# Use dictionary syntax in agg():
# df.groupby('region').agg({
#     'sales_amount': ['sum', 'mean'],
#     'customer_id': 'count'
# }).reset_index()
# Explain the multi-level column structure that results from the dictionary-based aggregation and how it differs from single aggregations

# def sales_range(x):
#     return x.max() - x.min()

sales_by_region = df.groupby("region").agg(
    {
        "sales_amount" : ["sum", "mean", "min", "max", sales_range]
    }
).round(2).reset_index()

print(sales_by_region)


print(df.groupby("region").agg(
    {
        "customer_id" : "count",
        "sales_amount" : ["sum", "mean"]
    }
).round(2).reset_index().rename(columns= {"region" : "Region", "customer_id": "Customer_ID", "sales_amount" : "Total_Sales_Amount"}))