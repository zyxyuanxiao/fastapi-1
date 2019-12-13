import databases
import sqlalchemy
import aioredis
# import asyncio_redis

database = databases.Database("mysql+pymysql://root:root@localhost/freeinfo")
metadata = sqlalchemy.MetaData()


async def create_connection():
    await database.connect()


async def disconnect():
    await database.disconnect()


# async def redis_connection():
#     redis_db1 = await aioredis.create_redis_pool("redis://localhost/15672//")
#     return redis_db1
