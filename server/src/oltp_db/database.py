import os 
import psycopg2 
from dotenv import load_dotenv, find_dotenv 

load_dotenv(find_dotenv()) 

def create_database():
    conn = psycopg2.connect(host="localhost", port="5432",database="postgres",user="postgres",password=os.getenv("DB_PASSWORD"))
    conn.set_session(autocommit = True) 
    cur = conn.cursor() 

    cur.execute("DROP DATABASE IF EXISTS branchdb")
    cur.execute("CREATE DATABASE branchdb WITH ENCODING 'utf8' TEMPLATE template0")

    conn.close()

    conn = psycopg2.connect(host="localhost", port="5432",database="branchdb",user="postgres",password=os.getenv("DB_PASSWORD"))
    conn.set_session(autocommit = True) 
    cur = conn.cursor()

    return conn, cur

def main():
    cur, conn = create_database()
    conn.close()

main()
