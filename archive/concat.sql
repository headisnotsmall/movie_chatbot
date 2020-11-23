--有中文的電影評分排序

SELECT original_title, title_tw, year, director, name, avg_vote FROM public.movies
JOIN casts on movies.imdb_title_id = casts.imdb_title_id
JOIN names on casts.imdb_name_id = names.imdb_name_id
LEFT JOIN movies_tw on movies.imdb_title_id = movies_tw.imdb_title_id
WHERE votes > 5000 and ordering = 1 and title_tw is not null
ORDER BY avg_vote DESC

CREATE TABLE casts(
	id integer,
	imdb_title_id varchar(20),
	ordering integer,
	imdb_name_id varchar(20)
);

CREATE TABLE movies(
	id integer,
	imdb_title_id varchar(20),
	title varchar(200),
	original_title varchar(200),
	year integer,
	duration integer,
	director varchar(100),
	avg_vote real,
	votes integer
);

CREATE TABLE movies_tw(
	id integer,
	imdb_title_id varchar(20),
	title_tw varchar(100)
	R1 varchar(20),
	R2 varchar(20)
);

CREATE TABLE names(
	id integer,
	imdb_name_id varchar(20),
	name varchar(200)
)


INSERT INTO movies VALUES
(5826,'tt0040349','Feudin'', Fussin'' and A-Fightin''','Feudin'', Fussin'' and A-Fightin''',1948,78,'George Sherman',6.2,128),
(13346,'tt0062523','Zhenya, Zhenechka i ''Katyusha''','Zhenya, Zhenechka i ''Katyusha''',1967,85,'Vladimir Motyl',7.6,449),
(14423,'tt0065600','''Ctyri vrazdy stací, drahousku''','''Ctyri vrazdy stací, drahousku''',1971,103,'Oldrich Lipský',7.6,626),
(16019,'tt0070061','Film d''amore e d''anarchia, ovvero ''stamattina alle 10 in via dei Fiori nella nota casa di tolleranza...''','Film d''amore e d''anarchia, ovvero ''stamattina alle 10 in via dei Fiori nella nota casa di tolleranza...''',1973,124,'Lina Wertmüller',7.8,2495),
(17224,'tt0073697','''Sheba, Baby''','''Sheba, Baby''',1975,90,'William Girdler',5.8,1222),
(20880,'tt0085516','F.F.S.S., cioè: ''...che mi hai portato a fare sopra a Posillipo se non mi vuoi più bene?''','F.F.S.S., cioè: ''...che mi hai portato a fare sopra a Posillipo se non mi vuoi più bene?''',1983,98,'Renzo Arbore',6.2,272),
(22351,'tt0090354','Yo, ''El Vaquilla''','Yo, ''El Vaquilla''',1985,105,'José Antonio de la Loma Jr., José Antonio de la Loma',5.2,224),
(24483,'tt0097049','Chastnyy detektiv, ili operatsiya ''Kooperatsiya''','Chastnyy detektiv, ili operatsiya ''Kooperatsiya''',1990,94,'Leonid Gaidai',5.3,441),
(30614,'tt0119207','God Said, ''Ha!''','God Said, ''Ha!''',1998,85,'Julia Sweeney',7.1,926),
(31587,'tt0123313','Voitheia o Vengos, faneros praktor ''000''','Voitheia o Vengos, faneros praktor ''000''',1967,89,'Thanasis Vengos',8.2,1267)