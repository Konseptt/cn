import socket
import threading  # Import threading to handle multiple clients concurrently

# Define the server function to handle client requests
def handle_client(conn):
    try:
        # Receive the file request from the client
        file_request = conn.recv(1024).decode()
        print(f"Requested file: {file_request}")

        # Try to open the requested file
        try:
            with open(file_request, 'rb') as file:
                # Send the file content to the client in raw bytes
                file_data = file.read()
                conn.send(file_data)
                print(f"Sent file {file_request} to the client.")
        except FileNotFoundError:
            print(f"File {file_request} not found.")
            conn.send(b"File not found.")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        conn.close()  # Close the connection

# Create a socket object for the server
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('0.0.0.0', 57))  # Bind to port 57 on all network interfaces
socket.listen(5)  # Listen for incoming connections
print("Server listening on port 57...")

# Accept and handle incoming client connections concurrently
while True:
    conn, addr = socket.accept()
    print(f"Accepted connection from {addr}")
    # Use a new thread to handle each client
    client_thread = threading.Thread(target=handle_client, args=(conn,))
    client_thread.start()
