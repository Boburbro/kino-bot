from helper.psql.psql import PSQL
from loader import bot
from telebot.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardRemove,
)


@bot.callback_query_handler(func=lambda call: True)
async def callback_query(call: CallbackQuery):
    if call.data == "delete_this_message":
        await bot.delete_message(call.message.chat.id, call.message.message_id)

    elif (str(call.data)).startswith("-"):
        psql = PSQL()
        if await psql.deleteChannel(id=int(call.data)):
            channels = await psql.getChannels()
            channelsButtons = []

            for channel in channels:
                channelsButtons.append(
                    InlineKeyboardButton(
                        text=channel.title,
                        callback_data=f"{channel.id}",
                    )
                )
            if len(channelsButtons) == 0:
                await bot.edit_message_text(
                    text="Hech qanday kanal topilmadi!",
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                )
                await bot.edit_message_reply_markup(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    reply_markup=ReplyKeyboardRemove,
                )
            else:
                channelsButtons.append(
                    InlineKeyboardButton(
                        text="Bajarildi",
                        callback_data="delete_this_message",
                    )
                )
                channelsMarkup = InlineKeyboardMarkup(row_width=1).add(*channelsButtons)
                await bot.edit_message_reply_markup(
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    reply_markup=channelsMarkup,
                )
        else:
            await bot.send_message(call.message.chat.id, "Xatolik! Bajarilmadi.")


"""

    elif call.data == "delete_all_channels":
        sql = AdminSQL()
        try:
            sql.remove_all_channels()
            await bot.send_message(call.message.chat.id, "Bajarilindi!")
            await bot.delete_message(call.message.chat.id, call.message.message_id)
        except Exception as e:
            await bot.send_message(call.message.chat.id, e)

"""
