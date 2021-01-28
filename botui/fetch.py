import sqlite3 as sql



def fetch(id):
     with sql.connect(r'botui\database.db') as con:
         cur = con.cursor()
         query=f"select response from response where id={id}"  
         cur.execute(query)
         
         msg = cur.fetchall()[0][0]
         return msg

 

  