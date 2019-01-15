<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="shortcut icon" type="image/png" href="favicon.png"/>

        <link href="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="css/navbar.css">
        <link rel="stylesheet" type="text/css" href="css/courts.css">
        <link rel="stylesheet" type="text/css" href="css/judges.css">
        <link rel="stylesheet" type="text/css" href="css/modal.css">

        <title>Паспорта судов</title>
    </head>
    <body>
        <?php include("navbar.php"); ?>
        <?php include("modal.php"); ?>
        
        <div class="main-content container-fluid">
            <div id="courts" class="list-group courts-panel">
                <div id="courtsList" class="panel">
                </div>
            </div>

            <div class="users-container">
                <div id="usersPanel" class="list-group users-panel">
                </div>
            </div>

            <div class="user-details-container">
                <div class="user-details">
                    <table id="judgefio">
                        <thead>
                            <tr>
                                <th class="title" colspan="2">Персональные данные</th>
                            </tr>
                        </thead>
                        <tbody>
                        </tbody>
                    </table>
                    <table id="judge-qualification">
                        <thead>
                            <tr>
                                <td class="space" colspan="2"></td>
                            </tr>
                            <tr>
                                <th class="title" colspan="2">Квалификационный класс</th>
                            </tr>
                        </thead>
                        <tbody>
                        </tbody>
                    </table>
                    <table id="judge-assignment">
                        <thead>
                            <tr>
                                <th class="space" colspan="2"></th>
                            </tr>
                            <tr>
                                <th class="title" colspan="2">Предыдущее назначение на должность</th>
                            </tr>
                        </thead>
                        <tbody>
                        </tbody>
                    </table>
                    <table id="educations">
                        <thead>
                            <tr>
                                <th class="space" colspan="2"></th>
                            </tr>
                            <tr>
                                <th class="title" colspan="2">Образование</th>
                            </tr>
                        </thead>
                        <tbody>
                        </tbody>
                    </table>
                    <table id="degrees">
                        <thead>
                            <tr>
                                <th class="space" colspan="2"></th>
                            </tr>
                            <tr>
                                <th class="title" colspan="2">Учёные степени</th>
                            </tr>
                        </thead>
                        <tbody>
                        </tbody>
                    </table>
                    <table id="awards">
                        <thead>
                            <tr>
                                <td class="space" colspan="2"></td>
                            </tr>
                            <tr>
                                <th class="title" colspan="2">Награды</th>
                            </tr>
                        </thead>
                        <tbody>
                        </tbody>
                    </table>
                </div>
                <div class="user-exp-details">
                    <table id="jobs">
                        <thead>
                            <tr>
                                <td class="title" colspan="5">Трудовая деятельность</td>
                            </tr>
                            <tr class="subtitle-top">
                                <td colspan="2">Дата</td>
                                <td rowspan="2">Место работы</td>
                                <td rowspan="2">Должность</td>
                                <td rowspan="2">Местонахождение</td>
                            </tr>
                            <tr class="subtitle-top">
                                <td>назначения</td>
                                <td>увольнения/окончания полномочий</td>
                            </tr>
                        </thead>
                        <tbody>
                        </tbody>
                    </table>
                    <table id="judge-exp">
                        <thead>
                            <tr>
                                <td class="space" colspan="4"></td>
                            </tr>
                            <tr>
                                <td class="title" colspan="4">Стаж на текущую дату (<?php echo date("d.m.Y"); ?>)</td>
                            </tr>
                            <tr class="subtitle-top">
                                <td></td>
                                <td>Лет</td>
                                <td>Месяцев</td>
                                <td>Дней</td>
                            </tr>
                        </thead>
                        <tbody>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>      
        
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.18.1/moment.min.js"></script>
        <script src="js/common.js"></script>
        <script src="js/judges.js"></script>
    </body>
</html>
