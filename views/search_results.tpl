<!DOCTYPE html>
<html lang="en">
<head>
    <!-- ... (your head content) ... -->
</head>
<body>
    <h2>Search Results</h2>
    <table border="1">
        <tr>
            <th>Product ID</th>
            <th>Product Name</th>
            <th>Price</th>
            <th>Category Name</th>
            <th>Update</th>
            <th>Delete</th>
        </tr>
        % for item in search_results:
            <tr>
                <td>{{item['ProductID']}}</td>
                <td>{{item['ProductName']}}</td>
                <td>{{item['Price']}}</td>
                <td>{{item['Category']['CategoryName']}}</td>
                <td><a href="/update/{{item['ProductID']}}">Update</a></td>
                <td><a href="/delete/{{item['ProductID']}}">Delete</a></td>
            </tr>
        % end
    </table>
    <a href="/list">Back to List</a>
</body>
</html>
