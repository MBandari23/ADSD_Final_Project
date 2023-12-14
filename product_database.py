import sqlite3

connection = sqlite3.connect("product_category_db.db")

def get_product_and_category(product_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Query to fetch product details along with category name
    cursor.execute(
        """
        SELECT p.ProductID, p.ProductName, p.Price, c.CategoryName
        FROM products p
        JOIN categories c ON p.CategoryID = c.CategoryID
        WHERE p.ProductID = ?
        """,
        (product_id,),
    )

    # Fetch the result
    result = cursor.fetchall()

    connection.close()

    return result


DB_NAME = "product_category.db"

def get_product_and_category(product_id):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Fetch the product details with the given product_id
    cursor.execute(
        """
        SELECT p.ProductID, p.ProductName, p.Price, c.CategoryName
        FROM products p
        JOIN categories c ON p.CategoryID = c.CategoryID
        WHERE p.ProductID = ?
        """,
        (product_id,),
    )

    result = cursor.fetchall()

    connection.close()

    return result



def get_products_and_categories():
    cursor = connection.cursor()
    cursor.execute(
        "SELECT p.ProductID, p.ProductName, p.Price, c.CategoryName "
        "FROM products p JOIN categories c ON p.CategoryID = c.CategoryID"
    )
    rows = cursor.fetchall()
    items = []
    for row in rows:
        item = {
            'ProductID': row[0],
            'ProductName': row[1],
            'Price': row[2],
            'Category': {'CategoryName': row[3]}
        }
        items.append(item)
    return items

# ... (your existing database functions) ...


def add_product_and_category(product_name, price, category_name):
    cursor = connection.cursor()

    # Check if the category exists; if not, add it
    cursor.execute(f"INSERT OR IGNORE INTO categories (CategoryName) VALUES ('{category_name}')")
    connection.commit()

    # Get the CategoryID for the given category
    cursor.execute(f"SELECT CategoryID FROM categories WHERE CategoryName = '{category_name}'")
    category_id = cursor.fetchone()[0]

    # Add product without specifying ProductID (let the database generate it)
    cursor.execute(f"INSERT INTO products (ProductName, Price, CategoryID) VALUES ('{product_name}', {price}, {category_id})")
    connection.commit()


def update_product_and_category(product_id, product_name, price, category_name):
    cursor = connection.cursor()

    # Check if the category exists; if not, add it
    cursor.execute(f"INSERT OR IGNORE INTO categories (CategoryName) VALUES ('{category_name}')")
    connection.commit()

    # Get the CategoryID for the given category
    cursor.execute(f"SELECT CategoryID FROM categories WHERE CategoryName = '{category_name}'")
    category_id = cursor.fetchone()[0]

    # Update product
    cursor.execute(f"UPDATE products SET ProductName='{product_name}', Price={price}, CategoryID={category_id} WHERE ProductID={product_id}")
    connection.commit()

def delete_product_and_category(product_id):
    cursor = connection.cursor()

    # Delete product
    cursor.execute(f"DELETE FROM products WHERE ProductID={product_id}")
    connection.commit()

DB_NAME = "product_category.db"

def set_up_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # Create categories table if it does not exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS categories (
            CategoryID INTEGER PRIMARY KEY,
            CategoryName TEXT
        )
        """
    )

    # Create products table if it does not exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS products (
            ProductID INTEGER PRIMARY KEY,
            ProductName TEXT,
            Price REAL,
            CategoryID INTEGER,
            FOREIGN KEY (CategoryID) REFERENCES categories(CategoryID)
        )
        """
    )
def test_set_up_database():
    print("testing set_up_database()")
    set_up_database()
    items = get_products_and_categories()
    assert len(items) == 5
    product_ids = [item['ProductID'] for item in items]
    product_names = [item['ProductName'] for item in items]
    prices = [item['Price'] for item in items]
    category_ids = [item['CategoryID'] for item in items]
    category_names = [item['CategoryName'] for item in items]

    print("Product IDs:", product_ids)
    print("Product Names:", product_names)
    print("Prices:", prices)
    print("Category IDs:", category_ids)
    print("Category Names:", category_names)

# ... (similar modifications for other test functions)

if __name__ == "__main__":
    try:
        test_set_up_database()
        # ... (call other test functions)
    finally:
        connection.close()
    print("done.")
