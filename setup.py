import sqlite3

connection = sqlite3.connect("product_category_db.db")

cursor = connection.cursor()

try:
    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.execute("DROP TABLE IF EXISTS categories")
except Exception as e:
    print(f"Error dropping tables: {e}")

# Create the 'products' table
try:
    cursor.execute("CREATE TABLE products (ProductID INTEGER PRIMARY KEY, ProductName TEXT, Price REAL, CategoryID INTEGER, FOREIGN KEY (CategoryID) REFERENCES categories(CategoryID))")
except Exception as e:
    print(f"Error creating 'products' table: {e}")

# Create the 'categories' table
try:
    cursor.execute("CREATE TABLE categories (CategoryID INTEGER PRIMARY KEY, CategoryName TEXT)")
except Exception as e:
    print(f"Error creating 'categories' table: {e}")

# Insert sample data into 'categories' table
categories_data = [('Electronics',),
                   ('Clothing',),
                   ('Books',),
                   ('Home and Kitchen',),
                   ('Toys and Games',)]

for category_data in categories_data:
    try:
        cursor.execute("INSERT INTO categories (CategoryName) VALUES (?)", category_data)
    except Exception as e:
        print(f"Error inserting data into 'categories' table: {e}")

# Insert sample data into 'products' table
products_data = [('Laptop', 999.99, 1),
                 ('T-shirt', 19.99, 2),
                 ('The Great Gatsby', 12.99, 3),
                 ('Coffee Maker', 49.99, 4),
                 ('Board Game', 29.99, 5)]

for product_data in products_data:
    try:
        cursor.execute("INSERT INTO products (ProductName, Price, CategoryID) VALUES (?, ?, ?)", product_data)
    except Exception as e:
        print(f"Error inserting data into 'products' table: {e}")

connection.commit()
connection.close()
print("done.")
