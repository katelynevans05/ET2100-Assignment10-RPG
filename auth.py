import hashlib
import secrets
import getpass
from database import get_user, create_user

def digest(salt, password):
    return hashlib.sha256((salt + password).encode()).hexdigest()

def password_input():
    try:
        return getpass.getpass("Password: ")
    except (EOFError, KeyboardInterrupt):
        raise

def authenticate():
    while True:
        choice = input("[R]egister, [L]ogin, or [Q]uit: ").strip().lower()
        if choice == "q":
            return None
        if choice not in ("r", "l"):
            print("Please choose R, L, or Q.")
            continue
        username = input("Username: ").strip().lower()
        if not (3 <= len(username) <= 20 and username.isalnum()):
            print("Username must be 3-20 letters/numbers.")
            continue
        user = get_user(username)
        if choice == "r":
            if user:
                print("That username is taken.")
                continue
            password = password_input()
            if len(password) < 4:
                print("Password must have at least 4 characters.")
                continue
            salt = secrets.token_hex(16)
            create_user(username, salt, digest(salt, password))
            print("Account created!")
            return username
        if not user:
            print("Account not found.")
            continue
        if digest(user["salt"], password_input()) == user["password_hash"]:
            print("Login successful!")
            return username
        print("Incorrect password.")
