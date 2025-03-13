# Operação não atômica: é uma operação que não é executada de uma vez só, ou seja, é uma operação que pode ser interrompida no meio do processo.
# O código a seguir é um exemplo de operação não atômica:
import threading
import time

contador = 0


def incrementar():
    global contador
    for _ in range(1000000):
        time.sleep(0.0001)
        contador += 1


threads = [threading.Thread(target=incrementar) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Contador final: {contador}")
