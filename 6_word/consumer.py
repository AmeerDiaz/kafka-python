from kafka import KafkaConsumer


consumer = KafkaConsumer('test')
for message in consumer:
	'''print(message.value)'''
	print ("%d:%d: k=%s v=%s" % (message.partition,
                                 message.offset,
                                 message.key,
                                 message.value))
