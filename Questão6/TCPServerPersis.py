from socket import *
import threading

boasVindas = f"Olá! Bem-vindo! Qual o seu nome?"
servicos = "1. Agendar um horário de monitoria\n"
servicos += "2. Listar as próximas atividades da disciplina\n"
servicos += "3. E-mail do professor"
monitoria = f"Para agendar uma monitoria, basta enviar um e-mail para cainafigueiredo@poli.ufrj.br \n"
pendencias = f"Fique atento para as datas das proximas atividades. Confira o que vem por ai! \n"
pendencias += "P1: 26 de Maio de 2022\nLista3: 29 de Maio de 2022 \n"
emailProf = f"Quer falar com o professor? o e-mail dele é sadoc@dcc.ufrj.br \n"
finalizar = "Obrigado por utilizar nossos serviços!\nAté logo!"

serverPort = 12000
def recive_client_request(connectionSocket, clientAddress):
	_ =connectionSocket.recv(1024)
	connectionSocket.send(boasVindas.encode())

	name = connectionSocket.recv(1024)
	ini_servicos= f"Certo, {name.decode()}! Como posso te ajudar? Digite o numero que corresponde a opção desejada:\n"
	send_servicos = ini_servicos + servicos
	connectionSocket.send(send_servicos.encode())
	
	option = connectionSocket.recv(1024).decode()
	if option == "1":
		connectionSocket.send((monitoria + finalizar).encode())
	elif option == "2":
		connectionSocket.send((pendencias + finalizar).encode())
	elif option == "3":
		connectionSocket.send((emailProf + finalizar).encode())
	else:
		connectionSocket.send(finalizar.encode())


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