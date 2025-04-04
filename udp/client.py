import socket

# Create a socket object for the client (UDP)
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
addr = ('192.168.56.1', 59)

# Request a file from the server
file_request = input("Enter the filename to request from the server: ")

# Send the file request to the server
socket.sendto(file_request.encode(), addr)

# Receive the file data from the server
file_data, addr = socket.recvfrom(1024)

# Save the received data to a file prefixed with 'received_'
if file_data == b"File not found.":
    print("File not found.")
else:
    with open(f"received_{file_request}", 'wb') as f:
        f.write(file_data)
    print(f"File saved as 'received_{file_request}'")

# Close the client socket
socket.close()
