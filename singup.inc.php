<?php
require 'conectare.php';

if(!empty($_POST['Name'])&& !empty($_POST['Password'])&& !empty($_POST['Email'])&& !empty($_POST['Username'])&&
    isset($_POST['Name'])&& isset($_POST['Password'])&& isset($_POST['Email'])&& isset($_POST['Username']))
{

    $username = strtolower($_POST['Username']);
    $password = $_POST['Password'];
    $email = $_POST['Email'];
    $name = $_POST['Name'];
    $password_hashed = password_hash($password, PASSWORD_DEFAULT);

    $sql = "SELECT Username from users where Username='$username'";
    $result = mysqli_query($conectare, $sql);
    $check = mysqli_num_rows($result);

    if($check>0){
        header("Location:indexsingup.php?Info=exista");
        die();
    } else{

    $sql = "INSERT INTO  users(Username,Password,Email,Name) VALUES ('$username' , '$password_hashed' , '$email' , '$name')";

    $result = mysqli_query($conectare, $sql);
    header("LOCATION:indexsingup.php?Info=ok");
    }
}
else {
    header("LOCATION:indexsingup.php?Info=eroare");
}