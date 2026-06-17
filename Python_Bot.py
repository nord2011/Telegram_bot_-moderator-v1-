import asyncio
import random
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command, CommandObject
import json
from config import TOKEN
import utils

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

@router.message(Command('save_list'))
async def save_list(message: Message):
    user = message.from_user.id ##Айди кто написал
    if utils.is_moderator(user):
        utils.save_roles(admin_list)
        print(user)
    else:
        print(f"Недостаточно прав [{user}]")



@router.message(Command('mute'))
async def mute(message: Message, command: CommandObject):
    args = command.args
    user = message.from_user.id
    if utils.is_moderator(user):
        pass
    else:
        "Недостаточно прав"
@router.message(Command('unmute'))
async def unmute(message: Message, command: CommandObject):
    args = command.args
    user = message.from_user.id
    if utils.is_moderator(user):
        pass
    else:
        "Недостаточно прав"

@router.message(Command('ban'))
async def mute(message: Message, command: CommandObject):
    args = command.args
    user = message.from_user.id
    if utils.is_admin(user):
        pass
    else:
        "Недостаточно прав"

@router.message(Command('unban'))
async def unmute(message: Message, command: CommandObject):
    args = command.args
    user = message.from_user.id
    if utils.is_admin(user):
        pass
    else:
        "Недостаточно прав"




@router.message(F.text) #Должна быть предпоследней!
async def echo(message: Message):
    await message.answer(f"Вы написали {message.text}")


async def main():
    print("Бот запущен")
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
asyncio.run(main()) # Должна быть последней!

