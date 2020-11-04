from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base # model's basis
Base = declarative_base()
engine = create_engine('postgresql://scott:tiger@localhost:5432/mydatabase')
Base.metadata.create_all()