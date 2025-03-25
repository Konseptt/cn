import socket
import threading

def handle_client(server_socket, addr, data):
    try:
        print(f"Client {addr} connected to server.")
        
        file_request = data.decode()
        print(f"Requested file: {file_request} from {addr}")

        try:
            with open(file_request, 'rb') as file:
                file_data = file.read()
                server_socket.sendto(file_data, addr)
                print(f"Sent file {file_request} to {addr}.")
        except FileNotFoundError:
            print(f"File {file_request} not found.")
            server_socket.sendto(b"File not found.", addr)

    except Exception as e:
        print(f"Error: {e}")

# Create and bind the socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(('0.0.0.0', 59))
print("Server listening on port 59...")

# Main loop
while True:
    data, addr = server_socket.recvfrom(1024)
    client_thread = threading.Thread(target=handle_client, args=(server_socket, addr, data))
    client_thread.start()
