import json
from pathlib import Path
from cryptography.fernet import Fernet
base_path = Path(__file__).parent.parent.parent  # Points to pyt-WMS directory

# Load the saved key
file_path = base_path / "data" / "secret.key"
with open(file_path, "rb") as key_file:
    key = key_file.read()

# Load the encrypted password
file_path = base_path / "data" / "encrypted_password.txt"
with open(file_path, "rb") as f:
    encrypted = f.read()
def check_admin(adminpass):
    # Decrypt
        cipher = Fernet(key)
        decrypted_password = cipher.decrypt(encrypted).decode()
        if adminpass == decrypted_password:
            return True    
        return False
def user_check(username):
  file_path = base_path / "data" / "users.json"
  with open(file_path, "r") as f:
      data = json.load(f)
  # Check if username already exists
  for u in data["users"]:
      if u["username"] == username:
          return False
  return True
def add_user(username, passwd):
          file_path = base_path / "data" / "users.json"
          if user_check(username):  # Check if user already exists
            with open(file_path, "r+") as g:
                data = json.load(g)
                data["users"].append({"username":username, "password": passwd})
                g.seek(0)  # Go back to beginning of file
                json.dump(data, g)
                g.truncate()# Remove any leftover content
                
def remove_user(username):
    file_path = base_path / "data" / "users.json"
    with open(file_path, "r+") as f:
        data = json.load(f)
        for u in data["users"]:
            if u["username"] == username:
                data["users"].remove(u)
                f.seek(0)  # Go back to beginning of file
                json.dump(data, f)
                f.truncate()  # Remove any leftover content
                return True
        return False
def update_user(username, passwd):
    file_path = base_path / "data" / "users.json"
    with open(file_path, "r+") as f:
        data = json.load(f)
        for u in data["users"]:
            if u["username"] == username:
                remove_user(username)
                add_user(username, passwd)
                return True
        return False    
def login_auth(username, passwd):
    file_path = base_path / "data" / "users.json"
    with open(file_path, "r") as f:
        data = json.load(f)
    for u in data["users"]:
        if u["username"] == username and u["password"] == passwd:
            return True
    return False
