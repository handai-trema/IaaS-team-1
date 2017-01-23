<?php
$servername = "localhost";
$username = "root";
$password = "";
$database = "input";

//Receive the RAW post data via the php://input IO stream.
$content = file_get_contents("php://input");


//Make sure that it is a POST request.
if(strcasecmp($_SERVER['REQUEST_METHOD'], 'POST') != 0){
    throw new Exception('Request method must be POST!');
}
 
//Make sure that the content type of the POST request has been set to application/json
$contentType = isset($_SERVER["CONTENT_TYPE"]) ? trim($_SERVER["CONTENT_TYPE"]) : '';
if(strcasecmp($contentType, 'application/json') != 0){
    throw new Exception('Content type must be: application/json');
}
 
//Receive the RAW post data.
$content = trim(file_get_contents("php://input"));
 
//Attempt to decode the incoming RAW post data from JSON.
$decoded = json_decode($content, true);
 
//If json_decode failed, the JSON is invalid.
if(!is_array($decoded)){
    throw new Exception('Received content contained invalid JSON!');
}
 
//Process the JSON.

var_dump($decoded);

// Create connection
$conn = mysqli_connect($servername, $username, $password, $database);

// Check connection
if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
}
echo "Connected successfully";

//read the json file contents
    $jsondata = file_get_contents('test.json');
	
	 //convert json object 
   
   $data=$decoded;
	
	$keys = array_keys($data);

	
					$sql2 = "TRUNCATE TABLE servers";

		
		if (mysqli_query($conn, $sql2)) {
    echo "Old records deleted";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}

for($i = 0; $i < count($data); $i++) {


    foreach($data[$keys[$i]] as $key => $value) {

        echo $key . " : " . $value . "<br>";
		
		$sql = "INSERT INTO servers (ID, Name)
VALUES ('', '$value')";
		


if (mysqli_query($conn, $sql)) {
    echo "New record created successfully";
} else {
    echo "Error: " . $sql . "<br>" . mysqli_error($conn);
}
		
	
	    }

    echo "}<br>";

}


?>