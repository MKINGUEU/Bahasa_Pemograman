import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database ="bpuas"
)
if db.is_connected():
  print("Berhasil terhubung ke database")