import json
import os
from typing import Optional, Dict, Any

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
    if rank == 1:
        role_list = moderators + admin + owner
        role_list[moderators].append(append_id)
        save_roles(role_list)
        return True
    if rank == 2:
        role_list = moderators + admin + owner
        role_list[admin].append(append_id)
        save_roles(role_list)
        return True
    if rank == 3:
        role_list = moderators + admin + owner
        role_list[owner].append(append_id)
        save_roles(role_list)
        return True


"""@router.message(Command('add_admin'))
async def add_admin(message: Message, command: CommandObject):
    # command.args содержит аргументы (через пробел в команде написано)
    args = command.args
    try:
        user = message.from_user.id
        user_adding = str(args[0]) + str(args[1]) + str(args[2]) + str(args[3]) + str(args[4]) + str(args[5]) + str(args[6]) + str(args[7]) + str(args[8]) + str(args[9])
        try:
            user_adding = user_adding + str(args[10])
            rank = int(args[11])
        except:
            rank = int(args[10])
        if not user_adding and rank:
            await message.answer("Вы ничего не ввели (id юзера или ранг)")
        if utils.is_owner(user, 3):
            utils.add_admin_in_list(user, user_adding, rank)
            print(f"Добавлен админ [{user}]")
        else:
            print(f"Недостаточно прав [{user}]")
    except Exception as e:
        print("Ошибка, не верно ввели")
        print(e)"""




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
    owner = load_roles()["owners"]
    admin = load_roles()["admins"]
    moderators = load_roles()["moderators"]
    return user_id in owner or user_id in admin or user_id in moderators

def is_admin(user_id):
    admin = load_roles()["admins"]
    owner = load_roles()["owners"]
    return user_id in owner or user_id in admin

def is_owner(user_id):
    owner = load_roles()["owners"]
    return user_id in owner

def get_target(message):
    if message.reply_to_message:
        user = message.reply_to_message.from_user
        return user.id, user.full_name
    parts = message.text.split()
    if len(parts) < 2:
        return None, None
    user_name = parts[1].replace("@", "")
    return None, user_name

def get_roles_name(user_id):
    if is_owner(user_id):
        return "Владелец"
    elif is_admin(user_id):
        return "Админ"
    elif is_moderator(user_id):
        return "Модератор"
    else:
        return "Пользователь/Участник"

async def get_user_info(bot: Any, user_id: int) -> Dict[str,Any]:
    try:
        user = await bot.get_chat(user_id)

        return {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "full_name": user.full_name,}
    except Exception as e:
        return {
            "id": user_id,
            "first_name": None,
            "last_name": None,
            "username": None,
            "full_name": None}

