import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file into a DataFrame
sales_data = pd.read_csv('supermarket_sales - Sheet1.csv')

# Sales Performance by Location
# Group the sales data by city and calculate the total sales
sales_by_location = sales_data.groupby('City')['Total'].sum().reset_index()

# Sort the data by total sales in descending order
sales_by_location = sales_by_location.sort_values(by='Total', ascending=False)

# Calculate the percentage of total sales for each location
total_sales = sales_data['Total'].sum()
sales_by_location['Percentage of Total Sales'] = sales_by_location['Total'] / total_sales * 100

# Print the resulting DataFrame
print(sales_by_location)

# Visualize the results with a bar plot
plt.figure(figsize=(10, 6))
sns.barplot(x='City', y='Total', data=sales_by_location, color='skyblue')
plt.title('Sales Performance by Location')
plt.xlabel('Location')
plt.ylabel('Total Sales')
plt.show()

# Sales Performance by Product Category
# Group the sales data by product category and calculate the total sales
sales_by_category = sales_data.groupby('Product line')['Total'].sum().reset_index()

# Sort the data by total sales in descending order
sales_by_category = sales_by_category.sort_values('Total', ascending=False)

# Reset the index and display the table
sales_by_category = sales_by_category.reset_index(drop=True)
print(sales_by_category)

# Create a bar chart of sales by product category
sns.barplot(x='Product line', y='Total', data=sales_by_category)
plt.title('Sales Performance by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.xticks(rotation=45, ha='right')
plt.show()

# Sales Performance by Customer Demographics
# Group the sales data by gender and calculate the total sales
sales_by_gender = sales_data.groupby('Gender')['Total'].sum().reset_index()

# Print the results
print("Sales Performance by Gender:")
print(sales_by_gender)
print()

# Create a bar chart of sales by gender
sns.barplot(x='Gender', y='Total', data=sales_by_gender)
plt.title('Sales Performance by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Sales')
plt.show()

# Group the sales data by payment method and calculate the total sales
sales_by_payment_method = sales_data.groupby('Payment')['Total'].sum().reset_index()
print("Sales Performance by Payment Method:")
print(sales_by_payment_method)
print()

# Create a pie chart of sales by payment method
plt.pie(sales_by_payment_method['Total'], labels=sales_by_payment_method['Payment'], autopct='%1.1f%%')
plt.title('Sales by Payment Method')
plt.show()

