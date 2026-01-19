import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server to localhost and port
server_socket.bind(("localhost", 12345))

# Listen for incoming connections
server_socket.listen(1)

print("Server is running and waiting for client connection...")

# Accept client connection
client_socket, client_address = server_socket.accept()
print("Connected to client:", client_address)

# Receive message from client
message = client_socket.recv(1024).decode()
print("Message received from client:", message)

# Echo the same message back to client
client_socket.send(message.encode())

# Close connections
client_socket.close()
server_socket.close()
