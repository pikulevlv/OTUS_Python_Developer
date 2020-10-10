from dataclasses import dataclass
from aiohttp import ClientSession
import asyncio
from loguru import logger


from sqlalchemy import create_engine, Table, MetaData
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base # model's basis
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from models import engine, Base
from const import secret_key #import api key

# make a session
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

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