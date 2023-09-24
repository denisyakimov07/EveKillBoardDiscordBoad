import pymongo
from loguru import logger

from DB.db import client

db: pymongo.database.Database = client.session_url_tokens
def create_new_session(guild, url_token):
    try:
        db.session_url_tokens.replace_one({'_id': str(guild.id)}, {'_id': str(guild.id), 'url_token': str(url_token)})
        logger.info(f"Token updated guild.id - {guild.id}")
    except Exception as ex:
        logger.error(f"Cant get server info {ex}")
