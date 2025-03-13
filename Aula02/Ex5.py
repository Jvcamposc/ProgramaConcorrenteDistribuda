import threading
import time

# Variavel global (acessada por todas as threads)

Contador = 0
lock = threading.Lock()


def incrementa():
    global Contador
    for _ in range(10):
        lock.acquire()  # Bloqueia o acesso a variavel compartilhada
        try:
            Contador += 1
            print(Contador)
            time.sleep(1)
        finally:
            lock.release()  # Libera o acesso a variavel compartilhada


threads = []

for i in range(10):
    thread = threading.Thread(target=incrementa)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print(f"Contador:  {Contador}")
