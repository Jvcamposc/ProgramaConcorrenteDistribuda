# Overhead
import threading
import time

Contador = 0
L = threading.Lock()


def Incrementar():
    global Contador
    global TempoTotal
    t0 = time.time()
    for _ in range(1000000):
        with L:
            Contador += 1
    tf = time.time()
    delta_t = tf - t0
    TempoTotal = TempoTotal + delta_t
    print(f"Tempo de execução: {delta_t}")


threads = [threading.Thread(target=Incrementar) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Contador final: {Contador}")
print(f"Tempo total: {TempoTotal:.2f} segundos")
