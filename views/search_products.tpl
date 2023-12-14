<!DOCTYPE html>
<html lang="en">
<head>
    <!-- ... (your existing head content) ... -->
</head>
<body>
    <h2>Search Products</h2>
    <form action="/search" method="post">
        <label for="query">Category Name:</label>
        <input type="text" id="query" name="query" required>
        <button type="submit">Search</button>
    </form>
    <br>
    <a href="/list">Back to Product List</a>
</body>
</html>
