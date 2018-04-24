
import psycopg2
from config import str_connect_to_db
import hashlib,\
    datetime,\
    binascii,\
    os
import traceback
import datetime


def create_connection():
    """
    метод создания подключения к БД
    :return: или подключение или None
    """
    conn = None
    try:
        conn = psycopg2.connect(str_connect_to_db)
    except:
        print("I am unable to connect to the database")
    return conn


def remove(id):
    select = '''
        DELETE FROM events WHERE id_event = {}
    '''.format(id)
    print(select)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(select)
    conn.commit()
