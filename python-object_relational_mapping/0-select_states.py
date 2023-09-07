#import of mysqldb module to make the codes work
import MySQLdb


#database connnection
database = MySQLdb.connect(host="localhost", user="sqluser", passwd="password", db="hbtn_0e_0_usa")

cur = database.cursor()

sel = cur.execute("SELECT * FROM states")

