CREATE TABLE favorites(
	favorites_id INT NOT NULL AUTO_INCREMENT,
	account_id VARCHAR(50),
	fid INT NOT NULL,
	PRIMARY KEY(favorites_id),
	FOREIGN KEY(account_id) REFERENCES account(acount_email),
	FOREIGN KEY(fid) REFERENCES food(fid)
);

ALTER TABLE favorites AUTO_INCREMENT=0;