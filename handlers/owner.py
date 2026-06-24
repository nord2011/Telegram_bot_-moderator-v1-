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
async def roles(message: Message, bot: Bot):
    loaded_roles = utils.load_roles()
    chat_id = message.chat.id
    print(loaded_roles)
    list_roles = f"Список админов:"
    a = 1
    for role in loaded_roles["owners"]:
        user_data = await utils.get_user_info(bot,chat_id,role)
        print(user_data)
        list_roles += f"\n{a}. [{user_data["full_name"]}](tg://user?id={role}) Владелец"
        a += 1
    for role in loaded_roles["admins"]:
        user_data = await utils.get_user_info(bot,chat_id,role)
        print(user_data)
        list_roles += f"\n{a}. [{user_data["full_name"]}](tg://user?id={role}) Админ"
        a += 1

    for role in loaded_roles["moderators"]:
        user_data = await utils.get_user_info(bot,chat_id,role)
        print(user_data)
        list_roles += f"\n{a}. [{user_data["full_name"]}](tg://user?id={role}) Модератор"
        a += 1



    print(list_roles)
    await message.answer(list_roles, parse_mode='Markdown')

