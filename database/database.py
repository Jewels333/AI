import sqlite3
 
# connecting to the database
connection = sqlite3.connect("accountServer.db")
 

crsr = connection.cursor()
 

sql_command = """"""

crsr.execute(sql_command)
 

sql_command = """"""
crsr.execute(sql_command)
 

connection.commit()
 

connection.close()