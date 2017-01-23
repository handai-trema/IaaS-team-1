<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "input";

// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}


$sql = "SELECT ID, Name FROM servers";
$result = mysqli_query($conn, $sql);

if (mysqli_num_rows($result) > 0) {
    // output data of each row
    while($row = mysqli_fetch_assoc($result)) {
        echo "id: " . $row["ID"]. " - Name: " . $row["Name"]. "<br>";
    }
} else {
    echo "0 results";
}

mysqli_close($conn);