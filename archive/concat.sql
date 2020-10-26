SELECT * FROM public.movies 
WHERE YEAR > 2015 AND VOTES > 3000
ORDER BY avg_vote DESC
LIMIT 100;

SELECT * FROM public.movies
WHERE original_title like '%Jurassic%'``

SELECT original_title, tw_title, director, name, avg_vote FROM public.movies
JOIN casts on movies.imdb_title_id = casts.imdb_title_id
JOIN names on casts.imdb_name_id = names.imdb_name_id
LEFT JOIN tw_movie on movies.imdb_title_id = tw_movie.imdb_title_id
WHERE votes > 5000 and ordering = 1
LIMIT 100