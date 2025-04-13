import mariadb
from mariadb import Connection
from typing import Optional
from fastapi import HTTPException, status
from time import sleep
from os import getenv

_pool = None

def create_database_pool():
    global _pool

    _pool = mariadb.ConnectionPool(
        user=getenv('DATABASE_USER'),
        password=getenv('DATABASE_PASSWORD'),
        host=getenv('DATABASE_HOST'),
        port=3306,
        pool_name="mypool",
        pool_size=5,
        database=getenv('DATABASE')
    )
    
def get_database_connection() -> Connection:
    try:
        return _pool.get_connection()
    except Exception as e:
        raise HTTPException(status.HTTP_500_INTERNAL_SERVER_ERROR, 'Could not create a database connection')
