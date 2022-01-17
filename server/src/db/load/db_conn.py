import os 
import psycopg2 
from dotenv import load_dotenv, find_dotenv 

load_dotenv(find_dotenv()) 

def connect_database():
    conn = psycopg2.connect(host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"),database="storedb",user=os.getenv("DB_USER"),password=os.getenv("DB_PASSWORD"))
    conn.set_session(autocommit = True) 
    cur = conn.cursor()

    return conn, cur