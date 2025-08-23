import socket

HOST = "0.0.0.0"
PORT = 55555
# simple ARP table
arp_table = {
        "192.168.1.10": "AA:BB:CC:DD:EE:01",
        "192.168.1.20": "AA:BB:CC:DD:EE:02",
        "192.168.1.30": "AA:BB:CC:DD:EE:03",
}

#main server function
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM for TCP protocol
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print("ARP Server is running...")

    while True:
        client_socket, addr = server_socket.accept()
        ip_request = client_socket.recv(1024).decode().strip()

        if ip_request in arp_table:
            mac = arp_table[ip_request]
            response = f"MAC Address of {ip_request}:: {mac}"
        else: 
            response = "No IP found in ARP table."

        client_socket.send(response.encode())
        client_socket.close()

# program entry point
if __name__ == " __main__":
     run_server()
     