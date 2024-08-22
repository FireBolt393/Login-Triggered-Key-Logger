import socket
import time
import os
from threading import Thread as t

# Define the path for storing messages
MESSAGE_FILE = 'messages.txt'


def load_messages():
    if os.path.exists(MESSAGE_FILE):
        with open(MESSAGE_FILE, 'r') as file:
            return file.readlines()
    return []


def save_message(message):
    with open(MESSAGE_FILE, 'a') as file:
        file.write(message + '\n')


def clear_messages():
    if os.path.exists(MESSAGE_FILE):
        os.remove(MESSAGE_FILE)


def check_listener():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)  # Set a timeout for the connection attempt
            sock.connect(('127.0.0.1', 9999))
            # print("Listener is online.")
            return True
    except (socket.timeout, ConnectionRefusedError):
        # print("Listener is offline.")
        return False


def sendMessage(message):

    if check_listener():
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.connect(('127.0.0.1', 9999))
                sock.sendall(message.encode('utf-8'))
                # print("Message sent successfully!")
                acknowledgment = sock.recv(1024).decode('utf-8')

        except ConnectionResetError:
            # print('Listener is Offline, writing the data to file.')
            save_message(message)
            if not retry.is_alive():
                retry.start()


def sendSavedMessages():
    s = False
    message = load_messages()
    clear_messages()
    if message:
        for m in message:
            sendMessage(m)

    return s


def tryAgain():
    while not check_listener():
        # print("Retrying...")
        time.sleep(1)

    else:
        sendSavedMessages()


def dataToBeTransmitted(m):
    global retry
    retry = t(target=tryAgain, daemon=True)

    if check_listener():
        sendSavedMessages()
        clear_messages()

    else:
        if not retry.is_alive():
            retry.start()
# for testing

# import encryptor
# while True:
#     m = input('Enter message: ')
#     if m == 'q':
#         break
#     m = encryptor.encrypt(m)
#     m = m[1] + m[0]

    if check_listener():
        sendMessage(m)

    else:
        save_message(m)
        if not retry.is_alive():
            retry.start()

