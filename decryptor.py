import base64

def decrypt(*args):
    try:
        # Decryptor
        min_index = 0

        if __name__ == '__main__':
            file = args[0]
            key = args[1]
            max_index = len(key)
            with open(file, "rb") as f:
                encoded_message = f.read()

        else:
            key = args[0][:16]
            file = args[0][16:]
            max_index = len(key)
            encoded_message = file.encode()
        decoded_message = base64.b64decode(encoded_message)
        decrypted_message = bytearray()

        for xor_result in decoded_message:
            # Ensure the result is within the valid byte range (0-255)
            xor_result = xor_result & 0xFF
            byte = xor_result ^ ord(key[min_index])
            decrypted_message.append(byte)

            if min_index == max_index - 1:
                min_index = 0
            else:
                min_index += 1

        if __name__ == '__main__':
            with open(file, "wb") as f:
                f.write(decrypted_message)
        else:
            return decrypted_message.decode()

    except Exception as e:
        print(e)


if __name__ == '__main__':
    key = input("Enter the key: ")
    file = input("Enter the file name: ")
    decrypt(file, key)
