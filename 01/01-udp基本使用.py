import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 发送数据，必须是二进制或者utf8格式
    # udp_socket.sendto(b"scorn",("192.168.33.53",8080))

    send_data = input("tell me what you want to say:")

    udp_socket.sendto(send_data.encode("utf-8"),("192.168.33.53",8080))

    udp_socket.close()

if __name__ == '__main__':
	main()
