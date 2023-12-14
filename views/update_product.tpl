<!-- update_product.tpl -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Update Product</title>
</head>
<body>

<h2>Update Product</h2>

<form action="/update" method="post">
    <input type="hidden" name="product_id" value="{{item['ProductID']}}" />

    <label for="product_name">Product Name:</label>
    <input type="text" name="product_name" value="{{item['ProductName']}}" required/>

    <label for="price">Price:</label>
    <input type="number" step="0.01" name="price" value="{{item['Price']}}" required/>

    <label for="category_name">Category Name:</label>
    <input type="text" name="category_name" value="{{item['CategoryName']}}" required/>

    <!-- Add this line to handle the 'Stock' key -->
    <label for="stock">Stock:</label>
    <input type="text" name="stock" value="{{item.get('Stock', '')}}" required/>

    <button type="submit">Update Product</button>
</form>

</body>
</html>
