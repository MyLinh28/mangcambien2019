import pymysql
db = pymysql.connect("localhost","root","12345678","bai6")
cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS heart")
sql = """CREATE TABLE heart(
			ID INT(10) PRIMARY KEY AUTO_INCREMENT,
			Heart_rate INT(3) NOT NULL,
			Stt char(10) NOT NULL,
			Data_Time char(30) NOT NULL)"""
cursor.execute(sql)
db.close()