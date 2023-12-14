<!DOCTYPE html>
<html lang="en">
<head>
    <!-- ... (your existing head content) ... -->
</head>
<body>
    <h2>Product List</h2>

    <form action="/search" method="GET">
    <label for="category">Search by Category:</label>
    <input type="text" name="category_name" id="category" placeholder="Enter category name">
    <button type="submit">Search</button>
</form>


    <table border="1">
        <tr>
            <th>Product ID</th>
            <th>Product Name</th>
            <th>Price</th>
            <th>Category Name</th>
            <th>Update</th>
            <th>Delete</th>
        </tr>
        % for item in data:
            <tr>
                <td>{{item['ProductID']}}</td>
                <td>{{item['ProductName']}}</td>
                <td>{{item['Price']}}</td>
                <!-- Check if 'Category' key exists before accessing 'CategoryName' -->
                % if 'Category' in item and 'CategoryName' in item['Category']:
                    <td>{{item['Category']['CategoryName']}}</td>
                % else:
                    <td>N/A</td>
                % end
                <td><a href="/update/{{item['ProductID']}}">Update</a></td>
                <td><a href="/delete/{{item['ProductID']}}">Delete</a></td>
            </tr>
        % end
    </table>
    <a href="/add">Add Product</a>
</body>
</html>
