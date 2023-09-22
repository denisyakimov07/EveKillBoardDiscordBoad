from loguru import logger

from DB.db import db


def add_server_config(d_server_id: int):
    logger.info(f'Server {d_server_id}')
    try:
        if db.server_admin_pass.find({d_server_id}):
            logger.info('Server exist')
            logger.info(db.servers_config.find({d_server_id}))
        else:
            db.servers_config.insert_one({"server_id": d_server_id})
            logger.info(f'Server {d_server_id} added to db')
    except Exception as ex:
        logger.error(f"Cant get server info {ex}")