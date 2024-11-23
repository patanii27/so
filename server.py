import socket

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_address = ('127.0.0.1', 8080)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server is listening on {server_address}...")

    while True:
        # Wait for a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        try:
            # Receive data from the client
            data = client_socket.recv(1024).decode('utf-8')
            print(f"Received: {data}")

            # Process the data (expecting two numbers separated by a space)
            try:
                num1, num2 = map(int, data.split())
                result = num1 + num2
                response = f"The sum is: {result}"
            except ValueError:
                response = "Error: Please send two integers separated by a space."

            # Send the result back to the client
            client_socket.sendall(response.encode('utf-8'))
        finally:
            # Clean up the connection
            client_socket.close()

if __name__ == "__main__":
    start_server()
