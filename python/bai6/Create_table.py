import pymysql
db = pymysql.connect("localhost","root","12345678","bai6")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS sensors")
sql = """CREATE TABLE sensors(
			id INT(10) PRIMARY KEY AUTO_INCREMENT,
			SensorID char(10) NOT NULL,
			Temperature INT(3) NOT NULL,
			Humidity INT(3) NOT NULL,
			Data_and_Time char(30) NOT NULL)"""
cursor.execute(sql)
db.close()