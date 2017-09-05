# "Database code" for the DB Forum.

import psycopg2

def get_posts():
 """Return all posts from the 'database', most recent first."""
 a = psycopg2.connect(database="forum")
 b = a.cursor()
 b.execute("select content, time from posts order by time desc")
 return b.fetchall()
 a.close()

def add_post(content):
 """Add a post to the 'database' with the current timestamp."""
 a = psycopg2.connect(database="forum")
 b = a.cursor()
 b.execute("insert into posts values (%s)", (content,))
 a.commit()
 a.close()
