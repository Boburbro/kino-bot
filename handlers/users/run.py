from loader import bot
from telebot.types import Message

from helper.asynic_funcs import asynic_func

from handlers.users.runner import manage_channels
from keyboards.default import admin_buttons


@bot.message_handler(content_types=["text"])
async def run(message: Message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    text = message.text

    if text.isdigit():
        # TODO: send movie

        pass

    if await asynic_func.isAdmin(message.from_user.id):
        if text == "Back to menu":
            await bot.send_message(
                chat_id, "Menu:", reply_markup=admin_buttons.main_markup
            )
            return

        await manage_channels.manageChannel(message=message)
