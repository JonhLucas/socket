import socket
import threading

host = 'localhost'
port = 8083
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)
print("Socket criado:", host,",", port)

def handle_cliente(socket_cliente):
    request = socket_cliente.recv(1024)
    print("Recebido: ", request.decode())
    mensage = "Mensagem destinada aos cliente\n"
    socket_cliente.send(mensage.encode())
    flag = 'Confirmacao de recebimento:'
    socket_cliente.send(flag.encode())
    socket_cliente.close()

while True:
    client, add = server.accept()
    print("Conexao aceita:", add[0],",", add[1])
    client_handler = threading.Thread(target=handle_cliente, args=(client, ))
    client_handler.start()
server.close()
