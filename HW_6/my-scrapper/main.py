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

from loguru import logger

from models import Rubric, MosruDataset
from server import ApiService, address_1, address_2, SERVICES, fetch, fetch_data, \
    get_data, run_main, run_main_, engine, Base, session_factory, Session
import config
from flask import request

if __name__ == '__main__':

    res = run_main_()
    logger.info(f"result's type: {type(res)}")
    try:
        logger.info(res.keys())
    except:
        pass
    logger.info("attention!")
    
    # Base.metadata.create_all()
    Base.metadata.create_all(engine)
    # DeclarativeBase.metadata.create_all(engine)
    # Meta.create_all(engine)
    
    logger.info("created DB")
    if res:
        logger.info("begin session")
        session = Session()

        # r = Rubric(text='SOME RUBRIC')
        r = session.query(Rubric).filter_by(text="SOME RUBRIC").one_or_none()
        if r is None:
            r = Rubric(text='SOME RUBRIC')
            session.add(r)
            session.commit()
            r = session.query(Rubric).filter_by(text="SOME RUBRIC").one()

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
        # session.close()

        example = session.query(MosruDataset).filter_by(isarchive=True, containsgeodata=False).all()
        # example = session.query(MosruDataset).one()
        # r = session.query(Rubric).filter_by(text="SOME RUBRIC").one_or_none()
        logger.info(f"example len: {len(example)}")
        for e in example:
            logger.info(f"{e.id}, {e.created_at}")
        session.close()



