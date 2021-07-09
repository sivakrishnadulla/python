import sqlite3

conn = sqlite3.connect("xyz.db")
cursor = conn.cursor()  # to make run faster we use cursor() functions
print("Data Base Opened")
#in SQL coloumns are called as 'FIELDS', row are called as 'RECORDS'
#primary key = unique + not null
#conn.execute(''' CREATE TABLE IF NOT EXISTS EMPLOYEE1( ID INT PRIMARY KEY NOT NULL,NAME TEXT UNIQUE NOT NULL,AGE AGE INT NOT NULL,SALARY INT NOT NULL)''')
print("Data Base created")

##def insert_records(ID,NAME,AGE,SALARY):
##    cursor.execute('''INSERT INTO EMPLOYEE1(ID,NAME,AGE,SALARY) VALUES(?,?,?,?)''',(ID,NAME,AGE,SALARY))
##    conn.commit()
##    print("record inserted")

def Display():
    data=cursor.execute("SELECT * FROM EMPLOYEE1 ")

    for record in data:
        print('ID: ' +str(record[0]))
        print('NAME: ' +str(record[1]))
        print('AGE: ' +str(record[2]))
        print('SALARY: ' +str(record[3]))
    x = data.fetchall()

    conn.commit()

def update_records():
    cursor.execute(''' UPDATE EMPLOYEE1 set AGE=30 WHERE ID=3''') #we can perform any modify operations here
    conn.commit()
    print('record updated')

update_records()

def delete_records():
    cursor.execute('''DELETE from EMPLOYEE1 WHERE ID=7''') # once record delete it wont come back
    conn.commit()
    print('record deleted')

delete_records()


Display()

#insert_records(7,'madhan',25,560000)
conn.close()
print("Database closed")
