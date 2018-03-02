USE sudstat;

CREATE TABLE courts(
	ID INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(128) CHARACTER SET UTF8 NOT NULL,
	PRIMARY KEY (ID)
);

CREATE TABLE judges(
	court_id INT NOT NULL,
	ext_id INT NOT NULL,
	name TEXT CHARACTER SET UTF8,
	PRIMARY KEY (ext_id, court_id),
	FOREIGN KEY (court_id) REFERENCES courts(ID)
);

CREATE TABLE adm_stat_types(
	ID INT NOT NULL,
	col_number INT NOT NULL,
	description TEXT CHARACTER SET UTF8,
	PRIMARY KEY (ID)
);

CREATE TABLE civ_stat_types(
	ID INT NOT NULL,
	col_number INT NOT NULL,
	description TEXT CHARACTER SET UTF8,
	PRIMARY KEY (ID)
);

CREATE TABLE crim_stat_types(
	ID INT NOT NULL,
	col_number INT NOT NULL,
	description TEXT CHARACTER SET UTF8,
	PRIMARY KEY (ID)
);

CREATE TABLE adm_charge(
	year INT NOT NULL,
	court_id INT NOT NULL,
	modification DATE NOT NULL,
	PRIMARY KEY (year, court_id),
	FOREIGN KEY (court_id) REFERENCES courts(ID)
);

CREATE TABLE civ_charge(
	year INT NOT NULL,
	court_id INT NOT NULL,
	modification DATE NOT NULL,
	PRIMARY KEY (year, court_id),
	FOREIGN KEY (court_id) REFERENCES courts(ID)
);

CREATE TABLE crim_charge(
	year INT NOT NULL,
	court_id INT NOT NULL,
	modification DATE NOT NULL,
	PRIMARY KEY (year, court_id),
	FOREIGN KEY (court_id) REFERENCES courts(ID)
);

CREATE TABLE adm_charge_data(
	charge_year INT NOT NULL,
	charge_court_id INT NOT NULL,
	judge_ext_id INT NOT NULL,
	judge_court_id INT NOT NULL,
	stat_type_id INT NOT NULL,
	data INT,
	PRIMARY KEY (charge_year, charge_court_id, judge_ext_id, stat_type_id),
	FOREIGN KEY (charge_year, charge_court_id) REFERENCES adm_charge(year, court_id),
 	FOREIGN KEY (judge_ext_id, judge_court_id) REFERENCES judges(ext_id, court_id),
	FOREIGN KEY (stat_type_id) REFERENCES adm_stat_types(ID)
);

CREATE TABLE civ_charge_data(
	charge_year INT NOT NULL,
	charge_court_id INT NOT NULL,
	judge_ext_id INT NOT NULL,
	judge_court_id INT NOT NULL,
	stat_type_id INT NOT NULL,
	data INT,
	PRIMARY KEY (charge_year, charge_court_id, judge_ext_id, stat_type_id),
	FOREIGN KEY (charge_year, charge_court_id) REFERENCES civ_charge(year, court_id),
 	FOREIGN KEY (judge_ext_id, judge_court_id) REFERENCES judges(ext_id, court_id),
	FOREIGN KEY (stat_type_id) REFERENCES civ_stat_types(ID)
);

CREATE TABLE crim_charge_data(
	charge_year INT NOT NULL,
	charge_court_id INT NOT NULL,
	judge_ext_id INT NOT NULL,
	judge_court_id INT NOT NULL,
	stat_type_id INT NOT NULL,
	data INT,
	PRIMARY KEY (charge_year, charge_court_id, judge_ext_id, stat_type_id),
	FOREIGN KEY (charge_year, charge_court_id) REFERENCES crim_charge(year, court_id),
 	FOREIGN KEY (judge_ext_id, judge_court_id) REFERENCES judges(ext_id, court_id),
	FOREIGN KEY (stat_type_id) REFERENCES crim_stat_types(ID)
);

-- CREATE TABLE periods(
-- 	ID INT NOT NULL AUTO_INCREMENT,
-- 	year INT NOT NULL,
-- 	quarter ENUM('first', 'second', 'third', 'fourth') NOT NULL,
-- 	PRIMARY KEY (year, quarter)
-- );

CREATE TABLE stat_types(
	ID INT NOT NULL AUTO_INCREMENT,
	column_num INT NOT NULL,
	type VARCHAR(128) CHARACTER SET UTF8 NOT NULL,
	PRIMARY KEY (ID)
);

CREATE TABLE stat_data(
	stat_type_id INT NOT NULL,
	year INT NOT NULL,
	quarter ENUM('first', 'second', 'third', 'fourth') NOT NULL,
	data VARCHAR(64) CHARACTER SET UTF8 NOT NULL,
	PRIMARY KEY (stat_type_id, year),
	FOREIGN KEY (stat_type_id) REFERENCES stat_types(ID)
);

