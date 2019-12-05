
<?php
require 'conectare.php';
session_start();

?>
<!doctype html>
<html lang="en">
<head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	 <link href="images/favicon.ico" rel="icon" type="image/x-icon" />



    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" type="text/css" href="css/arta.css">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.3.1/css/all.css" integrity="sha384-mzrmE5qonljUremFsqc01SB46JvROS7bZs3IO2EmfFsd15uHvIt+Y8vEf7N7fWAU" crossorigin="anonymous">
    <link href="/your-path-to-fontawesome/css/fontawesome.css" rel="stylesheet">
    <link href="/your-path-to-fontawesome/css/brands.css" rel="stylesheet">
    <link href="/your-path-to-fontawesome/css/solid.css" rel="stylesheet">
    <title>SmartHome with raspberry pi</title>
</head>
<body>
<!-- head-ul siteului minimalist-->
<div class="container-fluid bg-dark">
    <div class="row">
        <div class="col"></div>
         <div class="col ml-3 color-fa-home">
                <span><i class="fas fa-home fa-3x"></i></span>
         </div>
    <div class="col"></div>
    </div>
</div>

<?php
if(!isset($_SESSION['userid'])){

    echo ' <div class="container-fluid">
    <div class="row">
        <div class="col"></div>

        <div class="col">
            <div class="d-flex justify-content-center h-100">
                <div class="card" style="height: 313px;">
                    <div class="card-header bg-dark">
                        <h3>Sign In</h3>
                    </div>
                    <div class="card-body bg-dark">
                       <!-- button username -->
                        <form action="singin.inc.php" method="post">
                            <div class="input-group form-group">
                                <div class="input-group-prepend">
                                    <span class="input-group-text"><i class="fas fa-user"></i></span>
                                </div>
                                <input type="text" class="form-control" name="Username" placeholder="Username">
                                <!-- button password-->
                            </div>
                            <div class="input-group form-group">
                                <div class="input-group-prepend">
                                    <span class="input-group-text"><i class="fas fa-key"></i></span>
                                </div>
                                <input type="password" class="form-control" name="Password" placeholder="Password">
                            </div>

                            <div class="row align-items-center remember">
                                <input type="checkbox">Remember Me
                            </div>
                            <div class="form-group">
                                <input type="submit" value="Login" class="btn float-right login_btn">
                            </div>
                        </form>
                    </div>
                    <div class="card-footer bg-dark mb-5">
                        <div class="d-flex justify-content-center flex-wrap links">';
                             if(isset($_GET['Info'])&& $_GET['Info']=='gresit') {
                                 echo '<p class="text-danger display-6" >Your wrong password or username!</p>';}
                            echo'Don\'t have an account?<a href="indexsingup.php">Sign Up</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    <div class="col"></div>
    </div>
</div>
';

}
else {
    echo '<form action="logout.inc.php" method="post">
    <input type="submit" value="Log Out"> 
    </form>
    ';
}


?>














<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>