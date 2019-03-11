from random import randint
#su dung thuoc tinh ramdom tu module randint
from time import sleep
from  datetime import datetime

print ("Chuong trinh lay ngau nhien")
try:
	while(1):
		temperature = randint(28,30)
		humidity = randint(80,90)
		time_now  =  datetime.now()
		print ('Cap nhap luc %s ' %str(time_now))
		print ('Nhiet do: %s' %str(temperature))
		print ('Do am: %s' %str(humidity))
		print ('----------------------')
		sleep(1)
except KeyboardInterrrupt:
	print ('Chuong trinh ket thuc')
