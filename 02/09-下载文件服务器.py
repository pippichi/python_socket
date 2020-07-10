import socket
import codecs


def send_file_2_client(new_client_socket, client_addr):
	# 1. receive file path from client
	file_name = new_client_socket.recv(1024).decode("utf-8")
	print("%s by %s" % (file_name, str(client_addr)))

	# 2.open file, read data
	file_content = None
	try:
		f = codecs.open(file_name, "rb")
		file_content = f.read()
		f.close()
	except Exception as e:
		print("file not exists!")

	if file_content:
		new_client_socket.send(file_content)


def main():
	tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	tcp_server_socket.bind(("", 7890))

	tcp_server_socket.listen(128)

	while True:

		new_client_socket, client_addr = tcp_server_socket.accept()

		# file_name = new_client_socket.recv(1024).decode("utf-8")
		# print(file_name)

		# new_client_socket.send("ok".encode("utf-8"))
		send_file_2_client(new_client_socket, client_addr)

		new_client_socket.close()
		
	tcp_server_socket.close()

if __name__ == '__main__':
	main()
