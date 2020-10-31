import psycopg2

# Update connection string information 
host = "localhost"
dbname = "imdb_movies"
user = "postgres"
password = "L25027"

# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3}".format(host, user, dbname, password)
conn = psycopg2.connect(conn_string) 
print("Connection established")

cursor = conn.cursor()

'''

# Drop previous table of same name if one exists
cursor.execute("DROP TABLE IF EXISTS inventory;")
print("Finished dropping table (if existed)")

# Create a table
cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
print("Finished creating table")

# Insert some data into the table
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
print("Inserted 3 rows of data")

'''

sql = '''
SELECT original_title, year, director, name, avg_vote FROM public.movies
JOIN casts on movies.imdb_title_id = casts.imdb_title_id
JOIN names on casts.imdb_name_id = names.imdb_name_id
WHERE votes > 5000 and ordering = 1
ORDER BY avg_vote DESC
'''

# Fetch all rows from table
cursor.execute(sql)
rows = cursor.fetchall()

# Print all rows

searching_name = input('Which movie do you want to know? ')

for row in rows:
    if searching_name in row[0]:
       print(
           '片名:', row[0],
           '\n年份:', row[1],
           '\n導演:', row[2],
           '\n主演:', row[3],
           '\n評分:', row[4],
           '\n---------------------'
       )

# Clean up
conn.commit()
cursor.close()
conn.close()