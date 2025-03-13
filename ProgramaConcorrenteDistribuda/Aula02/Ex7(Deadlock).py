import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def T1():
    print("T1: Tentando adquirir lock1...")
    lock1.acquire()
    print("T1: lock1 adquirido!")
    time.sleep(1)

    lock2.acquire()
    print("T1: lock2 adquirido!")
    lock2.release()
    lock1.release()
    print("T1: Finalizado!")


def T2():
    print("T2: Tentando adquirir lock2...")
    lock2.acquire()
    print("T2: lock2 adquirido! Tente aduquirir lock1")
    time.sleep(1)

    lock1.acquire()
    print("T2: lock1 adquirido!")
    lock1.release()
    lock2.release()
    print("T2: Finalizado!")


t1 = threading.Thread(target=T1)
t2 = threading.Thread(target=T2)

t1.start()
t2.start()


# Variavel global (acessada por todas as threads)

Contador = 0


def incrementar():
    global Contador
    for _ in range(5000):
        V = Contador
        time.sleep(0.001)
        Contador = V + 1


threads = []

for i in range(50):
    t = threading.Thread(target=incrementar)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Contador: {Contador}")
