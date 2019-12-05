<?php
$conectare = mysqli_connect('localhost','marian','marian','bazabazei');

if(!$conectare){
    die(mysqli_connect_error());
}
