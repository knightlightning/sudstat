<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="shortcut icon" type="image/png" href="favicon.png"/>

        <link href="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="css/navbar.css">
        <link rel="stylesheet" type="text/css" href="css/courts-stat.css">
        <link rel="stylesheet" type="text/css" href="css/bootstrap-treeview.css">

        <title>Статистика</title>
    </head>
    <body>
        <?php include("navbar.php"); ?>

        <div class="main-content container-fluid">
            <div class="stat-container">
                <div id="tree"></div>
            </div>
            <div class="details-container">
                <object class="details" data="" type="application/pdf">
                    <!--<a href="data/test.pdf">test.pdf</a>-->
                </object>
            </div>
        </div>

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/moment.min.js"></script>
        <script src="js/bootstrap-treeview.js"></script>
        <script src="js/common.js"></script>
        <script src="js/courts-stat.js"></script>
    </body>
</html>
