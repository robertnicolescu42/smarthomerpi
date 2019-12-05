<?php
session_start();
require 'conectare.php';


if (isset($_POST['Username'])&& !empty($_POST['Username'])&& isset($_POST['Password'])&&!empty($_POST['Password']))
{
    $username = strtolower($_POST['Username']);
    $password = $_POST['Password'];
    $sql = "SELECT * FROM users Where Username='$username'";
    $result = mysqli_query($conectare,$sql);
    $row = $result->fetch_assoc();
    $hash = $row['Password'];

    $check = password_verify($password,$hash);

    if($check == 0){
        header("Location:index.php?Info=gresit");
        die();
    } else {
        $sql = "SELECT * FROM users where Username='$username' AND Password ='$hash'";
        $result = mysqli_query($conectare, $sql);

        }
    if ($username == 'admin') {
        header("Location:indexadmin.php");
        $_SESSION['userid'] = $row['userid'];
        $_SESSION['Name'] = $row['Name'];
        $_SESSION['Username'] = $row['Username'];
        $_SESSION['Password'] = $row['Password'];}
    else {
            if (!$row = $result->fetch_assoc()) {
                echo 'Parola sau usernameul nu merge';
            } else {
                $_SESSION['userid'] = $row['userid'];
                $_SESSION['Name'] = $row['Name'];
                $_SESSION['Username'] = $row['Username'];
                $_SESSION['Password'] = $row['Password'];
            }
            header("Location:index2.php");


        }

}


