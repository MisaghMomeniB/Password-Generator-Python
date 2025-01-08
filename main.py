import random
import string
import secrets
import base64
import hashlib
from datetime import datetime
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QColor

class PasswordGeneratorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.password_history = []  # Store generated passwords

    def setup_ui(self):
        self.setWindowTitle("Advanced Password Generator")
        self.resize(500, 350)

        # Title
        title_label = QtWidgets.QLabel("Generate Secure and Memorable Passwords")
        title_label.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        title_label.setAlignment(QtCore.Qt.AlignCenter)

        # Password length
        length_label = QtWidgets.QLabel("Password Length:")
        self.length_input = QtWidgets.QSpinBox(minimum=4, value=12)
        self.length_input.setFont(QtGui.QFont("Arial", 10))

        # Checkboxes
        self.uppercase_checkbox = self.create_checkbox("Include Uppercase Letters", True)
        self.digits_checkbox = self.create_checkbox("Include Digits", True)
        self.symbols_checkbox = self.create_checkbox("Include Symbols", True)
        self.exclude_similar_checkbox = self.create_checkbox("Exclude Similar-Looking Characters", False)
        self.memorable_checkbox = self.create_checkbox("Generate Memorable Password", False)
        self.passphrase_checkbox = self.create_checkbox("Use Passphrase", False)

        # Buttons
        self.generate_button = self.create_button("Generate Password", "#4CAF50", self.generate_password)
        self.copy_button = self.create_button("Copy to Clipboard", "#008CBA", self.copy_password, enabled=False)
        self.save_button = self.create_button("Save Password to File", "#f44336", self.save_password, enabled=False)
        self.exit_button = self.create_button("Exit", "#555555", self.close)
        self.reset_button = self.create_button("Reset", "#FF5722", self.reset_fields)

        # Password strength indicator
        self.strength_label = QtWidgets.QLabel("Password Strength: Weak")
        self.strength_label.setFont(QtGui.QFont("Arial", 10))

        # Password output
        self.password_output = QtWidgets.QLineEdit()
        self.password_output.setReadOnly(True)
        self.password_output.setPlaceholderText("Your password will appear here")
        self.password_output.setFont(QtGui.QFont("Courier New", 12))

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(title_label)
        layout.addWidget(length_label)
        layout.addWidget(self.length_input)
        layout.addWidget(self.uppercase_checkbox)
        layout.addWidget(self.digits_checkbox)
        layout.addWidget(self.symbols_checkbox)
        layout.addWidget(self.exclude_similar_checkbox)
        layout.addWidget(self.memorable_checkbox)
        layout.addWidget(self.passphrase_checkbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.strength_label)
        layout.addWidget(self.password_output)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.reset_button)
        layout.addWidget(self.exit_button)

        self.setLayout(layout)

    def create_checkbox(self, text, checked=False):
        checkbox = QtWidgets.QCheckBox(text)
        checkbox.setChecked(checked)
        return checkbox
    
    def create_button(self, text, color, callback, enabled=True):
        button = QtWidgets.QPushButton(text)
        button.setStyleSheet(f"background-color: {color}; color: white; padding: 10px;")
        button.setEnabled(enabled)
        button.clicked.connect(callback)
        return button
    
    def generate_password(self):
        length = self.length_input.value()
        options = {
            "use_uppercase": self.uppercase_checkbox.isChecked(),
            "use_digits": self.digits_checkbox.isChecked(),
            "use_symbols": self.symbols_checkbox.isChecked(),
            "exclude_similar": self.exclude_similar_checkbox.isChecked(),
            "memorable": self.memorable_checkbox.isChecked(),
            "passphrase": self.passphrase_checkbox.isChecked(),
        }

        try:
            password = self.create_password(length, **options)
            self.password_output.setText(password)
            self.copy_button.setEnabled(True)
            self.save_button.setEnabled(True)
            self.check_password_strength(password)
            self.password_history.append(password)
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def create_password(self, length, use_uppercase, use_digits, use_symbols, exclude_similar, memorable, passphrase):
        # Define character sets
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase if use_uppercase else ''
        digits = string.digits if use_digits else ''
        symbols = string.punctuation if use_symbols else ''

        # Exclude similar characters if needed
        if exclude_similar:
            similar_chars = "il1Lo0O"
            lowercase_letters = ''.join(ch for ch in lowercase_letters if ch not in similar_chars)
            uppercase_letters = ''.join(ch for ch in uppercase_letters if ch not in similar_chars)
            digits = ''.join(ch for ch in digits if ch not in similar_chars)
            symbols = ''.join(ch for ch in symbols if ch not in similar_chars)

        all_characters = lowercase_letters + uppercase_letters + digits + symbols
        if not all_characters:
            raise ValueError("At least one character set must be enabled.")

        password = []
        if passphrase:
            words = ["apple", "banana", "cherry", "delta", "eagle", "falcon", "grape", "hero"]
            while len(password) < length:
                word = secrets.choice(words)
                if len(password) + len(word) <= length:
                    password.extend(word)
        else:
            password.extend(self.ensure_minimum_characters(use_uppercase, use_digits, use_symbols, lowercase_letters, uppercase_letters, digits, symbols))
            while len(password) < length:
                password.append(secrets.choice(all_characters))

        random.shuffle(password)
        return ''.join(password)

    def ensure_minimum_characters(self, use_uppercase, use_digits, use_symbols, lowercase, uppercase, digits, symbols):
        password = []
        if use_uppercase:
            password.append(secrets.choice(uppercase))
        if use_digits:
            password.append(secrets.choice(digits))
        if use_symbols:
            password.append(secrets.choice(symbols))
        password.append(secrets.choice(lowercase))
        return password

    def check_password_strength(self, password):
        length = len(password)
        if length < 8:
            self.strength_label.setText("Password Strength: Weak")
        elif length < 12:
            self.strength_label.setText("Password Strength: Medium")
        else:
            self.strength_label.setText("Password Strength: Strong")

    def copy_password(self):
        password = self.password_output.text()
        if password:
            QtWidgets.QApplication.clipboard().setText(password)
            QtWidgets.QMessageBox.information(self, "Copied", "Password copied to clipboard!")

    def save_password(self):
        password = self.password_output.text()
        if password:
            with open("generated_passwords.txt", "a") as file:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                file.write(f"{timestamp}: {password}\n")
            QtWidgets.QMessageBox.information(self, "Saved", "Password saved to 'generated_passwords.txt'.")

    def reset_fields(self):
        self.password_output.clear()
        self.length_input.setValue(12)
        self.uppercase_checkbox.setChecked(True)
        self.digits_checkbox.setChecked(True)
        self.symbols_checkbox.setChecked(True)
        self.exclude_similar_checkbox.setChecked(False)
        self.memorable_checkbox.setChecked(False)
        self.passphrase_checkbox.setChecked(False)
        self.strength_label.setText("Password Strength: Weak")
        self.copy_button.setEnabled(False)
        self.save_button.setEnabled(False)

    # Add additional functionality for cloud storage, hashing, or Base64 conversion if required.

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = PasswordGeneratorApp()
    window.show()
    app.exec_()