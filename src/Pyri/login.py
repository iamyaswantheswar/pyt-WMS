import hashlib
import json
from pathlib import Path
import tkinter as tk
from tkinter import messagebox
from typing import Optional, Dict, Any
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoginSystem:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self.users_file = data_dir / "users.json"
        self.admin_file = data_dir / "admin.hash"
        self._ensure_data_files_exist()

    def _ensure_data_files_exist(self) -> None:
        """Ensure required data files and directories exist."""
        try:
            self.data_dir.mkdir(parents=True, exist_ok=True)
            if not self.users_file.exists():
                self.users_file.write_text("{}")
            if not self.admin_file.exists():
                self.set_admin_password("admin")  # Default admin password
        except Exception as e:
            logger.error(f"Failed to initialize data files: {e}")
            raise

    def _hash_password(self, password: str) -> str:
        """Hash a password for storing."""
        return hashlib.sha256(password.encode()).hexdigest()

    def verify_admin(self, password: str) -> bool:
        """Verify admin password."""
        try:
            stored_hash = self.admin_file.read_text().strip()
            return self._hash_password(password) == stored_hash
        except Exception as e:
            logger.error(f"Error verifying admin: {e}")
            return False

    def set_admin_password(self, new_password: str) -> None:
        """Set a new admin password."""
        try:
            hashed = self._hash_password(new_password)
            self.admin_file.write_text(hashed)
        except Exception as e:
            logger.error(f"Error setting admin password: {e}")
            raise

    def add_user(self, username: str, password: str) -> bool:
        """Add a new user."""
        try:
            users = self._load_users()
            if username in users:
                return False
            users[username] = self._hash_password(password)
            self._save_users(users)
            return True
        except Exception as e:
            logger.error(f"Error adding user: {e}")
            return False

    def verify_user(self, username: str, password: str) -> bool:
        """Verify user credentials."""
        try:
            users = self._load_users()
            if username not in users:
                return False
            return users[username] == self._hash_password(password)
        except Exception as e:
            logger.error(f"Error verifying user: {e}")
            return False

    def _load_users(self) -> Dict[str, str]:
        """Load users from the JSON file."""
        try:
            return json.loads(self.users_file.read_text())
        except json.JSONDecodeError:
            return {}

    def _save_users(self, users: Dict[str, str]) -> None:
        """Save users to the JSON file."""
        self.users_file.write_text(json.dumps(users, indent=2))


class LoginWindow:
    def __init__(self, login_system: LoginSystem):
        self.login_system = login_system
        self.root = tk.Tk()
        self._setup_ui()

    def _setup_ui(self):
        self.root.title("Warehouse Management System - Login")
        self.root.geometry("400x300")
        self.root.configure(bg="white")

        # Center the window
        window_width = 400
        window_height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width / 2 - window_width / 2)
        center_y = int(screen_height / 2 - window_height / 2)
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # Add UI elements
        self._create_widgets()

    def _create_widgets(self):
        # Title
        title = tk.Label(
            self.root,
            text="Warehouse Management System",
            font=("Arial", 16, "bold"),
            bg="white"
        )
        title.pack(pady=20)

        # Username
        tk.Label(self.root, text="Username:", bg="white").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        # Password
        tk.Label(self.root, text="Password:", bg="white").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack(pady=5)

        # Login Button
        login_btn = tk.Button(
            self.root,
            text="Login",
            command=self._handle_login,
            width=15
        )
        login_btn.pack(pady=20)

        # Admin Button
        admin_btn = tk.Button(
            self.root,
            text="Admin Login",
            command=self._show_admin_login,
            width=15
        )
        admin_btn.pack()

        # Bind Enter key to login
        self.root.bind('<Return>', lambda e: self._handle_login())

    def _handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Both username and password are required")
            return

        if self.login_system.verify_user(username, password):
            messagebox.showinfo("Success", "Login successful!")
            # Proceed to main application
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def _show_admin_login(self):
        # Implementation for admin login popup
        pass

    def run(self):
        self.root.mainloop()

base_path = Path(__file__).parent.parent.parent
data_dir = base_path / "data"
login_system = LoginSystem(data_dir)
app = LoginWindow(login_system)
app.run()