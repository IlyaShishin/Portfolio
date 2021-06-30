create table if not exists Genre (
	id serial primary key,
	name text not null
);

create table if not exists Performer (
	id serial primary key,
	name text not null
);

create table if not exists GenrePerformer (
	id serial primary key,
	genre_id integer not null references Genre(id),
	performer_id integer not null references Performer(id)
);

create table if not exists Album (
	id serial primary key,
	name text not null,
	year_of_issue integer not null
);

create table if not exists AlbumPerformer (
	id serial primary key,
	album_id integer not null references Album(id),
	performer_id integer not null references Performer(id)
);

create table if not exists Song (
	id serial primary key,
	name text not null,
	duration integer not null,
	album_id integer not null references Album(id) 
);

create table if not exists Collection (
	id serial primary key,
	name text not null,
	year_of_issue integer not null 
);

create table if not exists SongCollection (
	id serial primary key,
	collection_id integer not null references Collection(id),
	song_id integer not null references Song(id)
);