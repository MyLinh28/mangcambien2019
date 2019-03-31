import pymysql
#from random import randint

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
	cursor.execute("DROP TABLE IF EXISTS sensor")
	sql = """CREATE TABLE sensor(
       		 id INT(10) PRIMARY KEY AUTO_INCREMENT, sensorid INT(3) NOT NULl,
			 long1 INT(3) NOT NULL, lat INT(3) NOT NULL, temp INT(3) NOT NULL,
			 humi INT(3) NOT NULL, rain INT(3) NOT NULL, status_weather VARCHAR(10), time_t DATETIME NOT NULL)"""
	cursor.execute(sql)
	db.close()

def random():
	from datetime import datetime
	import random
	sen=[1, 2, 3, 4]
	weather = ['rain', 'cold', 'wind', 'sunny' ]
	db = pymysql.connect("localhost","root","12345678","bai4")
	cursor = db.cursor()
	for i in  range(0,10):
		j = random.randint(0,3)
		k = random.randint(0,3)
		sensorid = sen[j]
		long1 = sen[j]
		lat = sen[j]
		temp = random.randint(20,30)
		humi = random.randint(80,90)
		rain = random.randint(0,1)
		status_weather = weather[k]
		time_t  =  datetime.now()
		sql = """INSERT INTO sensor(sensorid, long1, lat, temp, humi, rain, status_weather, time_t)
						VALUES (%s, %s,%s, %s, %s, %s,%s, %s)"""
		try:
			cursor.execute(sql,(sensorid, long1, lat, temp, humi, rain, status_weather,time_t))
			db.commit()
		except:
			db.rollback()
	db.close()
def yeucau():
	db=pymysql.connect("localhost","root","12345678","bai4")
	cursor = db.cursor()
	print("""Chon kieu du lieu ban muon sap xep:
		\n1. sensorid
		\n2. temp
		\n3. humi
		\n4. rain
		""")
	a = input()
	while(a!='1' and a!='2' and a!='3' and a!='4'):
		print('Nhap lai: ')
		a = input()
	print("""Chon:
		\n1.Sap xep tang
		\n2.Sap xep giam
		""")
	b = input()
	while(b!='1' and b!='2'):
		print("Nhap lai: ")
		b = input()
	try:
		if a == '1':
			if b == '1':
				sql = "select * from sensor order by sensorid asc"
			if b == '2':
				sql = "select * from sensor order by sensorid desc"
		if a == '2':
			if b == '1':
				sql = "select * from sensor order by temp asc"
			if b == '2':
				sql = "select * from sensor order by temp desc"
		if a == '3':
			if b == '1':
				sql = "select * from sensor order by humi asc"
			if b == '2':
				sql = "select * from sensor order by humi desc"
		if a == '4':
			if b == '1':
				sql = "select * from sensor order by rain asc"
			if b == '2':
				sql = "select * from sensor order by rain desc"
		cursor.execute(sql)
		print("3 gia tri dau tien la:")
		results = cursor.fetchmany(3)
		for row in results:
			print(row)
		#results = cursor.fetchall()
		#print (results)
	except:
		print("khong co du lieu")