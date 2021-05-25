import pandas as pd
import psycopg2

host ="host"
port=5432

conn = psycopg2.connect("host='{}' port={} dbname='{}' user={} password={}".format(host, port,
 "TestDb", "user", "passwd"))

sql = "SELECT * from TestTable;"

testDF = pd.read_sql_query(sql, conn)


print(testDF.count)

conn = None
