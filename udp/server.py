import socket
import threading  # Import threading to handle multiple clients concurrently

# Define the server function to handle client requests
def handle_client(client_socket, client_addr):
    try:
        # Receive the file request from the client
        file_request, addr = client_socket.recvfrom(1024)
        file_request = file_request.decode()
        print(f"Requested file: {file_request} from {client_addr}")

        # Try to open the requested file
        try:
            with open(file_request, 'rb') as file:
                # Send the file content to the client in raw bytes
                file_data = file.read()
                client_socket.sendto(file_data, client_addr)
                print(f"Sent file {file_request} to {client_addr}.")
        except FileNotFoundError:
            print(f"File {file_request} not found.")
            client_socket.sendto(b"File not found.", client_addr)
    
    except Exception as e:
        print(f"Error: {e}")

# Create a socket object for the server (UDP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 59))  # Bind to port 59 on all network interfaces
print("Server listening on port 59...")

# Handle incoming client requests
while True:
    # Receive the initial request (datagram)
    data, client_addr = server_socket.recvfrom(1024)
    file_request = data.decode()
    
    print(f"Received request from {client_addr}: {file_request}")
    
    # Handle each client in a separate thread
    client_thread = threading.Thread(target=handle_client, args=(server_socket, client_addr))
    client_thread.start()
