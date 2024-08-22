import random
import base64

# this is the same encryptor that i have built before.
def encrypt(file):
    try:

        # Generate a random key
        chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        random.shuffle(chars)
        key = "".join(chars[1:17])

        min_index = 0
        max_index = len(key)

        if __name__ == '__main__':
            print(f"Key: {key}\n")

            with open(file, "rb") as f:
                message = f.read()
        else:
            message = file.encode()

        encrypted_message = []
        for byte in message:
            xor_result = byte ^ ord(key[min_index])
            encrypted_message.append(xor_result)

            if min_index == max_index - 1:
                min_index = 0
            else:
                min_index += 1

        # Encode the encrypted message to base64
        encoded_message = base64.b64encode(bytes(encrypted_message)).decode()

        if __name__ == '__main__':
            with open(file, "wb") as f:
                f.write(encoded_message.encode())
        else:
            return encoded_message, key

    except Exception as e:
        print(e)


if __name__ == "__main__":
    file = input("Enter the file name: ")
    encrypt(file)

