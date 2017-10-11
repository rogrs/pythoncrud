#!/usr/bin/env python
import csv
import datetime
import pymssql
from decimal import Decimal
import os

db_url  = os.getenv('STG_SERVER')
db_user = os.getenv('STG_USERNAME')
db_password = os.getenv('STG_PASSWORD')
db_database = os.getenv('STG_DATABASE')


conn = pymssql.connect(server=db_url,
                       user=db_user,
                       password=db_password,
                       database=db_database)

# Create a database cursor
cursor = conn.cursor()

query=open('query.txt', 'r').read()

# Execute the query
cursor.execute(query)

with open("output.csv", "w") as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in cursor:
        writer.writerow(row)

# Close the cursor and the database connection
cursor.close()
conn.close()
