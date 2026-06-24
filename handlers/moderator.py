import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, ChatPermissions
from aiogram.filters import Command, CommandObject
import json
from Telegram_Bot import utils


router = Router()

admin_list = [utils.load_roles()]
ban_list = [utils.load_banned()]

@router.message(Command('mute'))
async def mute(message: Message, bot: Bot):
    ##args = command.args
    user = message.from_user.id
    user_mute_id, target_name = utils.get_target(message)
    if not utils.is_moderator(user):
        ""
        return
    await message.bot.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=user_mute_id,
        permissions=ChatPermissions(
            can_send_messages=False,
            can_send_media_messages=False,
            can_send_other_messages=False
        ),
    )
    print(f"{target_name} замучен")
    await message.answer(f"{target_name} замучен")

@router.message(Command('unmute'))
async def unmute(message: Message, bot: Bot):
    user = message.from_user.id
    user_mute_id, target_name = utils.get_target(message)
    if not utils.is_moderator(user):
        ""
        return
    await message.bot.restrict_chat_member(
        chat_id=message.chat.id,
        user_id=user_mute_id,
        permissions=ChatPermissions(
            can_send_messages=True,
            can_send_media_messages=True,
            can_send_other_messages=True
        ),
    )
    print(f"{target_name} размучен")
    await message.answer(f"{target_name} размучен")