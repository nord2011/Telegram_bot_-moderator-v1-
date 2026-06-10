import json
import os

from Telegram_Bot.Python_Bot import add_admin

ROLES_FILE =  "data/roles.json"
BANNED_FILE = "data/banned.json"

def load_roles():
    if not os.path.exists(ROLES_FILE):
        return {"moderators": [],"admins": [],"owner": []}
    with open(ROLES_FILE, "r") as f:
        return json.load(f)

def save_roles(roles):
    with open(ROLES_FILE, "w") as f:
        json.dump(roles, f)


def add_admin_in_list(user_id, append_id, rank):
    moderators = load_roles()["moderators"]
    admin = load_roles()["admins"]
    owner = load_roles()["owner"]
    if user_id not in owner:
        print("Недостаточно прав")
        return False
    if rank > 3 or rank == 0:
        print("Неверный ранг")
        return False
    pass


def load_banned():
    if not os.path.exists(BANNED_FILE):
        return {[]}
    with open(BANNED_FILE, "r") as f:
        return json.load(f)

def save_banned(banned):
    with open(BANNED_FILE, "w") as f:
        json.dump(banned, f)

def add_to_banned(user_id):
    banned_list = load_banned()
    if user_id not in banned_list:
        banned_list.append(user_id)
        save_banned(banned_list)
        return True
    return False

def remove_from_banned(user_id):
    banned_list = load_banned()
    if user_id in banned_list:
        banned_list.remove(user_id)
        save_banned(banned_list)
        return True
    return False

def is_moderator(user_id):
    owner = load_roles()["owner"]
    admin = load_roles()["admins"]
    moderators = load_roles()["moderators"]
    return user_id in owner or user_id in admin or user_id in moderators

def is_admin(user_id):
    admin = load_roles()["admins"]
    owner = load_roles()["owner"]
    return user_id in owner or user_id in admin

def is_owner(user_id):
    owner = load_roles()["owner"]
    return user_id in owner

print(add_to_banned(12345))
print(load_banned())
print(add_to_banned(56789))
print(load_banned())
print(remove_from_banned(12345))
print(load_banned())
