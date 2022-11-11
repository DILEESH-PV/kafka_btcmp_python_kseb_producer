import random
import time
from kafka import KafkaProducer

bootstrap_server = ["localhost:9092"]
topic = "kseb"
producer = KafkaProducer(bootstrap_servers = bootstrap_server)

producer = KafkaProducer()
jsondata={}

def senddata():
    temp = random.randint(0,10)
    jsondata={'userid':2,'unit':temp}
    message = producer.send(topic,bytes(str(jsondata),"utf-8"))
    print(jsondata)

    metadata = message.get()
   # print(metadata.topic)
    #print(metadata.partition)
    time.sleep(4)
while True:
    senddata()