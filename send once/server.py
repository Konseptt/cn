import socket

# Define the server function to handle client requests
def handle_client(client_socket):
    try:
        # Receive the file request from the client
        file_request = client_socket.recv(1024).decode()
        print(f"Requested file: {file_request}")

        # Try to open the requested binary file
        try:
            with open(file_request, 'rb') as file:
                # Send the binary file content to the client in raw bytes
                file_data = file.read()
                client_socket.send(file_data)
                print(f"Sent binary file {file_request} to the client.")
        except FileNotFoundError:
            print(f"File {file_request} not found.")
            client_socket.send(b"File not found.")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        client_socket.close()  # Close the connection

# Create a socket object for the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 56))  # Bind to port 56 on all network interfaces
server_socket.listen(5)  # Listen for incoming connections
print("Server listening on port 56...")


client_socket, addr = server_socket.accept()
print(f"Accepted connection from {addr}")
# Handle the client request (one after another)
handle_client(client_socket)
print("Connection closed")
