from loader import bot
from telebot.types import Message, ReplyKeyboardRemove

from keyboards.default import admin_buttons
from helper.asynic_funcs import asynic_func


@bot.message_handler(commands=["start"])
async def command_start(message: Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Assalomu alaykum!\n{message.from_user.full_name}",
        reply_markup=ReplyKeyboardRemove(),
    )


@bot.message_handler(commands=["admin"])
async def command_admin(message: Message):
    reply_markup = None
    if await asynic_func.isAdmin(message.from_user.id):
        reply_markup = admin_buttons.main_markup
    await bot.send_message(
        chat_id=message.chat.id,
        text=f"Admin: @ITwithBobur",
        reply_markup=reply_markup,
    )
