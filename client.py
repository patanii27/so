import socket

def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    server_address = ('127.0.0.1', 8080)
    client_socket.connect(server_address)
    print(f"Connected to server at {server_address}")

    try:
        # Input two numbers from the user
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        # Send the numbers to the server
        message = f"{num1} {num2}"
        client_socket.sendall(message.encode('utf-8'))

        # Receive the response from the server
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Server response: {response}")
    finally:
        # Clean up the connection
        client_socket.close()

if __name__ == "__main__":
    start_client()