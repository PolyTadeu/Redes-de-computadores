from socket import *
import threading

user = 'polyana'
password = 'aluno'
sucessMessage = 'Login realizado com sucesso!'
errorMessage = 'Error: Incorrect username or password.'
serverPort = 12000
def recive_client_request(connectionSocket, clientAddress):
	while True:
		sentence = connectionSocket.recv(1024)
		if not sentence:
			print(str(clientAddress) + " end his session.")
			connectionSocket.close()
			return
		login = sentence.decode().split('/')
		if (login[0]==user) and (login[1]==password):
			connectionSocket.send(sucessMessage.encode())
		else:
			connectionSocket.send(errorMessage.encode())


def main():
	serverSocket = socket(AF_INET, SOCK_STREAM)
	serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	serverSocket.bind(("", serverPort))
	serverSocket.listen(1)
	print("The server is ready to receive")
	while True:
		client = threading.Thread(target=recive_client_request, args=serverSocket.accept())
		client.start()
	serverSocket.close()

main()