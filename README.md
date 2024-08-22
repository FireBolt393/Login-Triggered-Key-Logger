# Login-Triggered-Key-Logger
**CyberSpy** is a Python-based keylogger designed to activate when a login page is detected on the user's screen. The tool captures keystrokes only when specific keywords associated with login forms, such as "username" or "password," are detected on the screen. This project is intended for educational purposes, demonstrating how a targeted keylogger can be developed and used in ethical hacking simulations or penetration testing scenarios.

## Features
**Targeted Activation:** The keylogger remains dormant until it detects a login page, ensuring that only sensitive information such as usernames and passwords are captured.
Screen Monitoring: Continuously monitors the screen for specific keywords associated with login forms.

**Customizable Keywords:** Easily modify the keywords that trigger the keylogger to match different login pages.
Encrypted Data Transmission: Captured keystrokes can be transmitted securely to a remote server using encryption, preventing interception by unauthorized parties.

**Acknowledgment Mechanism:** The system can confirm the server's successful receipt of the data, ensuring that no data is lost.

**Cross-Platform Compatibility:** Works on Windows, macOS, and Linux.

## How It Works
**Screen Monitoring:** The tool continuously captures the screen and extracts text using OCR (Optical Character Recognition) technology.

**Keyword Detection:** The extracted text is analyzed to detect specific login-related keywords such as "login," "username," or "password."

**Keylogging Activation:** Upon detecting these keywords, the keylogger activates and starts recording all keystrokes.

**Data Transmission:** The captured keystrokes are then encrypted and sent to a remote server or stored locally, depending on the configuration.

**Acknowledgment:** After sending the data, the listener sends back an acknowledgment to confirm successful delivery.

## Prerequisites
Python 3.x
`pytesseract` for OCR (Optical Character Recognition)

`opencv-python` for screen capture

`socket` for network communication

`threading` for handling multiple connections

`Tesseract-OCR` installed (required by pytesseract)

`keyboard` for logging the keys pressed by the victim.

Make sure to install the compiled version of Tesseract-OCR and provide the right path in the script. 

## Usage
**Modify Keywords:** Customize the list of keywords in the find_login_keywords function to match the specific login forms you want to target.

**Encryption Configuration:** Feel free to use an encryption of your own.

**Server Setup:** run listener.py to start the server. The spyware stores the encrypted captured data on the victim's device. Once the server starts, if the victim's machine is active, it sends the stored data to the server.

## Legal Disclaimer
This project is for educational purposes only. Unauthorized use of keyloggers to capture sensitive information is illegal and unethical. Ensure that you have explicit permission before using this tool in any environment. The creators of this tool are not responsible for any misuse or damage caused by this software.

## Contributing
Contributions are welcome! If you have ideas to improve the tool or fix bugs, feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
