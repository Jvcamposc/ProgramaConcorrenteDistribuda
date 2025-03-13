# Verificar o número de processadores logicos
# Exemplo 1
import os
NumProcessadores = os.cpu_count()
print(f"Numero de Processadores lógicos: {NumProcessadores}")

# Verificar o número de processadores fisicos
# Exemplo 2
import threading
import time
def tarefa():
    print("Incio...")
    time.sleep(2)
    print("Fim...")

# Blocoo principal (main)
thead = threading.Thread(target=tarefa)
thead.start()  # Inicia a thread
thead.join()  # Aguarda a concluão da thread
print("Thread principal finalizada")

