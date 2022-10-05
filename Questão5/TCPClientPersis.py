from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort)) 
while(True):
    user = input("Enter the user: ")
    password = input("Enter the password: ")
    login = f"{user}/{password}"
    clientSocket.send(login.encode())
    message = clientSocket.recv(1024)
    print("From Server: ", message.decode())

clientSocket.close()
