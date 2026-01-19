import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(("localhost", 12345))

# Message in required format
message = "GANESH_201900415"

# Send message to server
client_socket.send(message.encode())

# Receive echoed message from server
reply = client_socket.recv(1024).decode()
print("Message echoed from server:", reply)

# Close socket
client_socket.close()
