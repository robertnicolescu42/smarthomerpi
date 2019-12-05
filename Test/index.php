<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The HTML5 Herald</title>
  <meta name="description" content="The HTML5 Herald">
  <meta name="author" content="SitePoint">

  <link rel="stylesheet" href="css/styles.css?v=1.0">

</head>

<body>
<?php
/*
    $command = escapeshellcmd('python led.py');
    $output = shell_exec($command);
    echo $output;
*/
system("gpio -g mode 15 out");
system("gpio -g write 15 1"); //red led

system("gpio -g mode 16 out");
system("gpio -g write 16 1"); //yellow led

system("gpio -g mode 18 out");
system("gpio -g write 18 1"); //green led

system("gpio -g mode 22 out");
system("gpio -g write 22 1"); //white led

system("gpio -g write 15 0");
system("gpio -g write 16 0");
system("gpio -g write 18 0");
system("gpio -g write 22 0");

/*
    $command = escapeshellcmd('i2cdetect -l');
    $output = shell_exec($command);
    echo $output;
*/
    echo "Abc";
?>
</body>
</html>