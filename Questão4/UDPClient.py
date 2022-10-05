from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
N = input("Enter the value of N: ")
N = int(N)
for i in range(N):
    i = str(i)
    clientSocket.sendto(i.encode(),(serverName, serverPort)) 
clientSocket.close()
