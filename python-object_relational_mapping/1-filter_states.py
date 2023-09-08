#import of mysqldb module to make the codes work
import MySQLdb


  #database connnection
database = MySQLdb.connect(host="localhost", user="root", passwd="ifetoye1990", db="hbtn_0e_0_usa")

cur = database.cursor()

cur.execute("SELECT * FROM states WHERE name=%s, (N) ORDER BY states.id ASC")

states = cur.fetchall()

"""for state in states:
    print(state)

cur.close()
database.close()"""