INSERT INTO stat_types (column_num, type)
VALUES
	(1, 'RAI_SUMMARY_ADM'),
	(2, 'RAI_SUMMARY_CIV'),
	(3, 'RAI_SUMMARY_CRIM'),
	(4, 'MIR_CHARGE');
	
INSERT INTO stat_data
VALUES
	(1, 2017, 'third', 'test1.pdf'),
	(2, 2017, 'third', 'test1.pdf'),
	(3, 2017, 'third', 'test1.pdf'),
	(4, 2017, 'third', 'test1.pdf'),
	(1, 2016, 'fourth', 'test1.pdf'),
	(2, 2016, 'fourth', 'test1.pdf'),
	(3, 2016, 'fourth', 'test1.pdf'),
	(4, 2016, 'fourth', 'test1.pdf'),
	(1, 2015, 'fourth', 'test1.pdf'),
	(2, 2015, 'fourth', 'test1.pdf'),
	(3, 2015, 'fourth', 'test1.pdf'),
	(4, 2015, 'fourth', 'test1.pdf');

INSERT INTO courts (name)
VALUES
	('Кировский районный суд'),
    ('Куйбышевский районный суд'),
    ('Ленинский районный суд'),
    ('Октябрьский районный суд'),
    ('Первомайский районный суд'),
    ('Советский районный суд'),
    ('Центральный районный суд'),
    ('Азовский районный суд'),
    ('Большереченский районный суд'),
    ('Большеуковский районный суд'),
    ('Горьковский районный суд'),
    ('Знаменский районный суд'),
    ('Исилькульский городской суд'),
    ('Калачинский городской суд'),
    ('Колосовский районный суд'),
    ('Кормиловский районный суд'),
    ('Крутинский районный суд'),
    ('Любинский районный суд'),
    ('Марьяновский районный суд'),
    ('Москаленский районный суд'),
    ('Муромцевский районный суд'),
    ('Называевский городской суд'),
    ('Нижнеомский районный суд'),
    ('Нововаршавский районный суд'),
    ('Одесский районный суд'),
    ('Оконешниковский районный суд'),
    ('Омский районный суд'),
    ('Павлоградский районный суд'),
    ('Полтавский районный суд'),
    ('Русско-Полянский районный суд'),
    ('Саргатский районный суд'),
    ('Седельниковский районный суд'),
    ('Таврический районный суд'),
    ('Тарский городской суд'),
    ('Тевризский районный суд'),
    ('Тюкалинский городской суд'),
    ('Усть-Ишимский районный суд'),
    ('Черлакский районный суд'),
    ('Шербакульский районный суд');

INSERT INTO adm_stat_types
VALUES
	(1, 1,  'Остаток на начало'),
	(2, 2,  'Поступило'),
	(3, 3,  'Всего в производстве'),
	(4, 4,  'Окончено'),
	(44, 5,  'Объединено'),
	(5, 6,  'Остаток'),
	(6, 7,  'Вынесено решений'),
	(107, 8,  'В упрощённом порядке'),
	(8, 9,  'Нарушение сроков'),
	(9, 10,  '%'),
	(10, 11,  'Поступило материалов'),
	(11, 12,  'Нарушен срок принятия'),
	(12, 13,  'Отказано в принятии'),
	(13, 14,  'Возвращено'),
	(14, 15,  'Возвращено');

INSERT INTO civ_stat_types
VALUES
	(1 , 1 , 'Остаток неоконченных дел на начало отчётного периода'),
	(2 , 2 , 'Поступило дел в отчётом периоде'),
	(3 , 3 , 'Всего рассмотренно с вынесением решения'),
	(4 , 4 , 'В том числе с удовлетворением требования'),
	(5 , 5 , 'В том числе с отказом в удовлетворении требования'),
	(6 , 6 , 'Прекращено'),
	(7 , 7 , 'Оставлено без рассмотрения'),
	(8 , 8 , 'Передано в другие суды'),
	(9 , 9 , 'Всего окончено'),
	(10 , 10 , 'Объединено'),
	(11 , 11 , 'Остаток неоконченных дел на конец отчётного периода');

INSERT INTO crim_stat_types
VALUES
	(1, 1,  'Остаток неоконченных дел на начало отчётного периода'),
	(2, 2,  'Поступило дел в отчётом периоде'),
	(3, 3,  'Всего рассмотренно с вынесением приговора'),
	(4, 4,  'В том числе с прекращением дела'),
	(5, 5,  'В том числе с применением принудительных мер к невменяемым'),
	(6, 6,  'Возвращено прокурору для устранения недостатков в порядке ст.237 п.2 УПК РФ'),
	(7, 7,  'Передано по подсудности или подведомственности'),
	(8, 8,  'Всего окончено'),
	(9, 9,  'Остаток неоконченных дел на конец отчётного периода');
