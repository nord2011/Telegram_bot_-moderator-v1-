import asyncio
import random
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command, CommandObject
import json
from config import TOKEN

router = Router()




class Admin:
    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

admin_list = [
    Admin("6415099063", 3)
]

def save_list_admin(list_admin):
    with open("Admin_list.txt", "w", encoding="utf-8") as file:
        for i in range(len(admin_list)):
            ad = admin_list[i]
            file.write(f"ad{i}\n")
            file.write(f"{ad.name}\n")
            file.write(f"{ad.rank}\n")


    print("Успешно сохранено!")

def load_list_admin():
    global admin_list
    with open("Admin_list.txt", "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

        current_admin_list = []
        for line in lines:
            if line.startswith("ad") and line[2:].isdigit():
                if len(current_admin_list) == 3:
                    name = current_admin_list[1]
                    rank = current_admin_list[2]
                    admin_list.append(Admin(name, rank))
                current_admin_list.append(line)
            else:
                current_admin_list.append(line)
        if len(current_admin_list) == 3:
            name = current_admin_list[1]
            rank = current_admin_list[2]
            admin_list.append(Admin(name, rank))
        return admin_list

def add_list_admin(user, rank):
    global admin_list
    ad = Admin(user, rank)
    admin_list.append(ad)
    save_list_admin(admin_list)


def check_admin(user, min_rank=1):
    str_user = str(user)
    for i in admin_list:
        if i.name == str_user:
            if i.rank >= min_rank:
                return i
            break

    return False

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
    if check_admin(user):
        save_list_admin(admin_list)
        print(user)
    else:
        print(f"Недостаточно прав [{user}]")

@router.message(Command('add_admin'))
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
        if check_admin(user, 3):
            add_list_admin(user_adding, rank)
            print(f"Добавлен админ [{user}]")
        else:
            print(f"Недостаточно прав [{user}]")
    except Exception as e:
        print("Ошибка, не верно ввели")
        print(e)

@router.message(Command('mute'))
async def mute(message: Message, command: CommandObject):
    args = command.args
    user = message.from_user.id
    if check_admin(user, 1):
        pass
    else:
        "Недостаточно прав"
@router.message(Command('unmute'))
async def unmute(message: Message, command: CommandObject):
    args = command.args
    user = message.from_user.id
    if check_admin(user, 1):
        pass
    else:
        "Недостаточно прав"

@router.message(Command('ban'))
async def mute(message: Message, command: CommandObject):
    args = command.args
    user = message.from_user.id
    if check_admin(user, 2):
        pass
    else:
        "Недостаточно прав"

@router.message(Command('unban'))
async def unmute(message: Message, command: CommandObject):
    args = command.args
    user = message.from_user.id
    if check_admin(user, 2):
        pass
    else:
        "Недостаточно прав"




@router.message(F.text) #Должна быть предпоследней!
async def echo(message: Message):
    await message.answer(f"Вы написали {message.text}")

load_list_admin()

async def main():
    print("Бот запущен")
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)
asyncio.run(main()) # Должна быть последней!

