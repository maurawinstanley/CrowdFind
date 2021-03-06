CREATE TABLE IF NOT EXISTS users (
	id int(1) NOT NULL AUTO_INCREMENT,
	email varchar(40) NOT NULL,
	zipCode int(1) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS items (
	id int(1) NOT NULL AUTO_INCREMENT,
	userid int(1) NOT NULL,
	name varchar(40) NOT NULL,
	description varchar(100) NOT NULL,
	location varchar(100) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (userid) REFERENCES users(id)
);
