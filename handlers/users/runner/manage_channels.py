from telebot.types import Message
from loader import bot

from keyboards.default import admin_buttons


async def manageChannel(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    text = message.text

    if text == "🔊Channels":
        await bot.send_message(
            chat_id,
            "Manage channels:",
            reply_markup=admin_buttons.channels_markup,
        )
