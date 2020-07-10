import socket
import codecs

def main():
	# 1.initialize socket
	tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 2.get ip and port 
	dest_ip = input("input your ip: ")
	dest_port = int(input("input your port: "))
	# 3.connect server
	tcp_socket.connect((dest_ip, dest_port))
	# 4.get file name 
	download_file_name = input("enter your file name: ")
	# 5.send file name to server
	tcp_socket.send(download_file_name.encode("utf-8"))
	# 6.receive data from server
	recv_data = tcp_socket.recv(1024)
	
	if recv_data:
		# 7.save data to file
		with codecs.open("new-" + download_file_name, "wb") as f:
			f.write(recv_data)
	
	# 8.close socket
	tcp_socket.close()

if __name__ == '__main__':
	main()
