import socket

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ("localhost", 13333)

# Send message to server
message = "Hello Server, this is Client"
client_socket.sendto(message.encode(), server_address)

# Receive reply from server
reply, server = client_socket.recvfrom(1024)
print("Reply from Server:", reply.decode())

# Close socket
client_socket.close()
