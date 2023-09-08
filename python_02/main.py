import psycopg2
from fastapi import FastAPI


app = FastAPI()
con = psycopg2.connect(
    database = "test",
    user = "postgres",
    password = "Abigail@123",
    host = "localhost",
    port = "5432"
)

cursor_obj = con.cursor()
cursor_obj.execute("SELECT * FROM EMP")
result = cursor_obj.fetchall()