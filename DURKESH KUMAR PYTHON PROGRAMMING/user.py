import sqlite3
connection=sqlite3.connect("user.db")
cursor=connection.cursor()
x="""create table user(admno integer,name char(20),age integer);"""
cursor.execute(x)
connection.commit()
connection.close()
