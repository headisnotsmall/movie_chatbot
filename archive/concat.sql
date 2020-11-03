--有中文的電影評分排序

SELECT original_title, title_tw, year, director, name, avg_vote FROM public.movies
JOIN casts on movies.imdb_title_id = casts.imdb_title_id
JOIN names on casts.imdb_name_id = names.imdb_name_id
LEFT JOIN movies_tw on movies.imdb_title_id = movies_tw.imdb_title_id
WHERE votes > 5000 and ordering = 1 and title_tw is not null
ORDER BY avg_vote DESC

CREATE TABLE casts(
	imdb_title_id varchar(20),
	ordering integer,
	imdb_name_id varchar(20)
);

CREATE TABLE movies(
	imdb_title_id varchar(20),
	title varchar(200),
	original_title varchar(200),
	year integer,
	duration integer,
	director varchar(100),
	avg_vote real,
	votes integer
);

CREATE TABLE movie_tw(
	imdb_title_id varchar(20),
	title_tw varchar(100)
);

CREATE TABLE names(
	imdb_name_id varchar(20),
	name varchar(200)
)