"""import of sqlalchemy module to make the codes work"""
import sqlalchemy
from sqlalchemy import create_engine
from model_state import Base, State


username = "root"
password = "ifetoye1990"
database = "hbtn_0e_6_usa"

path = "mysql+mysqldb://{}:{}".format(username, password, database)

dataconnect = create_engine(path, echo=True)
connection = dataconnect.connect()

connection.execute("SELECT * FROM states")