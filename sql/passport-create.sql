USE passport;

CREATE TABLE job_places (
	ID INT NOT NULL AUTO_INCREMENT,
	name TEXT CHARACTER SET UTF8 NOT NULL,
	PRIMARY KEY (ID)
);

CREATE TABLE judges (
	ID INT NOT NULL AUTO_INCREMENT,
	surname TEXT CHARACTER SET UTF8 NOT NULL,
	name TEXT CHARACTER SET UTF8 NOT NULL,
	patron TEXT CHARACTER SET UTF8 NOT NULL,
	citizenship TEXT CHARACTER SET UTF8,
	birthplace TEXT CHARACTER SET UTF8 NOT NULL,
	birthdate DATE NOT NULL,
	job_place_id INT NOT NULL,
	job_position TEXT CHARACTER SET UTF8 NOT NULL,
	job_acceptance_day DATE NOT NULL,
	qualifier_class_name TEXT CHARACTER SET UTF8,
	qualifier_class_reason TEXT CHARACTER SET UTF8,
	qualifier_class_date DATE,
	assignment_order TEXT CHARACTER SET UTF8 NOT NULL,
	assignment_date DATE NOT NULL,
	previous_judge_exp_years INT NOT NULL,
	previous_judge_exp_months INT NOT NULL,
	previous_judge_exp_days INT NOT NULL,
	previous_law_exp_years INT NOT NULL,
	previous_law_exp_months INT NOT NULL,
	previous_law_exp_days INT NOT NULL,
	avatar VARCHAR(64) CHARACTER SET UTF8,
	upload_date DATE NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY (job_place_id) REFERENCES job_places(ID)
);

CREATE TABLE academic_degrees (
	ID INT NOT NULL AUTO_INCREMENT,
	judge_id INT NOT NULL,
	name TEXT CHARACTER SET UTF8 NOT NULL,
	order_text TEXT CHARACTER SET UTF8,
	order_date DATE NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY (judge_id) REFERENCES judges(ID)
);

CREATE TABLE awards (
	ID INT NOT NULL AUTO_INCREMENT,
	judge_id INT NOT NULL,
	name TEXT CHARACTER SET UTF8 NOT NULL,
	certificate_type TEXT CHARACTER SET UTF8,
	certificate_number TEXT CHARACTER SET UTF8 NOT NULL,
	certificate_date DATE NOT NULL,
	PRIMARY KEY (ID),
	FOREIGN KEY (judge_id) REFERENCES judges(ID)
);

CREATE TABLE educations (
	ID INT NOT NULL AUTO_INCREMENT,
	judge_id INT NOT NULL,
	school TEXT CHARACTER SET UTF8 NOT NULL,
	type TEXT CHARACTER SET UTF8,
    graduation_date DATE NOT NULL,
    specialization TEXT CHARACTER SET UTF8,
    qualification TEXT CHARACTER SET UTF8,
	PRIMARY KEY (ID),
	FOREIGN KEY (judge_id) REFERENCES judges(ID)
);

CREATE TABLE job_history (
	ID INT NOT NULL AUTO_INCREMENT,
	judge_id INT NOT NULL,
	place TEXT CHARACTER SET UTF8 NOT NULL,
	city TEXT CHARACTER SET UTF8,
	position TEXT CHARACTER SET UTF8,
	acceptance_date DATE NOT NULL,
	discharge_date DATE,
	PRIMARY KEY (ID),
	FOREIGN KEY (judge_id) REFERENCES judges(ID)
);
