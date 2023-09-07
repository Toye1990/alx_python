#import of mysqldb module to make the codes work
import MySQLdb


  #database connnection
database = MySQLdb.connect(host="localhost", user="sqluser", passwd="password", db="hbtn_0e_0_usa")

cur = database.cursor()

cur.execute("SELECT * FROM states WHERE name=%s, (N) ORDER BY id ASC")

states = cur.fetchall()

for state in states:
    print(state)

cur.close()
database.close()