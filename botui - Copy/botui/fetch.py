#import sqlite3 as sql



def fetch(id):
     #response=['']
     #with sql.connect(r'botui\database.db') as con:
       #  cur = con.cursor()
        # query=f"select response from response where id={id}"  
         #cur.execute(query)
        response=["""We regularly post about vacancies in our facebook page. Please keep an eye on our facebook page
        to get further updates.""",""" Please provide your contact number. One of our customer care executives will get in touch very
        soon""",""" Please provide your contact number. One of our customer care executives will get in touch very
        soon""", """Please provide your contact number. One of our customer care executives will get in touch very
        soon""",""" Please provide your contact number. One of our customer care executives will get in touch very
        soon""",""" We regularly post about vacancies in our facebook page. Please keep an eye on our facebook page
        to get further updates.""","""Yes, we do. You can share your CV here at hr@theantopolis.com""","""Hello Sir,How can I help you"""]
         
         #msg = cur.fetchall()[0][0]
        msg=response[id-1]
        return msg

 

  