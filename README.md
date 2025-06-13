# 🔐 Password Generator (Python)

A secure and customizable **strong password generator** script built in Python. Generate high-quality passwords with options for length, character types, and readability.

---

## 📋 Table of Contents

1. [Overview](#overview)  
2. [Features](#features)  
3. [Requirements](#requirements)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Code Structure](#code-structure)  
7. [Security Notes](#security-notes)  
8. [Contributing](#contributing)  
9. [License](#license)

---

## 💡 Overview

This Python script lets users quickly generate random, secure passwords via CLI. It’s customizable and ideal for both personal use and integration into larger automation workflows.

---

## ✅ Features

- Customizable **length** (default: 16 characters)  
- Mix of **uppercase**, **lowercase**, **digits**, and **symbols**  
- Option to **exlude similar-looking characters** (e.g., `O`, `0`, `l`, `1`)  
- Choice to **avoid ambiguous symbols** for better readability  
- Easily embeddable as a function or module in other Python projects

---

## 🧾 Requirements

- **Python 3.7+**  
- No external dependencies—just the Python standard library

---

## ⚙️ Installation

```bash
git clone https://github.com/MisaghMomeniB/Password-Generator-Python.git
cd Password-Generator-Python
python3 --version  # ensure Python ≥3.7
````

---

## 🚀 Usage

### CLI Example

Run the script directly with customizable options:

```bash
python3 password_generator.py --length 20 --no-ambiguous --no-similar
```

**Options:**

* `--length <int>`: Set password length (default `16`)
* `--no-ambiguous`: Exclude punctuation that’s hard to read
* `--no-similar`: Skip characters like `0`, `O`, `l`, `1`
* `--count <int>`: Generate multiple passwords in one run

### As a Python Module

Import `generate_password()` in your code:

```python
from password_generator import generate_password

pwd = generate_password(length=24, no_ambiguous=True)
print("Generated password:", pwd)
```

---

## 📁 Code Structure

```
/ (root)
├── password_generator.py   # CLI script & core logic
└── README.md               # This file
```

* `generate_password()`: main function with customizable options
* `if __name__ == "__main__":` block handles CLI parsing via `argparse`

---

## 🔒 Security Notes

* Uses `secrets.SystemRandom()` for cryptographic-quality randomness
* Ensures a mix of character types by design
* Avoids insecure `random` module

---

## 🤝 Contributing

Improvements welcome! Suggested enhancements:

* Add **pronounceable password** mode
* Integrate **password strength estimation**
* GUI or web-based interface

To contribute:

1. Fork the repository
2. Create a new branch (`feature/...`)
3. Submit a detailed pull request

---

## 📄 License
