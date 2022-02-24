import sqlite3 as sql

#This function for creat table in databass
def creat_table():
    connection=sql.connect('S_Databass.db')
    cursor=connection.cursor()

    cursor.execute('CREATE TABLE student(id int PRIMARY KEY ,name nvarchar(20) ,family nvarchar(20), avg real) ')
    cursor.execute('CREATE TABLE teacher(id int PRIMARY KEY ,name nvarchar(20) ,family nvarchar(20) ,idc int )')
    cursor.execute('CREATE TABLE course(id int PRIMARY KEY ,name nvarchar(20))')
    cursor.execute('CREATE TABLE unit_select(id int PRIMARY KEY, ids int, idc int, idt int, mark real)')

    connection.commit()

#for creat table uncomment line 16
# creat_table()

class dbm:
    def __init__(self):
        self.connection=sql.connect('S_Databass.db')
        self.cursor=self.connection.cursor()

    def insert(self,Q,P):
        self.cursor.execute(Q, P)
        self.connection.commit()

    def select(self,Q):
        self.cursor.execute(Q)
        L = self.cursor.fetchall()
        return L


    def update(self,Q):
        self.cursor.execute(Q)
        self.connection.commit()

