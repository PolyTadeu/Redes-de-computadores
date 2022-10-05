from socket import *
import threading

serverPort = 12000
def recive_client_request(connectionSocket, clientAddress):
	while True:
		message = connectionSocket.recv(2048)
		if not message:
			print(str(clientAddress) + " end his session.")
			connectionSocket.close()
			return
		print(f"{clientAddress} client send: {message.decode()}")


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