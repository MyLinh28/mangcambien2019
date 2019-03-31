import paho.mqtt.client as mqtt
import random, json
from datetime import datetime
from time import sleep

MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic = "linh/heart_rate"

#------------------------------
#ham ket noi den may chu
def on_connect(client, userdata, rc):
	if rc != 0:
		pass
		print ("Unable to connect to MQTT Broker...")
	else:
		print ("Connect wiht MQTT Broker: " + str(MQTT_Broker))

def on_publish(client, userdata, mid):
	pass

def on_disconnect(client, userdata, rc):
	if rc != 0:
		pass

mqttc = mqtt.Client()
mqttc.username_pw_set(username="linh",password="123456")
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish
mqttc.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)

#-----------------------------------------------------------------
#push du lieu
def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)
	print (("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic)))
	print ("")
#-----------------------------------------------------------------
#FAKE RANDOM SENSOR
def publish_Fake_Heart_values_to_MQTT():
	Heart_Fake_value = int(random.uniform(50,120))
	Heart_data = {}
	#Heart_data['ID'] = "Heart_rate"
	Heart_data['Data_Time'] = (datetime.today()).strftime("%d-%b-%Y %H:%M:%S")
	Heart_data['Heart_rate'] = Heart_Fake_value
	if 50 <= Heart_Fake_value < 60:
		Heart_data['Stt'] = "Low"
	if 60 <= Heart_Fake_value < 70:
		Heart_data['Stt'] = "Normal"
	if 70 <= Heart_Fake_value < 100:
		Heart_data['Stt'] = "High"
	if 100 <= Heart_Fake_value < 120:
		Heart_data['Stt'] = "Warring"
	heart_json_data = json.dumps(Heart_data)
	print ("Publishing fake Sensor Value: ")
	publish_To_Topic (MQTT_Topic, heart_json_data)
	#sleep(10)
while True:
	publish_Fake_Heart_values_to_MQTT()
	sleep(10)