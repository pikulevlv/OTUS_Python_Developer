from datetime import datetime
from loguru import logger
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy.ext.declarative import declarative_base # model's basis

#make engine and Base
engine = create_engine("sqlite:///mosru_data.db")
Base = declarative_base(bind=engine)

class Rubric(Base):
    """Rubric"""
    __tablename__ = 'rubrics_1'
    id = Column(Integer, primary_key=True, unique=True)
    text = Column(String(64), nullable=False, unique=True, default='UNIVERSAL_RUBRIC')

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.text!r})"

    def __repr__(self):
        return str(self)

class MosruDataset(Base):
    """Dataset class"""
    __tablename__ = 'datasets_1'
    id = Column(Integer, primary_key=True)
    id_from_mosru = Column(Integer)
    caption = Column(String)
    categoryid = Column(Integer)
    publishdate = Column(String)
    keywords = Column(String)
    containsgeodata = Column(Boolean)
    isforeign = Column(Boolean)
    isarchive = Column(Boolean)
    isnew = Column(Boolean)
    lastupdatedate = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    rubric = Column(Integer, ForeignKey("rubrics_1.id"), nullable=True)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.caption!r})" # representation !r
    def __repr__(self):
        return str(self)

