import socket

# Create a socket object for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server at IP 192.168.56.1 and port 55
client_socket.connect(('192.168.56.1', 57))

# Request a text file from the server
file_request = input("Enter the filename to request from the server: ")
client_socket.send(file_request.encode())  # Send the file request

# Receive the file data from the server
file_data = client_socket.recv(1024)

# Save the received data to a file prefixed with 'received_'
if file_data == b"File not found.":
    print("File not found.")
else:
    with open(f"received_{file_request}", 'wb') as f:
        f.write(file_data)
    print(f"File saved as 'received_{file_request}'")

# Close the client socket
client_socket.close()
