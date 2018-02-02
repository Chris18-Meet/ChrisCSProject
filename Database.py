from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
if __name__ =='__main__':
    DBSession = sessionmaker()

class Emails(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)

create_all()