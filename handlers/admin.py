import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command, CommandObject
import json
from Telegram_Bot import utils


router = Router()

admin_list = [utils.load_roles()]
ban_list = [utils.load_banned()]

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