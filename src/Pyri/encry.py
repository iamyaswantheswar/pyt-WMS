from cryptography.fernet import Fernet
import getpass

# Step 1: Generate and save a key (do this only once)
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Step 2: Get password from user without showing it on screen
password = getpass.getpass("Enter password to encrypt: ")

# Step 3: Encrypt the password
cipher = Fernet(key)
encrypted = cipher.encrypt(password.encode())

# Step 4: Save the encrypted password
with open("encrypted_password.txt", "wb") as f:
    f.write(encrypted)

print("Password encrypted and saved.")
