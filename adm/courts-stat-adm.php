<!DOCTYPE html>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="shortcut icon" type="image/png" href="/favicon.png"/>

        <link href="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="/css/navbar.css">
        <link rel="stylesheet" type="text/css" href="/css/courts-stat-adm.css">

        <title>Администрирование</title>
    </head>
    <body>
        <?php include("navbar.php"); ?>
        
        <div class="main-content container">
            <form class="form-horizontal" id="myForm">
                <div class="form-group">
                    <label class="control-label col-sm-2">Тип:</label>
                    <div class="col-sm-10">
                        <select class="form-control" id="statType">
                            <option value="RAI_SUMMARY_ADM">Показатели АДМ</option>
                            <option value="RAI_SUMMARY_CIV">Показатели ГР</option>
                            <option value="RAI_SUMMARY_CRIM">Показатели УГ</option>
                            <option value="MIR_CHARGE">Нагрузка мировых судей</option>
                        </select>
                    </div>
                </div>
                <div class="form-group">
                    <label class="control-label col-sm-2">Год:</label>
                    <div class="col-sm-10"> 
                        <select class="form-control" id="statYear">
                        </select>
                    </div>
                </div>
                <div class="form-group">
                    <label class="control-label col-sm-2">Квартал:</label>
                    <div class="col-sm-10"> 
                        <select class="form-control" id="statQuarter">
                            <option value="first">I</option>
                            <option value="second">II</option>
                            <option value="third">III</option>
                            <option value="fourth">IV</option>
                        </select>
                    </div>
                </div>
                <div class="form-group">
                    <label class="control-label col-sm-2">Файл:</label>
                    <div class="col-sm-10"> 
                        <input type="file" class="form-control" accept=".pdf" id="file">
                    </div>
                </div>
                <div class="form-group"> 
                    <div class="col-sm-offset-2 col-sm-10">
                        <button type="submit" class="btn btn-primary" disabled>Загрузить</button>
                    </div>
                </div>
            </form>
        </div>
        
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
        <script src="/js/common.js"></script>
        <script src="/js/courts-stat-adm.js"></script>
    </body>
</html>
