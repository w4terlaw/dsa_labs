import threading


class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()

    def increment(self):
        for _ in range(100000):
            with self.lock:
                self.value += 1

    def decrement(self):
        for _ in range(100000):
            with self.lock:
                self.value -= 1


def main():
    n = int(input("Введите количество потоков для инкремента: "))
    m = int(input("Введите количество потоков для декремента: "))

    counter = Counter()

    threads = []

    for _ in range(n):
        threads.append(threading.Thread(target=counter.increment))

    for _ in range(m):
        threads.append(threading.Thread(target=counter.decrement))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Значение счетчика: {counter.value}")


if __name__ == "__main__":
    main()
