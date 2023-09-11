from DB.db import db
from loguru import logger


def add_server_config(server_id: int):
    logger.info(f'Server {server_id}')
    try:
        if db.servers_config.find({server_id: server_id}):
            logger.info('Server exist')
            logger.info(db.servers_config.find({server_id: server_id}))
        else:
            db.servers_config.insert_one({"server_id": server_id})
            logger.info(f'Server {server_id} added to db')
    except Exception as ex:
        logger.error(f"Cant get server info {ex}")