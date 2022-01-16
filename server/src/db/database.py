import os 
import psycopg2 
from dotenv import load_dotenv, find_dotenv 

load_dotenv(find_dotenv()) 

def create_database():
    conn = psycopg2.connect(host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"),database="postgres",user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"))
    conn.set_session(autocommit = True) 
    cur = conn.cursor() 

    cur.execute("DROP DATABASE IF EXISTS storedb")
    cur.execute("CREATE DATABASE storedb WITH ENCODING 'utf8' TEMPLATE template0")

    conn.close()

    return conn, cur

def connect_database():
    conn = psycopg2.connect(host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"),database="storedb",user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"))
    conn.set_session(autocommit = True) 
    cur = conn.cursor()

    return conn, cur

# create database - execute only once 
def main():
    cur, conn = create_database()
    conn.close()
# main()

