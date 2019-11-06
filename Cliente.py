import socket

host = 'localhost'
port = 8083

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host,port))
print("Cliente conectado.")
messenge = input()
client.send(messenge.encode())
response = client.recv(4096)
print("Recebido: ",response.decode())
client.close()