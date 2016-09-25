import MySQLdb

db = MySQLdb.connect(host = "localhost",user = "<username>",passwd = "<password>",db = "<database_name>")

cur = db.cursor()
cur.execute("SELECT * FROM <table_name>")

for row in cur.fetchall():
        print row[1]


db.close()

