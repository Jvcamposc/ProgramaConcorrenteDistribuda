import threading
import time


def saudacao(nome, tempo):
    print(f"Olá, {nome}")
    time.sleep(tempo)
    print(f"Tchau, {nome}")


A = thread = threading.Thread(target=saudacao, args=("João", 5))
B = thread = threading.Thread(target=saudacao, args=("Isabella", 2))

A.start()
B.start()
A.join()
B.join()

print("Thread principal finalizada!")
