import configparser

import mysql.connector
from mysql.connector import Error

def getConfig():
    config = configparser.ConfigParser()
    config.read("properties.ini")
    return config

connect_config= {
    'user': getConfig()['sql']['user'],
    'password': getConfig()['sql']['password'],
    'host':getConfig()['sql']['host'],
    'database':getConfig()['sql']['database'],
}

def getConnection():
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("connection successful")
            return conn
    except Error as e:
        print(e)

def getQuery(query):
    conn= getConnection()
    cursor= conn.cursor()
    cursor.execute(query)
    row= cursor.fetchone()
    conn.close()
    return row