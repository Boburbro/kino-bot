from loader import bot
from telebot.types import Message

from helper.asynic_funcs import asynic_func

from handlers.users.runner import manage_channels


@bot.message_handler(content_types=["text"])
async def run(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    text = message.text

    if await asynic_func.isAdmin(message.from_user.id):
        await manage_channels.manageChannel(message=message)
