import sqlite3
connection=sqlite3.connect("user.db")
cursor=connection.cursor()
def insert(admno,name,age):
    x="""insert into user(admno,name,age)values("{}","{}","{}")""".format(admno,name,age)
    cursor.execute(x)
    connection.commit()
    connection.close()
def update(name,age,admno):
    x="""update user set name="{}",age="{}" where admno="{}" """.format(name,age,admno)
    cursor.execute(x)
    connection.commit()
    connection.close()
def delete(admno):
    x="""delete from user where admno="{}" """.format(admno)
    cursor.execute(x)
    connection.commit()
    connection.close()
def select():
    
    cursor.execute("select * from user")
    y=cursor.fetchall()
    for i in y:
        print(i)




w="""
1.INSERT DATA
2.UPDATE DATA
3.DELETE  DATA
4.SELECT  DATA
5.EXIT
"""
from tabulate import tabulate
x=[["1.INSERT DATA"],["2.UPDATE DATA"],[" 3.DELETE DATA"],["4.SELECT DATA"],["5.EXIT FROM THIS"]]
print(tabulate(x))
print(w)
ch=1
while ch==1:
    x=int(input("ENTER THE ABOVE DATA :="))
    if x==1:
        admno=int(input("enter the admno :"))
        name=input("enter the name :")
        age=int(input("enter the age :"))
        insert(admno,name,age)
        print("data inserted successfully")
    elif x==2:
        admno=int(input("enter the admission number to update :"))
        name=input("enter the name to update :")
        age=int(input("enter the age to update :"))
        update(name,age,admno)
        print("data updated successfully")
    elif x==3:
        admno=int(input("enter the admno to delete :"))
        delete(admno)
        print("data deleted sucessfully")
    elif x==4:
        select()
        print("data displayed successfully")
    elif x==5:
        exit()
    else:
        print("invalide input was given")

    ch=int(input("enter 1 to continue again = "))
