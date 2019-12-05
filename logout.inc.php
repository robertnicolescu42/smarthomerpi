<?php
session_start();
session_destroy();

setcookie("RedOn", $_COOKIE['RedOn'] = "nesetat", time() + 60 * 60 * 24 * 5);
setcookie("YellowOn", $_COOKIE['RedOn'] = "nesetat", time() + 60 * 60 * 24 * 5);
setcookie("GreenOn", $_COOKIE['RedOn'] = "nesetat", time() + 60 * 60 * 24 * 5);
setcookie("WhiteOn", $_COOKIE['RedOn'] = "nesetat", time() + 60 * 60 * 24 * 5);
header("Location: index.php");