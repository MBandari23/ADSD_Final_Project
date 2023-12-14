from bottle import route, post, run, template, redirect, request, TEMPLATE_PATH, HTTPError
import product_database
import os
import traceback

# Set the template path explicitly
current_dir = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH.insert(0, os.path.join(current_dir, 'views'))

# Call set_up_database to create tables and insert sample data
product_database.set_up_database()

@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    try:
        # Fetch data from both tables using a JOIN
        items = product_database.get_products_and_categories()
        return template("list_products.tpl", data=items)
    except Exception as e:
        traceback.print_exc()
        return template('error', {'message': f'Error retrieving product list: {e}'})
@route("/search")
def get_search():
    return template("search_products.tpl")

@post("/search")
def post_search():
    query = request.forms.get("query")

    if query:
        # Assuming you want to search by category
        items = product_database.search_products_by_category(query)
        return template("search_results.tpl", search_results=items)
    else:
        redirect("/list")

@route("/list")
def get_list():
    try:
        # Set up the database
        product_database.set_up_database()

        # Fetch data from both tables using a JOIN
        items = product_database.get_products_and_categories()
        return template("list_products.tpl", data=items)
    except Exception as e:
        traceback.print_exc()
        return template('error', {'message': f'Error retrieving product list: {e}'})

@route("/search_results")
def get_search_results():
    return template("search_results.tpl", search_results=[])

@route("/add")
def get_add():
    return template("add_product.tpl")

@post("/add")
def post_add():
    product_id = request.forms.get("product_id")
    product_name = request.forms.get("product_name")
    price = request.forms.get("price")
    category_name = request.forms.get("category_name")

    try:
        # Check if product_id is provided and not None before converting to int
        if product_id is not None:
            product_id = int(product_id)
        else:
            raise HTTPError(400, "Product ID is required")
    except ValueError:
        return template('error', {'message': 'Invalid product ID format'})

    try:
        # Add product
        product_database.add_product_and_category(product_name, float(price), category_name)
        items = product_database.get_products_and_categories()
        return template("list_products.tpl", data=items)
    except Exception as e:
        traceback.print_exc()
        return template('error', {'message': f'Error adding product: {e}'})

# ... (Previous code)

@route("/update/<product_id>")
def get_update(product_id):
    try:
        # Get product information by ID
        items = product_database.get_product_and_category(product_id)

        # Check if the product is found
        if not items:
            return template('error', {'message': 'Product not found'})

        # Render the update_product template with the product information
        return template("update_product.tpl", item=items[0])
    except Exception as e:
        traceback.print_exc()
        return template('error', {'message': f'Error updating product: {e}'})

@post("/update")
def post_update():
    product_id = request.forms.get("product_id")
    product_name = request.forms.get("product_name")
    price = request.forms.get("price")
    category_name = request.forms.get("category_name")

    try:
        # Update product
        product_database.update_product_and_category(product_id, product_name, float(price), category_name)
        # Instead of redirecting, call the get_list function directly
        return get_list()
    except Exception as e:
        traceback.print_exc()
        return template('error', {'message': f'Error updating product: {e}'})

@route("/delete/<id>")
def get_delete(id):
    try:
        # Delete product
        product_database.delete_product_and_category(id)
        
        # Fetch updated data
        items = product_database.get_products_and_categories()
        
        # Render the template with the updated data
        return template("list_products.tpl", data=items)
    except Exception as e:
        traceback.print_exc()
        return template('error', {'message': f'Error deleting product: {e}'})

# ... (Other routes)

run(host='localhost', port=8080)

# ... (Other routes)




