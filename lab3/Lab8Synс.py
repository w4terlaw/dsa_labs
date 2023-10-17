import threading


def thread_synchronized(func):
    lock = threading.Lock()

    def wrapper(*args, **kwargs):
        with lock:
            return func(*args, **kwargs)

    return wrapper


class Counter:
    def __init__(self):
        self.value = 0

    # @thread_synchronized
    def increment(self, i):
        for _ in range(100000):
            print(i)
            self.value += 1

    @thread_synchronized
    def decrement(self, i2):
        for _ in range(100000):
            # print(i2)
            self.value -= 1


def main():
    n = int(input("Введите количество потоков для инкремента: "))
    m = int(input("Введите количество потоков для декремента: "))

    counter = Counter()

    threads = []

    for i in range(n):
        threads.append(threading.Thread(target=counter.increment, args=(i,)))

    for i2 in range(m):
        threads.append(threading.Thread(target=counter.decrement, args=(i2,)))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Значение счетчика: {counter.value}")


if __name__ == "__main__":
    main()
