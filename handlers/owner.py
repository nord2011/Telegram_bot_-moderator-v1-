import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command, CommandObject
import json
from Telegram_Bot import utils


router = Router()

@router.message(Command('myrole'))
async def my_role(message: Message):
    print(f"Роль {message.from_user.full_name} {utils.get_roles_name(message.from_user.id)}")
    await message.answer(f"Роль {message.from_user.full_name} {utils.get_roles_name(message.from_user.id)}")

@router.message(Command("roles"))
async def roles(message: Message):
    list_roles = utils.load_roles()
    print(f"Владелец(ы): \n {list_roles["owners"]}")
    print(f"Администраторы: \n {list_roles["admins"]}")
    print(f"Модераторы: \n {list_roles['moderators']}")
    await message.answer(f"[Назар](tg://user?id={list_roles["owners"][0]})", parse_mode='MarkdownV2')
