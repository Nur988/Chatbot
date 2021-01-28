import sqlite3 as sql


def store(table,colname,val):
     with sql.connect(r'botui\database.db') as con:
         cur = con.cursor()
         query=f"insert into {table} ({colname}) values('{val}')"   
         cur.execute(query)
         con.commit()
         
         
         return 1


   