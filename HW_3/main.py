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

Гугл
AIzaSyA21_lungeZwngEwtwAa7O4agwVUM30RLg

Мос ру
Смехов
Вениамин
https://apidata.mos.ru/Docs
ierwnrsl16s0@mail.ru
35776b13f50be5e64783795d20f359a3

https://apidata.mos.ru/v1/datasets?$inlinecount=allpages$foreign=true?&api_key=35776b13f50be5e64783795d20f359a3
https://apidata.mos.ru/v1/datasets?$inlinecount=allpages$foreign=false?&api_key=35776b13f50be5e64783795d20f359a3
https://apidata.mos.ru/v1/datasets/654/icon/s?&api_key=35776b13f50be5e64783795d20f359a3
https://apidata.mos.ru/v1/datasets/654/icon/s?&api_key=35776b13f50be5e64783795d20f359a3

"""

import asyncio
from dataclasses import dataclass
from aiohttp import ClientSession
from loguru import logger
from const import secret_key

# import psycopg2
# from const import PASSWORD

@dataclass
class ApiService:
    name: str
    url: str

address_1 = 'https://apidata.mos.ru/v1/datasets?$inlinecount=allpages$foreign=true?&api_key=' +\
    secret_key

address_2 = 'https://apidata.mos.ru/v1/datasets?$skip=200&$top=200&$inlinecount=allpages' \
            '$orderby=caption?&api_key=' +\
            secret_key
# ip_fields = ['Id', 'Caption', 'PublishDate', 'Keywords']

SERVICES = [
    ApiService("mosru_1",address_1), # название, ссылка
    ApiService("mosru_2",address_2),
    ApiService("mosru_1",address_1),
]

async def fetch(session: ClientSession, url: str) -> dict:
    """Async function for getting response (dict)"""
    async with session.get(url) as response:
        return await response.json()

async def fetch_data(apiservice: ApiService) -> list:
    """Async function """
    async with ClientSession() as session:
            result = await fetch(session, apiservice.url)
    logger.info("Got result for {}", apiservice.name)
    return result#['Items']

async def get_my_ip():
    coros = [fetch_data(s) for s in SERVICES]
    # res = await fetch_data(SERVICES[0])

    done, pending = await asyncio.wait(
        coros,
        # timeout=15, # если не выполнится за _ сек, бросай
        return_when=asyncio.ALL_COMPLETED
        # return_when=asyncio.FIRST_COMPLETED
    )
    print('Асинхронно выполнено задач:    ',len(done))
    print(done)
    print('Асинхронно не выполнено задач: ',len(pending))
    print(pending)
    for task in pending:
        # logger.debug("Cancelling task ", task)
        task.cancel()
    result = None
    for task in done:
        # logger.debug("Cancelling task ", task)
        if 'Message' not in task.result().keys():
            result = task.result()
            logger.info(f"Got result: {task.result().keys()}")
            break
        else:
            logger.warning("Результат отсутствует ('Message')")
    else:
        logger.warning("Результат отсутствует")
    try:
        print(result.keys())
    except:
        print(result)
    return result




def run_main():
    # asyncio.run(fetch_data(SERVICES[0]))
    asyncio.run(get_my_ip())

def run_main_():
    # asyncio.run(fetch_data(SERVICES[0]))
    return asyncio.run(get_my_ip())

if __name__ == '__main__':
    run_main()