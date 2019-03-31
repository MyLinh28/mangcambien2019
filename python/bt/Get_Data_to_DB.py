import pymysql
import json

def Heart(jsonData):
	json_Dict = json.loads(jsonData)
	#ID = json_Dict['ID']
	Data_Time = json_Dict['Data_Time']
	Heart_rate = json_Dict['Heart_rate']
	Stt = json_Dict['Stt']

	db = pymysql.connect("localhost","root","12345678","bai6")
	cursor = db.cursor()
	sql = """INSERT INTO heart(Heart_rate,Stt,Data_Time)
				VALUES (%s,%s,%s)"""
	val = (Heart_rate,Stt,Data_Time)
	cursor.execute(sql,val)
	db.commit()
	db.close()