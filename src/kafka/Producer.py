import threading, time

from kafka import KafkaProducer


class Producer(threading.Thread):
    daemon = True

    def run(self):
        producer = KafkaProducer(bootstrap_servers='172.16.218.128:10021')

        while True:
            producer.send("test", "msg")
            # producer.send("test", "abc")
            time.sleep(1)
