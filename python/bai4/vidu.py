def connect():
	import MySQLdb
	db = MySQLdb.connect("localhost","root","12345678","sinhvien")
	cursor = db.cursor()
	db.close()
def create():
	import MySQLdb
	db = MySQLdb.connect("localhost","root","12345678","sinhvien")
	cursor = db.cursor()
	sql = """CREATE TABLE sensors(
       		 id INT(10) PRIMARY KEY AUTO_INCREMENT, temperature INT(3) NOT NULL,
       		 humidity INT(3) NOT NULL, time DATETIME NOT NULL)"""
	cursor.execute(sql)
	db.close()
def insert():
	import MySQLdb
	db = MySQLdb.connect("localhost","root","12345678","sinhvien")
	cursor = db.cursor()
	sql = """INSERT INTO sensors(temperature, humidity, time) VALUES(14,23,'2019-04-05 00:30:12')"""
	try:
		cursor.execute(sql)
		db.commit()
	except:
   		db.rollback()
	db.close()
def dulieu():
	import MySQLdb
	db = MySQLdb.connect("localhost","root","12345678","sinhvien")
	cursor = db.cursor()
	sql = "SELECT *FROM sensors"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		print (result)
	except:
		print ("khong co du lieu")
def update():
	import MySQLdb
	db = MySQLdb.connect("localhost","root","12345678","sinhvien")
	cursor = db.cursor()
	sql = "UPDATE sensors SET temperature=30,humidity=80 where id=1"
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()
def delete():
	import MySQLdb
	db = MySQLdb.connect("localhost","root","12345678","sinhvien")
	cursor = db.cursor()
	sql =  "DELETE FROM sensors WHERE id=4"
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()
