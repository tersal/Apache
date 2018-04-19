<!DOCTYPE html>
 <html>
  <head>
   <meta charset="UTF-8">
   <title>A little connection mysql example</title>
  </head>

  <body>
   <h1>This is a Test Query for a database</h1>
   <p>Just a little Example of how this can be done</p>

   <?php 

     $con = mysqli_connect("localhost:3306", "default", "default", "library");

     if (mysqli_connect_errno($con))
     {
       echo "Failed to connect to MySQL: " . mysqli_connect_error();
     }

     $result = mysqli_query($con, "SELECT * FROM Authors");

     while($row = mysqli_fetch_array($result))
       {
        echo $row['Id'] . " " . $row['Name'];
        echo "<p>";
       }
     mysqli_close($con);
   ?>

   </body>
 </html>
