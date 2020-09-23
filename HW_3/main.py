"""
Асинхронная работа с сетью
Цель: В этом ДЗ вы напишете скрипт.
написать скрипт, который при помощи асинхронного клиента обращается к
открытому апи (например, jsonplaceholder) и выводит оттуда информацию
создать модели для объектов, которые тянутся с открытого апи
записать вытянутые модели в БД
скрипт для стягивания данных и записи в БД реализован в асинхронном виде
Критерии оценки: у моделей есть primary_key - 1 балл
созданы все миграции - 1 балл
скрипт стягивает данные с API и складывает в БД - 1 балл
обращение к API выполняется в асинхронном виде - 1 балл
на асинхронный клиент применяется close при завершении работы - 1 балл
запись в базу данных выполняется в асинхронном виде - 1 балл
соединение с базой данных закрывается при завершении работы - 1 балл

Работаем с apidata.mos.ru
"""

import asyncio
from dataclasses import dataclass
from datetime import datetime
from aiohttp import ClientSession
from loguru import logger
import psycopg2

from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base # model's basis
from sqlalchemy.orm import sessionmaker, scoped_session, relationship

#import api key
from const import secret_key

#make engine and Base
engine = create_engine("sqlite:///mosru_data.db")
Base = declarative_base(bind=engine)
# make a session
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


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

@dataclass
class ApiService:
    """Service class"""
    name: str
    url: str

# make two different addresses
address_1 = 'https://apidata.mos.ru/v1/datasets?$inlinecount=allpages$foreign=true?&api_key=' +\
    secret_key
address_2 = 'https://apidata.mos.ru/v1/datasets?$skip=200&$top=200&$inlinecount=allpages' \
            '$orderby=caption?&api_key=' +\
            secret_key

SERVICES = [
    ApiService("mosru_1",address_1), # name, link
    ApiService("mosru_2",address_2),
    ApiService("mosru_1",address_1),
]

async def fetch(session: ClientSession, url: str) -> dict:
    """Async function for getting response (dict)"""
    async with session.get(url) as response:
        return await response.json()

async def fetch_data(apiservice: ApiService) -> list:
    async with ClientSession() as session:
            result = await fetch(session, apiservice.url)
    logger.info("Got result for {}", apiservice.name)
    return result

async def get_data():
    coros = [fetch_data(s) for s in SERVICES]
    done, pending = await asyncio.wait(
        coros,
        timeout=15, # если не выполнится за _ сек, бросай
        return_when=asyncio.ALL_COMPLETED
        # return_when=asyncio.FIRST_COMPLETED
    )
    logger.info(f'Асинхронно выполнено задач:    {len(done)}')
    logger.info(f'"done" tasks: {done}')
    logger.info(f'Асинхронно не выполнено задач: {len(pending)}')
    logger.info(f'"pending" tasks: {pending}')
    for task in pending:
        logger.debug(f"Cancelling task {task}")
        task.cancel()
    result = None
    for task in done:
        logger.info(f'start "done" {task}')
        if 'Message' not in task.result().keys():
            result = task.result()
            logger.info(f"Got result: {task.result().keys()}")
            break
        else:
            logger.warning("Результат отсутствует ('Message')")
    else:
        logger.warning("Результат отсутствует")
    try:
        logger.info(result.keys())
    except:
        logger.info(result)
    return result

def run_main():
    """function for demo"""
    asyncio.run(get_data())

def run_main_():
    """function, that returns asyncfunction's result"""
    return asyncio.run(get_data())

if __name__ == '__main__':

    res = run_main_()
    logger.info(f"result's type: {type(res)}")
    try:
        logger.info(res.keys())
    except:
        pass

    Base.metadata.create_all()
    logger.info("created DB")
    if res:
        logger.info("begin session")
        session = Session()

        r = Rubric(text='SOME RUBRIC')
        r = session.query(Rubric).filter_by(text="SOME RUBRIC").one()
        session.add(r)
        session.commit()

        data = res['Items']
        for i in range(len(data)):
            if i % 100 == 0:
                logger.info(f"writing item #{i}")
            data_input = data[i]
            data_list = ['Id', 'Caption', 'CategoryId','PublishDate',
                         'Keywords','ContainsGeodata','IsForeign','IsArchive',
                         'IsNew','LastUpdateDate']
            param = [data_input[el] for el in data_list]
            dataset_1 = MosruDataset(id_from_mosru=param[0], caption=param[1],
                                     categoryid=param[2],publishdate=param[3],keywords=param[4],
                                     containsgeodata=param[5], isforeign=param[6],
                                     isarchive=param[7],isnew=param[8], lastupdatedate=param[9],
                                     rubric=r.id
                                     )
            session.add(dataset_1)
            session.commit()
        logger.info('session closed')
        session.close()



