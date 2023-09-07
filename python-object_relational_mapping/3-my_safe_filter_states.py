#import of mysqldb module to make the codes work
import MySQLdb
import sys
  #database connnection

def search(username, password, database, state_name):

 connect = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "ifetoye1990",
    db = "hbtn_0e_0_usa"
  )
 
 connect.execute("CREATE TABLE IF NOT EXISTS states(id INT PRIMARY NOT NULL AUTO_INCREMENT, name VACHAR(255))")
 states = ("California", "Arizona", "Texas", "New York", "Nevada")
 for state in states:
   connect.execute("INSERT INTO states (name) values (%s)", state)
 connection = connect.cursor()
 base = "SELECT * FROM states WHERE name LIKE ORDER BY id ASC{}".format('%{}%'.format(state_name))
 connection.execute(base)
 totals = connection.fetchall()
 
 for row in totals:
     print(row)
 base.connect()
 connect.close()

if __name__ =="__main__()":
     username, password, database, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
search(username, password, database, state_name)

