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

    Base.metadata.create_all(engine)

    logger.info("created DB")
    if res:
        logger.info("begin session")
        session = Session()

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
            data_list = ['Id', 'Caption', 'CategoryId', 'PublishDate',
                         'Keywords', 'ContainsGeodata', 'IsForeign', 'IsArchive',
                         'IsNew', 'LastUpdateDate']
            param = [data_input[el] for el in data_list]
            dataset_1 = MosruDataset(id_from_mosru=param[0], caption=param[1],
                                     categoryid=param[2], publishdate=param[3], keywords=param[4],
                                     containsgeodata=param[5], isforeign=param[6],
                                     isarchive=param[7], isnew=param[8], lastupdatedate=param[9],
                                     rubric=r.id
                                     )
            session.add(dataset_1)
            session.commit()
        logger.info('session closed')

        example = session.query(MosruDataset).filter_by(isarchive=True, containsgeodata=False).all()
        logger.info(f"example len: {len(example)}")
        session.close()

from app import app

if __name__ == '__main__':
    app.config.update(
        DEBUG=True,
        SECRET_KEY="powerful secretkey",
        WTF_CSRF_SECRET_KEY="a csrf secret key",
    )

    app.run(
        # host='0.0.0.0',
        debug=True,
    )