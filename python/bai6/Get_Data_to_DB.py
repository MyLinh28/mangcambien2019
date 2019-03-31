import pymysql
import json

def Heart(jsonData):
	json_Dict = json.loads(jsonData)
	SensorID = json_Dict['Sensor_ID']
	Data_and_Time = json_Dict['Date']
	Temperature = json_Dict['Temperature']
	Humidity = json_Dict['Humidity']

	db = pymysql.connect("localhost","root","12345678","bai6")
	cursor = db.cursor()
	sql = """INSERT INTO sensors(SensorID,Data_and_Time,Temperature,Humidity)
				VALUES (%s,%s,%s,%s)"""
	val = (SensorID,Data_and_Time,Temperature,Humidity)
	cursor.execute(sql,val)
	db.commit()
	db.close()

#day len web
#dieu khien, do thi
#lam mot trang web  pub len git