import psycopg2
from const import PASSWORD
from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base # model's basis
from sqlalchemy.orm import sessionmaker, scoped_session, relationship

# from main import fetch, fetch_data, get_my_ip, run_main
from main import run_main, run_main_

# from dataclasses import dataclass
from datetime import datetime


# create a connection
# conn = psycopg2.connect(
#     host = "127.0.0.1",
#     port = "5432",
#     database = "demo1",
#     user = "admin1",
#     password = PASSWORD,
# )
# print(conn)

engine = create_engine("sqlite:///mosru_data.db") # can create the file anywhere
Base = declarative_base(bind=engine) # bind helps metadata to use engine
# make a session factory and bind with the engine
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

class MosruDataset(Base):
    __tablename__ = 'datasets_2'
    id = Column(Integer, primary_key=True)
    id_from_mosru = Column(Integer)
    caption = Column(String)
    categoryid = Column(Integer)
    # publishdate = Column(DateTime)
    publishdate = Column(String)
    # fulldescription = Column(String)
    keywords = Column(String)
    containsgeodata = Column(Boolean)
    isforeign = Column(Boolean)
    isarchive = Column(Boolean)
    isnew = Column(Boolean)
    # lastupdatedate = Column(DateTime)
    lastupdatedate = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    # rubric = Column(Integer, ForeignKey("rubrics_2.id"), nullable=False)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.caption!r})" # representation !r
    def __repr__(self):
        return str(self)

class Rubric(Base):
    __tablename__ = 'rubrics_2'
    id = Column(Integer, primary_key=True)
    text = Column(String(32), nullable=False, unique=True, default='UNIVERSAL_RUBRIC')
    
if __name__ == '__main__':
    res = run_main_()
    print('result!', type(res))
    try:
        print(res.keys())
    except:
        pass

if __name__ == '__main__':
    Base.metadata.create_all()
    if res:
        session = Session()
        data = res['Items']
        for i in range(len(data)):
            data_input = data[i]
            data_list = ['Id', 'Caption', 'CategoryId','PublishDate',
                         'Keywords','ContainsGeodata','IsForeign','IsArchive',
                         'IsNew','LastUpdateDate']
            param = [data_input[el] for el in data_list]
            dataset_1 = MosruDataset(id_from_mosru=param[0], caption=param[1],
                                     categoryid=param[2],publishdate=param[3],keywords=param[4],
                                     containsgeodata=param[5], isforeign=param[6],
                                     isarchive=param[7],isnew=param[8], lastupdatedate=param[9])
            session.add(dataset_1)
            session.commit()
        session.close()

    # data_1 = res['Items'][1]
    # # print(data_1)
    # # data_list = [data_1['Id'], data_1['Caption'], data_1['CategoryId'],data_1['PublishDate'],
    # #  data_1['Keywords'],data_1['ContainsGeodata'],
    # #  data_1['IsForeign'],data_1['IsArchive'],data_1['IsNew'],data_1['LastUpdateDate']]
    # # for d in data_list:
    # #     print(d)
    # dataset_1 = MosruDataset(id_from_mosru=data_1['Id'],caption=data_1['Caption'],categoryid=data_1['CategoryId'],
    #                          publishdate=data_1['PublishDate'],keywords=data_1['Keywords'],
    #                          containsgeodata=data_1['ContainsGeodata'],isforeign=data_1['IsForeign'],isarchive=data_1['IsArchive'],
    #                          isnew=data_1['IsNew'],lastupdatedate=data_1['LastUpdateDate'])
    # # dataset_1 = MosruDataset(caption='hgkjhkhg')
    # session = Session()
    # session.add(dataset_1)
    # session.commit()
    # session.close()


