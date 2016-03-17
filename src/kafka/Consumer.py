import threading, time
from kafka import KafkaConsumer


class Consumer(threading.Thread):
    daemon = True

    def run(self):
        consumer = KafkaConsumer(bootstrap_servers='172.16.218.128:10021')
        consumer.subscribe(['test'])

        for msg in consumer:
            msg = next(consumer)
            print msg
