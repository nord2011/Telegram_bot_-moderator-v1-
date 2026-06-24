import asyncio
import random
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command, CommandObject
import json
from config import TOKEN

import utils
from Telegram_Bot.handlers import owner, admin, moderator, member

router = Router()


admin_list = [utils.load_roles()]
ban_list = [utils.load_banned()]



@router.message(Command('start'))
async def start(message: Message):
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}")

@router.message(Command("help"))
async def help(message: Message):
    text = """
    Я умею:
    ○ /start - Запуск/Перезапуск бота
    ○ /help - Список команд бота
    ○ /random - Генерация числа"""
    await message.answer(text)

@router.message(Command('random'))
async def random_number(message: Message):
    text = random.randint(1, 100)
    await message.answer(f"Случайное число: {text}")












"""@router.message(F.text) #Должна быть предпоследней!
async def echo(message: Message):
    await message.answer(f"Вы написали {message.text}")"""


async def main():
    print("Бот запущен")
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(owner.router)
    dp.include_router(admin.router)
    dp.include_router(moderator.router)
    dp.include_router(member.router)
    await dp.start_polling(bot)
asyncio.run(main()) # Должна быть последней!

