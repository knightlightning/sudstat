<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link rel="shortcut icon" type="image/png" href="/favicon.png" />

<link
	href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css"
	rel="stylesheet"
	integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
	crossorigin="anonymous">
<link rel="stylesheet" type="text/css" href="/css/navbar.css">
<link rel="stylesheet" type="text/css" href="/css/adm.css">

<title>Администрирование</title>
</head>
<body>
    <?php include("navbar.php"); ?>
        
    <div class="main-content">
		<div class="myheader">
			<div class="checkbox">
				<label><input type="checkbox" id="importOblsudData" checked>Импортировать данные областного суда</label>
				(<a href="file://///sudstat.omsksud.ru/judges-xml/obl/">\\sudstat.omsksud.ru\judges-xml\obl\</a>)
			</div>
			<div class="checkbox">
				<label><input type="checkbox" id="importRaisudData" checked>Импортировать данные районных судов</label>
				(<a href="file://///sudstat.omsksud.ru/judges-xml/rai/">\\sudstat.omsksud.ru\judges-xml\rai\</a>)
			</div>
			<div class="checkbox">
				<label><input type="checkbox" id="deleteInputFiles">Удалять успешно обработанные файлы</label>
			</div>
			<button type="button" id="import" class="btn btn-primary">Импортировать</button>
			<div class="myborder"></div>
		</div>
		<div id="myprogress" class="mylog"></div>
	</div>

	<script	src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
	<script
		src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
		integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
		crossorigin="anonymous"></script>
	<script src="/js/common.js"></script>
	<script src="/js/sse.js"></script>
	<script src="/js/judges-adm.js"></script>
</body>
</html>
