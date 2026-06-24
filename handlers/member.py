import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command, CommandObject
import json
from Telegram_Bot import utils

router = Router()

admin_list = [utils.load_roles()]
ban_list = [utils.load_banned()]

@router.message(Command('myrole'))
async def my_role(message: Message):
    print(f"Роль {message.from_user.full_name}: {utils.get_roles_name(message.from_user.id)}")
    await message.answer(f"Роль {message.from_user.full_name}: {utils.get_roles_name(message.from_user.id)}")

