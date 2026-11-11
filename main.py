from colorama import init
from auth import authenticate
from database import get_user
from player import Player
from game import play

def main():
    init(autoreset=True)
    print("=== THE LOST KINGDOM 2 ===")
    username = authenticate()
    if username is None:
        print("Goodbye!")
        return
    user = get_user(username)
    player = Player(username, user.get("progress"))
    play(username, player)

if __name__ == "__main__":
    main()
