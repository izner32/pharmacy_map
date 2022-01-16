import pandas as pd 
from database import connect_database

# load/insert data into tables query
def insert_store_query():
    filepath = "server/src/data/output_data/transformed_data/cleaned_drugstores_with_coordinates.csv"
    df_store_branch = pd.read_csv(filepath)
    
    stores = ["Mercury Drugs","Rose Pharmacy","The Generics Pharmacy","Generika","South Star Drugs","Watsons Pharmacy"]
    table_names = ["mercury","rose","generika","the_generics_pharmacy","south_star_drugs","watsons"]
    store_queries = []

    for i,store_name in enumerate(stores):
        for index, row in df_store_branch.iterrows():
            try:
                if row[1] == store_name:
                    stores_insert = ("""
                        INSERT INTO {} (branch_id, name, address, contact, latitude, longitude)
                        VALUES ({},'{}','{}','{}',{},{})
                        ON CONFLICT (branch_id) DO NOTHING
                        ;
                    """.format(table_names[i], row[0], row[1], row[2].replace("'","''"), row[3], row[4], row[5]))
                    store_queries.append([stores_insert])
                else:
                    continue   
            except Exception as e:
                print("error at row {}".format(index+1))
                print("ERROR : "+str(e))
                break
    
    return store_queries

insert_store_query()

def insert_store(conn,cur):
    for i,query in enumerate(insert_store_query()):
        try:
            # print(query[0])
            # break
            cur.execute(query[0])
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
            