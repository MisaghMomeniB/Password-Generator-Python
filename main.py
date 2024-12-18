import random
import string
import secrets
from datetime import datetime
from PyQt5 import QtWidgets, QtGui, QtCore

class PasswordGeneratorApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Password Generator")
        # self.setWindowIcon(QtGui.QIcon("password_icon.png"))
        self.resize(400, 300)

        # Title
        title_label = QtWidgets.QLabel("Generate Secure Passwords Easily!")
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

        # Buttons
        self.generate_button = self.create_button("Generate Password", "#4CAF50", self.generate_password)
        self.copy_button = self.create_button("Copy to Clipboard", "#008CBA", self.copy_password, enabled=False)
        self.save_button = self.create_button("Save Password to File", "#f44336", self.save_password, enabled=False)
        self.exit_button = self.create_button("Exit", "#555555", self.close)

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
        layout.addWidget(self.generate_button)
        layout.addWidget(self.password_output)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.save_button)
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
        }