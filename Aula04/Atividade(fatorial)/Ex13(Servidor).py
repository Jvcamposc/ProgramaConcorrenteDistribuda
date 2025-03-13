#SERVIDOR 

import socket 
from datetime import datetime

def iniciar_servidor():

    HOST = '127.0.0.1' #IPv4 (4 blocos de 8 bits)
    PORT = 65432

    #Criando o socket TCP / IP

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.bind((HOST, PORT)) # Vincular o socket ao endereço e porta    
        S.listen()
        print(f"Servidor iniciado em {HOST}:{PORT}")

        while True:
            conn, addr = S.accept()
            with conn:
                print(f"Conectado por {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data: 
                        break
                    
                    if data.decode().strip().lower() == "fatorial":
                        resposta = "numero"
                        conn.sendall(resposta.encode())

                        data = conn.recv(1024)
                        N = int(data.decode())

                        print(f"O numero recebido e {N}")
                        Fatorial = 1

                        for i in range(1, N + 1):
                            Fatorial = Fatorial * i

                        resposta = f"O fatorial de {N} e {Fatorial}"
                        conn.sendall(resposta.encode())
                        print(f"Fatorial enviado.")
                    else: 
                        conn.sendall("Mensagem inválida")
if __name__ == "__main__":
    iniciar_servidor()
