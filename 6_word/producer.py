from kafka import KafkaProducer
from collections import Counter

producer = KafkaProducer(bootstrap_servers = 'localhost:9092')

while True:
	print("\n\nType \"quit\" to exit")
	print("Enter message to be sent:")
	msg = input()
	word_list = msg.split()
	msg = str(Counter(word_list).most_common(None))
	if msg == "quit":
		print("Exiting...")
		break
	producer.send('test', msg.encode('utf-8'))
	print("Sending msg \"{}\"".format(msg))
	print("Message sent!")
