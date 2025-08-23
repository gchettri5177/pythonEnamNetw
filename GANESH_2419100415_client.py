import socket

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 55555

def query_arp(ip_address):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM for TCP protocol
    client_socket.connect((SERVER_HOST, SERVER_PORT))
    client_socket.send(ip_address.encode())
    response = client_socket.recv(1024).decode()
    client_socket.close()
    return response

#client program entry point
if __name__ =="__main__":
    ip = input("Enter IP to check: ")
    print(query_arp(ip))

