--有中文的電影評分排序

SELECT original_title, tw_title, year, director, name, avg_vote FROM public.movies
JOIN casts on movies.imdb_title_id = casts.imdb_title_id
JOIN names on casts.imdb_name_id = names.imdb_name_id
LEFT JOIN tw_movie on movies.imdb_title_id = tw_movie.imdb_title_id
WHERE votes > 5000 and ordering = 1 and tw_title is not null
ORDER BY avg_vote DESC