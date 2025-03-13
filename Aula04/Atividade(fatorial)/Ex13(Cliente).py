#Cliente

import socket
def iniciar_cliente():
    HOST = '127.0.0.1' #IPv4 (4 blocos de 8 bits)
    PORT = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as S:
        S.connect((HOST, PORT))
        print("Solicitando fatorial...")

        S.sendall(b"fatorial")
        data = S.recv(1024)

        if data.decode() == "numero":
            Numero = input(">> ")
            S.sendall(Numero.encode())
            data = S.recv(1024)   
            print(f"Resposta do servidor: {data.decode()}")
if __name__ == "__main__":
    iniciar_cliente()
        