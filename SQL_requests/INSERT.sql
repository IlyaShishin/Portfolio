INSERT INTO Performer(name)
	VALUES('Scorpions'),
	('ACDC'),
	('Eminem'),
	('Frank Sinatra'),
	('Bob Marley'),
	('Louis Armstrong'),
	('Kenny G'),
	('Johnny Cash');

INSERT INTO Genre(name)
	VALUES('Hard Rock'),
	('Rap'),
	('Swing'),
	('Jazz'),
	('Reggae'),
	('Country Music');

INSERT INTO GenrePerformer(genre_id, performer_id)
	VALUES(1, 1),
	(1, 2),
	(2, 3),
	(3, 4),
	(4, 6),
	(4, 7),
	(5, 5),
	(6, 8),
	(4, 4);

INSERT INTO Album(name, year_of_issue)
	VALUES('Love at First Sting', 1994),
	('Highway to Hell', 1979),
	('The Marshall Mathers LP 2', 2013),
	('Trilogy: Past Present Future', 1980),
	('Natty Dread', 1974),
	('What a Wonderful World', 1967),
	('The Moment', 1998),
	('American IV: The Man Comes Around', 2002);

INSERT INTO AlbumPerformer(album_id, performer_id)
	VALUES(1, 1),
	(2, 2),
	(3, 3),
	(4, 4),
	(5, 5),
	(6, 6),
	(7, 7),
	(8, 8);

INSERT INTO Song(name, duration, album_id)
	VALUES('Still Loving You', 6.75, 1),
	('Highway to Hell', 3.5, 2),
	('Rap God', 6, 3),
	('New York, New York', 3.5, 4),
	('No woman, No cry', 4.5, 5),
	('What a Wonderful World', 2.25, 6),
	('Havana', 5.5, 7),
	('Hurt', 3.6, 8),
	('Rock You Like a Hurricane', 4.25, 1),
	('Touch Too Much', 4.5, 2),
	('The Monster', 4.25, 3),
	('Strangers In the Night', 2.5, 4),
	('One Love', 2.5, 5),
	('Blueberry Hill', 3.5, 6),
	('The Moment', 8, 7),
	('I Walk The Line', 2, 8),
	('Bad Boys Running Wild', 4, 1);

INSERT INTO Collection(name, year_of_issue)
	VALUES('Rock will never die', 2018),
	('Rap and Jazz, oh my..', 2019),
	('From USA with Love', 2020),
	('Jazz Forever', 2001),
	('For Soul', 2005),
	('Best Songs Ever', 2021),
	('Cuba and Jamaica', 2010),
	('The Song Is Not Enough', 2018);

INSERT INTO SongCollection(collection_id, song_id)
	VALUES(1, 1),
	(1, 2),
	(1, 8),
	(2, 3),
	(2, 6),
	(2, 7),
	(3, 1),
	(3, 2),
	(3, 8),
	(4, 4),
	(4, 6),
	(4, 7),
	(5, 5),
	(5, 7),
	(5, 4),
	(6, 1),
	(6, 2),
	(6, 4),
	(6, 5),
	(7, 5),
	(7, 7),
	(8, 7),
	(8, 8);