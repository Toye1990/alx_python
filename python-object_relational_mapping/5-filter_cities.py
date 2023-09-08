"""import of mysqldb module to make the codes work"""
import MySQLdb

def main():
 connect = MySQLdb.connect(
    host = "localhost",
    user = "root",
    passwd = "ifetoye1990",
    db = "hbtn_0e_0_usa"
    )

 cur = connect.cursor()


 query = "SELECT cities.id, cities.name FROM cities JOIN state ON cities_id WHERE state.name=%s ORDER BY cities.id ASC"
 cur.execute(query, (state_name,))

 for row in cur:
  print(row)

 cur.close()
 connect.close()

 if __name__ == "__main__":
    main()