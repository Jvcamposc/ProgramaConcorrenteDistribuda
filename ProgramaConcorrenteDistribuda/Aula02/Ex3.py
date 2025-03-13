import threading
import time


def tarefa():
    print("Incio...")
    time.sleep(2)
    print("Fim...")
    # Bloco principal (main)


tA = threading.Thread(target=tarefa)
tB = threading.Thread(target=tarefa)

tA.start()
tB.start()
tA.join()
tB.join()

print("Thread principal finalizada!")
