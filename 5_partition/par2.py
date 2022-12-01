# kafka-topics.sh --create --topic hello_world2 --bootstrap-server localhost:9092 replication-factor 1 --partitions 3
#Lab 2: Pass key value pair
from json import dumps
from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])
topic_name='hello_world2'
producer.send(topic_name, key=b'foo', value=b'bar') #Note :key & value serialization we are doing while publishing the message
                                                    #itself , so explicitly not mentioning the key or value serializer
producer.send(topic_name, key=b'foo', value=b'bar')
producer.close()