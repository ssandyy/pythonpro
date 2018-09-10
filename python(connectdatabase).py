import cursor as cursor
import cx_Oracle
import pymysql

try:
    query="insert into Studentdata values(100,'Durga',99)"
    con=cx_Oracle.connect('root/Qwertyz@1899@localhost')
    cursor=con.cursor()
    cursor.execute(query)
    con.commit()
    print('record inserted sucessfully..')
except cx_Oracle.DatabaseError as e:
    if con:                                  # con:   = con !=none
        con.rollback()
        print("there is a problem:",e)

finally:
    if cursor:
        cursor.close()
    if con:
        con.close()