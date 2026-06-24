import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command, CommandObject
import json
from Telegram_Bot import utils
from Telegram_Bot.config import TOKEN

router = Router()

admin_list = [utils.load_roles()]
ban_list = [utils.load_banned()]

@router.message(Command('add_admin'))
async def add_admin(message: Message):
    pass
@router.message(Command('remove_admin'))
async def add_admin(message: Message):
    pass

@router.message(Command('save_list'))
async def save_list(message: Message):
    user = message.from_user.id ##Айди кто написал
    if utils.is_owner(user):
        utils.save_roles(admin_list)
        print(user)
    else:
        print(f"Недостаточно прав [{user}]")

@router.message(Command("roles"))
async def roles(message: Message):
    loaded_roles = utils.load_roles()
    list_roles = f"Список админов:"
    a = 1
    for member in loaded_roles:
        user_data = utils.get_user_info(member, TOKEN)
        if utils.get_roles_name(member) == "Владелец":
            list_roles =+ f"\n{a}. [{user_data["first_name"]}](tg://user?id={member}) Владелец"
            a += 1
            return
        if utils.get_roles_name(member) == "Админ":
            list_roles += f"\n{a}. [{user_data["first_name"]}](tg://user?id={member}) Админ"
            a += 1
            return
        if utils.get_roles_name(member) == "Модератор":
            list_roles += f"\n{a}. [{user_data["first_name"]}](tg://user?id={member}) Модератор"
            a += 1
            return
    print(list_roles)
    await message.answer(list_roles, parse_mode='MarkdownV2')

