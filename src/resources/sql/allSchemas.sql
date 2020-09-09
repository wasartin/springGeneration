CREATE TABLE account(
	account_email VARCHAR(50) NOT NULL,
	account_id VARCHAR(80),
	account_type CHAR(10),
	PRIMARY KEY(account_email)
);

CREATE TABLE food(
	fid INT NOT NULL AUTO_INCREMENT,
	fname VARCHAR(80),
	protein INT,
	carb INT,
	fat INT,
	calorie INT,
	price DOUBLE,
	category varchar(80),
	located INT NOT NULL,
	rating DOUBLE DEFAULT 0,
	rated INT DEFAULT 0,
	PRIMARY KEY(fid),
	FOREIGN KEY(located) REFERENCES restaurant(restaurant_id)
);

ALTER TABLE food AUTO_INCREMENT=0;

CREATE TABLE favorites(
	favorites_id INT NOT NULL AUTO_INCREMENT,
	account_id VARCHAR(50),
	fid INT NOT NULL,
	PRIMARY KEY(favorites_id),
	FOREIGN KEY(account_id) REFERENCES account(acount_id),
	FOREIGN KEY(fid) REFERENCES food(fid)
);

ALTER TABLE favorites AUTO_INCREMENT=0;

CREATE TABLE restaurant(
	restaurant_id INT NOT NULL AUTO_INCREMENT,
	restaurant_name VARCHAR(50),
	last_updated DATE,
	PRIMARY KEY(restaurant_id)
);

ALTER TABLE restaurant AUTO_INCREMENT=0;

CREATE TABLE ticket(
	ticket_id INT NOT NULL AUTO_INCREMENT,
	account_id VARCHAR(50),
	admin_id VARCHAR(50),
	date_assigned TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	text VARCHAR(300),
	category VARCHAR(30),
	PRIMARY KEY(ticket_id),
	FOREIGN KEY(account_id) REFERENCES account(account_email)  ON DELETE CASCADE,
	FOREIGN KEY(admin_id) REFERENCES account(account_email)  ON DELETE CASCADE
);

ALTER TABLE ticket AUTO_INCREMENT=0;