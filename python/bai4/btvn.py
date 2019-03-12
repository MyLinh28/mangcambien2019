import pymysql
def connect():
	db = pymysql.connect("localhost","root","12345678","bai4")
	cursor = db.cursor()
	cursor.execute("SELECT VERSION()")
	data = cursor.fetchone()
	print ("Database version : %s " %data)
	db.close()

def create():
	db = pymysql.connect("localhost","root","12345678","bai4")
	cursor = db.cursor()
	cursor.execute("DROP TABLE IF EXISTS btvn")
	sql = """CREATE TABLE btvn(
       		 id INT(10) PRIMARY KEY AUTO_INCREMENT, temperature INT(3) NOT NULL,
       		 humidity INT(3) NOT NULL, light INT(3) NOT NULL, time DATETIME NOT NULL)"""
	cursor.execute(sql)
	db.close()
def insert():
	db = pymysql.connect("localhost","root","12345678","bai4")
	cursor = db.cursor()
	sql = """INSERT INTO btvn(temperature, humidity, light, time) 
				VALUES (15, 40, 25, '2019-03-04 09:45:25'), (10,18, 60, '2019-03-06 19:25:25') """
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()
def truyvan():
	db=pymysql.connect("localhost","root","12345678","bai4")
	cursor = db.cursor()
	sql = "SELECT * FROM btvn"
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
		print(results)
	except:
		print("khong co du lieu")
	db.close()
def update():
	db=pymysql.connect("localhost","root","12345678","bai4")
	cursor = db.cursor()
	sql = "UPDATE btvn SET temperature=30, humidity=80 WHERE id=1"
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()
def delete():
	db = pymysql.connect("localhost","root","12345678","bai4")
	cursor = db.cursor()
	sql = "DELETE FROM btvn WHERE id=2"
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
	db.close()
def ramdom():
	from random import randint
	from time import sleep
	from datetime import datetime
	db = pymysql.connect("localhost","root","12345678","bai4")
	cursor = db.cursor()
	try:
		for i in  range(0,10):
			temp = randint(28,30)
			hum = randint(80,90)
			light = randint(20,80)
			time  =  datetime.now()
			sql = """INSERT INTO btvn(temperature, humidity,light, time) 
						VALUES (%s, %s,%s, %s)"""
			#sleep(1)
			cursor.execute(sql,(temp,hum,light,time))
			db.commit()
	except:
		db.rollback()
	db.close()
def yeucau():
	db=pymysql.connect("localhost","root","12345678","bai4")
	cursor = db.cursor()
	print("Chon kieu du lieu ban muon sap xep (id, temperature, humidity, light)")
	a = input()
	while(a!='id' and a!='temperature' and a!='humidity' and a!='light'):
		print('Nhap lai: ')
		a = input()
	print("Chon:\n1.Sap xep tang\n2.Sap xep giam")
	b = input()
	while(b!='1' and b!='2'):
		print("Nhap lai: ")
		b = input()
	try:
		if a == 'id':
			if b == '1':
				sql = "select * from btvn order by id asc"
			if b == '2':
				sql = "select * from btvn order by id desc"
		if a == 'temperature':
			if b == '1':
				sql = "select * from btvn order by temperature asc"
			if b == '2':
				sql = "select * from btvn order by temperature desc"
		if a == 'humidity':
			if b == '1':
				sql = "select * from btvn order by humidity asc"
			if b == '2':
				sql = "select * from btvn order by humidity desc"
		if a == 'light':
			if b == '1':
				sql = "select * from btvn order by light asc"
			if b == '2':
				sql = "select * from btvn order by light desc"
		cursor.execute(sql)
		results = cursor.fetchall()
		print (results)
	except:
		print("khong co du lieu")