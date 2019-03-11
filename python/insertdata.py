import MySQLdb

# mo ket noi toi Database
db = MySQLdb.connect("localhost","root","12345678","sinhvien" )

# chuan bi mot doi tuong cursor boi su dung phuong thuc cursor()
cursor = db.cursor()

# Truy van SQL de INSERT mot ban ghi vao trong database.
sql = """INSERT INTO sensors(temperature,
         humidity, time)
         VALUES ('19', '37', '2019-02-15 09:05:27')"""
try:
   # Thuc thi lenh SQL
   cursor.execute(sql)
   # Commit cac thay doi vao trong Database
   db.commit()
except:
   # Rollback trong tinh huong co bat ky error nao
   db.rollback()

# ngat ket noi voi server
db.close()
