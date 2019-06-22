CREATE TABLE artist
(
	name varchar(20) not null,
	company varchar(20),
	primary key(name)
)	ENGINE=INNODB;

CREATE TABLE album
(
	name varchar(20) not null,
	year int,
	artist varchar(20),
	primary key(name),
	foreign key (artist) references artist(name)
)	ENGINE=INNODB;

CREATE TABLE series
(
	name varchar(20) not null,
	type varchar(20),
	primary key(name)
)	ENGINE=INNODB;

CREATE TABLE song
(
	ID int AUTO_INCREMENT PRIMARY KEY,
	name varchar(100) not null,
	link varchar(11) not null,
	artist varchar(20),
	album varchar(20),
	series varchar(20),
	time int not null,
	foreign key (artist) references artist(name),
	foreign key (album) references album(name),	
	foreign key (series) references series(name)
)	ENGINE=INNODB;

CREATE TABLE playlist
(
	Sequence int AUTO_INCREMENT PRIMARY KEY,
	song_id int not null,
	foreign key (song_id) references song(ID)
)	ENGINE=INNODB;
