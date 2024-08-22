import socket
import threading
import decryptor


def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                decrypted_message = decryptor.decrypt(message)
                print(f"Received: {decrypted_message}")

                # Send acknowledgment back to the sender
                acknowledgment = "Message received successfully"
                client_socket.send(acknowledgment.encode('utf-8'))
            else:
                break
        except ConnectionResetError:
            break

    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))  # Bind to all interfaces on port 9999
    server.listen(5)  # Listen for incoming connections

    print("Server listening on port 9999...")

    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(target=handle_client, args=(client_socket,), daemon=True)
        client_handler.start()


if __name__ == "__main__":
    start_server()


