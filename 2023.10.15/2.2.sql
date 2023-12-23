drop database if exists mus_library;

create database mus_library;

use mus_library;

create table performers (
	performer_id smallint unsigned primary key auto_increment,
    performer_name varchar(50) not null unique
    );
    
create table styles (
	style_id smallint unsigned primary key auto_increment,
    style_name varchar(50) not null unique
);

create table publishers (
	publisher_id smallint unsigned primary key auto_increment,
    country varchar(50) not null
);

create table music_collections (
	collection_id smallint unsigned primary key auto_increment,
    album_title varchar(100) not null unique,
    performers smallint unsigned not null,
    output_date date not null,
    styles smallint unsigned not null,
    publishers smallint unsigned not null,
    constraint performers
		foreign key (performers) references performers (performer_id)
        on delete cascade
		on update cascade,
	constraint styles
		foreign key (styles) references styles (style_id)
        on delete cascade
        on update cascade,
	constraint publishers
		foreign key (publishers) references publishers (publisher_id)
        on delete cascade
        on update cascade
);

create table songs (
	song_id smallint primary key auto_increment,
    song_title varchar(50) not null,
    performers smallint unsigned,
    styles smallint unsigned not null,
    duration decimal (5, 2) not null,
    collection smallint unsigned not null,
    constraint music_collection
		foreign key (collection) references music_collection (collection_id)
        on delete cascade
        on update cascade,
	constraint styles
		foreign key (styles) references styles (style_id)
        on delete cascade
        on update cascade,
	constraint performers
		foreign key (performers) references performers (performer_id)
        on delete restrict
        on update cascade
);
        
    