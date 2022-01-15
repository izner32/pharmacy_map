import pandas as pd 

# load/insert data into tables
filepath = "server/src/data/output_data/transformed_data/cleaned_drugstores_with_coordinates.csv"
df_store_branch = pd.read_csv(filepath)

for index, row in df_store_branch.iterrows():
    stores_insert = ("""
        INSERT INTO (branch_id, name, address, contact, latitude, longitude)
        VALUES ({}, {}, {}, {}, {}, {})
    """.format(row[1], row[2], row[3], row[4], row[5], row[6]))