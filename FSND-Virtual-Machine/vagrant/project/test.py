import psycopg2

def output():
    a = psycopg2.connect(database="news")
    b = a.cursor()
    b.execute("select * from articles")
    print(b.fetchall())
    a.close()

output()
