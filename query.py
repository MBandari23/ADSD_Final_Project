import sqlite3

connection = sqlite3.connect("product_category_db.db")

cursor = connection.cursor()

# Fetch data from the 'products' table
cursor.execute("SELECT ProductID, ProductName, Price, CategoryID FROM products")
product_rows = list(cursor.fetchall())

# Fetch data from the 'categories' table
cursor.execute("SELECT CategoryID, CategoryName FROM categories")
category_rows = list(cursor.fetchall())

print("Products:")
print(product_rows)

print("\nCategories:")
print(category_rows)

# Combine the data into a single list of dictionaries
product_data = [{'ProductID': row[0], 'ProductName': row[1], 'Price': row[2], 'CategoryID': row[3]} for row in product_rows]
category_data = [{'CategoryID': row[0], 'CategoryName': row[1]} for row in category_rows]

print("\nCombined Data:")
combined_data = []

for product in product_data:
    related_category = next((category for category in category_data if category['CategoryID'] == product['CategoryID']), None)
    if related_category:
        product_copy = product.copy()
        product_copy['Category'] = related_category
        combined_data.append(product_copy)

print(combined_data)
