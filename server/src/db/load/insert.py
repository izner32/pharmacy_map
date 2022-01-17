import pandas as pd 
from db_conn import connect_database

# insert query for store table 
def insert_store_query():
    filepath = "server/src/data/output_data/transformed_data/cleaned_drugstores_with_coordinates.csv"
    df_store_branch = pd.read_csv(filepath)
    insert_queries = []

    for index, row in df_store_branch.iterrows():
        try:
            stores_insert = ("""
                INSERT INTO stores (branch_id, name, address, contact, latitude, longitude)
                VALUES ({},'{}','{}','{}',{},{})
                ON CONFLICT (branch_id) DO NOTHING
                ;
            """.format(row[0], row[1], row[2].replace("'","''"), row[3], row[4], row[5]))
            insert_queries.append(stores_insert)
        except Exception as e:
            print("error at row {}".format(index+1))
            print("ERROR : "+str(e))
            break
    return insert_queries

# insert values at stores table
def insert_store(conn,cur):
    for i,query in enumerate(insert_store_query()):
        try:
            cur.execute(query)
            conn.commit() 
        except Exception as e:
            print("error at row {}".format(i+1))
            print("ERROR : "+str(e))
            break

def main():
    conn, cur = connect_database()
    insert_store(conn, cur)
    conn.close()


main()
            