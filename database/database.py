import sqlite3
 
# connecting to the database
connection = sqlite3.connect("database/accountServer.db")
 

crsr = connection.cursor()
 

sql_command = """CREATE TABLE Users (
    UserID int,
    UserName varchar(255)
    PassWord varchar(255))"""

crsr.execute(sql_command)
 

sql_command = """"""
crsr.execute(sql_command)
 

connection.commit()
 

connection.close()