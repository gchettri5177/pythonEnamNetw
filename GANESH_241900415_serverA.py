import socket

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ("localhost", 13333)

# Bind socket to address
server_socket.bind(server_address)

print("UDP Server is running on port 13333...")
print("Waiting for client message...\n")

while True:
    # Receive message from client
    message, client_address = server_socket.recvfrom(1024)
    print(f"Message from Client {client_address}: {message.decode()}")

    # Reply to client
    reply = "Message received by server"
    server_socket.sendto(reply.encode(), client_address)
