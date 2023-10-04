import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(host='localhost', password='MAHI#82#ridm',user='root',database='gs')

  return __cnx