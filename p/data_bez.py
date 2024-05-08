import sqlite3

# def createuserstable():
#   database = sqlite3.connect('baza.sqlite')
#   cursor = database.cursor()
#
#   cursor.execute('''CREATE TABLE IF NOT EXISTS users(
#   user_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#   fullname VARCHAR,
#   username VARCHAR,
#   chatid INTEGER UNIQUE
#   )''')
#
#   database.commit()
#   database.close()
#
# createuserstable()

def registeruser(full_name, user_name, chat_id):
  database = sqlite3.connect('baza.sqlite')
  cursor = database.cursor()
  cursor.execute('''INSERT INTO users(fullname, username, chatid)
  VALUES(?,?,?)''', (full_name, user_name, chat_id))
  database.commit()
  database.close()
















