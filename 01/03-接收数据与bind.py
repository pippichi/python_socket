import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 绑定一个本地地址
    localaddr = ("",7788)
	udp_socket.bind(localaddr)  # 必须绑定自己电脑的ip以及port，其他的不行

	# 接受数据，后面的1024表示接受的数据最大的大小
	recv_data = udp_socket.recvfrom(1024)

	# recv_data这个变量中存储的是一个元组(接收到的数据，(发送方的ip,port))
	recv_msg = recv_data[0]  # 接受到的数据
	send_addr = recv_data[1]  # from address

	# 打印
	# print(recv_data)
	print("%s:%s" % (str(send_addr),recv_msg.decode("utf-8")))

	udp_socket.close()

if __name__ == '__main__':
	main()
