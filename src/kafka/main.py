import logging, time

from Producer import Producer
from Consumer import Consumer


def main():
    threads = [
        Producer(),
        Consumer()
    ]

    for t in threads:
        t.start()

    time.sleep(5000)


if __name__ == '__main__':
    main()
