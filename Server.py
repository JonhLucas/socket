import socket
import threading

address = ("localhost", 20000)

# Create sockets
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect sockets
try:
    server_socket.bind(address)
    print("Socket criado:", address[0],",", address[1])
except socket.error:
    print("Erro: porta ocupada")
    
server_socket.listen(1)


def handle_cliente(socket_client):
    while True:
        response = socket_client.recv(1024)
        if (response.decode() == "sair"):
            print("\n -------------------------------------\n| "+"Deconexao de ",
             socket_client.getpeername(), "|\n -------------------------------------\n")
            socket_client.close()
            break
        else:
            print("Mensagem do cliente",socket_client.getpeername(),":", response.decode())
            text = "Mensagem do servidor: recebimento confirmado\n"
            socket_client.send(text.encode())

# Print
while True:
    client, add = server_socket.accept()
    print("\n --------------------------------------------\n| "+
        "Nova conexao recebida de", add[0],",", add[1], "|\n --------------------------------------------\n")
    client_handler = threading.Thread(target=handle_cliente, args=(client, ))
    client_handler.start()

