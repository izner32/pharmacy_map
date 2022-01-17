from db_conn import connect_database

# create query for stores table
stores_create = ("""
    CREATE TABLE IF NOT EXISTS stores(
        branch_id INTEGER PRIMARY KEY,
        name VARCHAR(40),
        address TEXT,
        contact VARCHAR(200),
        latitude DECIMAL(8,6),
        longitude DECIMAL(9,6)
    );
""")

# create stores table 
def create_store(conn,cur):
    cur.execute(stores_create)
    conn.commit() 

def main():
    conn, cur = connect_database()
    create_store(conn,cur)
    conn.close()

main()

