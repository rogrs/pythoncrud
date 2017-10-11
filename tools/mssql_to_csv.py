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

# Replace this nonsense with your own query :)
query = """SELECT T.EXTERNAL_ID, T.CODE, T.DETAILING, T.HINT FROM (
SELECT  EXTERNAL_ID, SUBSTRING(PAYLOAD, 66, 3)  as CODE,  SUBSTRING(PAYLOAD, 89, 1)  as DETAILING,SUBSTRING(PAYLOAD, 26, 2) as HINT FROM LOG_ADAPTER_PEGASUS_NOTIFICATION
where  DESCRIPTION ='BILLING_AUTHORIZATION'
) AS T  WHERE T.CODE <> '00"'"""

# Execute the query
cursor.execute(query)

with open("output.csv", "w") as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in cursor:
        writer.writerow(row)

# Close the cursor and the database connection
cursor.close()
conn.close()
