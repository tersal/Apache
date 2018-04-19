<!DOCTYPE html>

 <html>
  <head>
   <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
   <title>The last at least</title>
  </head>

  <?php
    $nombre = $_REQUEST['nombre'];
    $comida = $_REQUEST['meal'];
  ?>

  <body>
  <p>
    Hi <?php echo $nombre; ?>
  <p>
    You like <strong><?php echo $comida; ?></strong>

    That's some fine taste
  </body>
 </html>
