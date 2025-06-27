import threading
import time

def long_task(name):
    print(f"Задача {name} началась")
    time.sleep(2)
    print(f"Задача {name} завершилась")

thread1 = threading.Thread(target=long_task, args=("A",))
thread2 = threading.Thread(target=long_task, args=("B",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Все потоки завершили работу")
