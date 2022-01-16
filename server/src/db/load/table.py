from db_conn import connect_database

# create queries for multiple store
def create_store_query():
    stores = ["generika","mercury","rose","south_star_drugs","the_generics_pharmacy","watsons"]

    i = 0
    stores_query = []
    while i < len(stores):
        stores_create = ("""
            CREATE TABLE IF NOT EXISTS {}(
                branch_id INTEGER PRIMARY KEY,
                name VARCHAR(40),
                address TEXT,
                contact VARCHAR(200),
                latitude DECIMAL(8,6),
                longitude DECIMAL(9,6)
            );
        """.format(stores[i]))

        i = i + 1 
        stores_query.append(stores_create)
    
    return stores_query 

# create table 
def create_store(conn,cur):
    for i in create_store_query():
        cur.execute(i)
        conn.commit() 

def main():
    conn, cur = connect_database()
    create_store(conn,cur)
    conn.close()

main()

