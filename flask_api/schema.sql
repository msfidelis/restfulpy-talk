CREATE TABLE posts IF NOT EXISTS(
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	user CHAR(100),
	message CHAR(140)
);
