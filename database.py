from tinydb import TinyDB, Query
from pathlib import Path
DB = TinyDB(str(Path(__file__).with_name("saves.json")))
USERS = DB.table("users")
User = Query()
def get_user(username):
    return USERS.get(User.username == username)
def create_user(username, salt, password_hash):
    USERS.insert({"username": username, "salt": salt, "password_hash": password_hash, "progress": None})
def save_user(username, player):
    USERS.update({"progress": player.to_dict()}, User.username == username)
