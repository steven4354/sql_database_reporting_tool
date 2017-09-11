import psycopg2

def output():
    a = psycopg2.connect(database="news")
    b = a.cursor()
    b.execute('''
    select *,
        case
        when path like 'trouble.for.trouble' then 'Trouble for troubled troublemakers'
        end
    group by
        path
    from orderedpath
    ;
    ''')
    print(b.fetchall())
    a.close()

output()

 Bad things gone, say good people
 Balloon goons doomed
 Bears love berries, alleges bear
 Candidate is jerk, alleges rival
 Goats eat Google's lawn
 Media obsessed with bears
 Trouble for troubled troublemakers
 There are a lot of bears
