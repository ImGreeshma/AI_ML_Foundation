import pandas as pd
import sqlite3

customer_csv_url = "https://raw.githubusercontent.com/graphql-compose/graphql-compose-examples/master/examples/northwind/data/csv/customers.csv"
orders_csv_url = "https://raw.githubusercontent.com/graphql-compose/graphql-compose-examples/master/examples/northwind/data/csv/orders.csv"

customers_df = pd.read_csv(customer_csv_url)
orders_df = pd.read_csv(orders_csv_url)

conn = sqlite3.connect(":memory:")
customers_df.to_sql("customers", conn, index=False, if_exists="replace")
orders_df.to_sql("orders", conn, index=False, if_exists="replace")

# query = "SELECT * from orders"
# sql_result = pd.read_sql(query, conn)
# print(sql_result)

# Task 1 — Aggregation and Grouping
# Using only the orders table, write a SQL query that returns each CustomerID along with:
# The total number of orders they placed (order_count)
# The total freight amount across all their orders (total_freight)
# The average freight amount per order (avg_freight)
# Sort the results by total_freight in descending order.
# Run the query using pd.read_sql_query() and display the top 10 rows.

# sql_agg = "SELECT customerID, COUNT(orderID) AS order_count, SUM(freight) AS total_freight, AVG(freight) AS avg_freight " \
# "FROM orders GROUP BY customerID ORDER BY total_freight DESC LIMIT 10" 
# sql_agg_result = pd.read_sql(sql_agg, conn)
# print (sql_agg_result)

# Task 2 — WHERE vs. HAVING
# Write two separate SQL queries to demonstrate the difference between WHERE and HAVING:
# Query A: From the orders table, filter rows where Freight is greater than 50 before aggregation, 
# then group by CustomerID and return the count of such orders as high_freight_orders.

# Query B: From the orders table, group by CustomerID and return only those customers whose total freight exceeds 500, 
# using HAVING. Return CustomerID and total_freight.

# query_A = "SELECT customerID, COUNT(*) AS high_freight_orders from orders WHERE freight > 50 GROUP BY customerID"
# query_A_result = pd.read_sql(query_A, conn)
# print(query_A_result)

# query_B = "SELECT customerID, SUM(freight) AS total_freight FROM orders GROUP BY customerID HAVING SUM(freight) > 500"
# query_B_result = pd.read_sql(query_B, conn)
# print(query_B_result)


# Task 3 — JOIN and Aggregation
# Write a SQL query that joins the customers and orders tables on CustomerID and returns:
# CompanyName (from customers)
# Country (from customers)
# Total number of orders placed (order_count)
# Total freight (total_freight)
# Include only customers who have placed at least one order (i.e., use INNER JOIN).

# Then write a second query using LEFT JOIN that includes all customers, even those with no orders. 
# For customers with no orders, total_freight should appear as NULL or 0.
# inner_join = "SELECT c.companyName, c.country, COUNT(o.orderID) AS order_count, SUM(o.freight) AS total_freight FROM customers c INNER JOIN orders o ON c.customerID = o.customerID GROUP BY c.customerID"
# inner_join_result = pd.read_sql(inner_join, conn)
# print(inner_join_result)

# left_join = "SELECT c.companyName, c.country, COUNT(o.orderID) AS order_count, SUM(o.freight) AS total_freight FROM customers c LEFT JOIN orders o ON c.customerID = o.customerID GROUP BY c.customerID"
# left_join_result = pd.read_sql(left_join, conn)
# print(left_join_result)