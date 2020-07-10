import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 发送数据，必须是二进制或者utf8格式
    # udp_socket.sendto(b"scorn",("192.168.33.53",8080))
    # 在发送数据的时候显然我们没有指定端口，那么这个时候windows会给他一个随机的端口，而且每次关开机之后这个端口都不一样（注意：这个端口的范围在1025-65535之间）
    while True:
	    send_data = input("tell me what you want to say:")

	    if send_data == 'exit':
	    	break

	    udp_socket.sendto(send_data.encode("utf-8"),("192.168.33.53",8080))

	udp_socket.close()

if __name__ == '__main__':
	main()
