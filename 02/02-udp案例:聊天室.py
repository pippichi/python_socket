import socket

def send_msg(udp_socket):
    """发送信息"""
    # 获取要发送的内容
    dest_ip = input("dest ip: ")
    dest_port = int(input("dest port"))
    send_data = input("your msg: ")
    udp_socket.send_to(send_data.encode("utf-8"),(dest_ip,dest_port))

def recv_msg(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))

def main():
    # 创建socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定ip
    udp_socket.bind(("",7799))

    # 用循环来进行
    while True: 
        # 发送
        # 获取要发送的内容
        send_msg(udp_socket)
        #  接收并显示
        recv_msg(udp_socket)

if __name__ == "__main__":
    main()
