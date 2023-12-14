<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Product</title>
</head>
<body>
    <h2>Add Product</h2>
    <form action="/add" method="post">
        <label for="product_id">Product ID:</label>
        <input type="text" name="product_id" required/>
        <br>
        <label for="product_name">Product Name:</label>
        <input type="text" name="product_name" required/>
        <br>
        <label for="price">Price:</label>
        <input type="text" name="price" required/>
        <br>
        <label for="category_name">Category Name:</label>
        <input type="text" name="category_name" required/>
        <br>
        <input type="submit" value="Add Product"/>
    </form>
</body>
</html>
