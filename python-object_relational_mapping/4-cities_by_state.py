#import of mysqldb module to make the codes work
import MySQLdb
import sys
  #database connnection

def search(username, password, database):

 connect = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "ifetoye1990",
    db = "hbtn_0e_0_usa"
  )

 connect.execute("INSERT INTO states (name) values (%s)", state)
 connection = connect.cursor()
 query = "SELECT * FROM cities ORDER BY id ASC"
 connection.execute(query)
 totals = connection.fetchall()
 
 for row in totals:
     print(row)
 query.connect()
 connect.close()

if __name__ =="__main__()":
     username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
search(username, password, database, state_name)

