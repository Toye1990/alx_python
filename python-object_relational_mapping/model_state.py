"""import of mysqldb module to make the codes work"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Numeric

Base = declarative_base()
"""base instance imported"""
class state(Base):
    """class instance to use"""
    __table__= "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name