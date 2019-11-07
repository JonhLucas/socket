import socket

address = ("localhost", 20000)
# Create sockets
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	client.connect(address)
	print("Cliente conectado.")
except socket.error:
	print("Falha na conexao")

# Echo
while True:
	print("Informe texto ou digite 'sair' para desconectar: ")
	text = input()
	try:
		client.send(text.encode())
	except socket.error:
		print("Falha ao enviar")
	if (text != "sair"):
		response = client.recv(4096)
		print(response.decode())	
	else:
		break	
		