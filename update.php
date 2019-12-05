<?php
session_start();
require 'conectare.php';


$itemp = $_POST['inputtemperature'];
$ihumidity = $_POST['inputhumidity'];
$ipressure= $_POST['inputpressure'];
$ilight= $_POST['inputlight'];

$sql="update ledstates set yellowLed='$ihumidity'";
$sql2 ="UPDATE ledstates SET redLed='$itemp'";
$sql3 ="UPDATE ledstates SET greenLed='$ipressure'";
$sql4 ="UPDATE ledstates SET whiteLed='$ilight'";

$result2=mysqli_query($conectare,$sql2);
$result=mysqli_query($conectare, $sql);
$result3=mysqli_query($conectare,$sql3);
$result4=mysqli_query($conectare,$sql4);


header("Location:indexadmin.php");