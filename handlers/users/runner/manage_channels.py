from telebot.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardRemove,
)
from helper.psql.psql import PSQL
from loader import bot

from keyboards.default import admin_buttons
from states.channels import Channels


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
    elif text == "Add Channel":
        txt = """
Kanal qo'shishdan oldin botni kanalga admin qilib oling. Bu botni kanalga obuna bo'lgan foydalanuvshilarni ko'rishga yordam beradi.
Kanal qo'shish uchun bizga bazi narsalar kerak.
Kanal id, Kanal url, kanal nomi va plan.
Tartib bo'yicha kiriting:

```
-1002586541 (id)
https://t.me/ITwithBobur (url)
IT with Bobur (name)
1000 (plan)
```
        """
        await bot.send_message(
            chat_id=chat_id,
            text=txt,
            disable_web_page_preview=True,
            parse_mode="markdown",
            reply_markup=admin_buttons.cancel_markup,
        )
        await bot.set_state(
            user_id=user_id,
            state=Channels.addChannels,
            chat_id=chat_id,
        )

    if text == "Delete Channel":
        psql = PSQL()

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
            await bot.send_message(
                chat_id=chat_id,
                text="Hech qanday kanal topilmadi!",
            )
        else:
            channelsButtons.append(
                InlineKeyboardButton(
                    text="Bajarildi",
                    callback_data="delete_this_message",
                )
            )
            channelsMarkup = InlineKeyboardMarkup(row_width=1).add(*channelsButtons)
            await bot.send_message(
                chat_id=chat_id,
                text="Kanalni tanlang!",
                reply_markup=channelsMarkup,
            )

    elif text == "📃Channel list":
        psql = PSQL()
        tex = ""
        for channel in await psql.getChannels():
            tex += f"<code>{channel.id}</code> - {channel.title}\nPlan:{channel.plan}\n{channel.link}\n\n"

        if tex == "":
            await bot.send_message(chat_id=chat_id, text="Hech qanday kanal topilmadi!")
        else:
            await bot.send_message(
                chat_id=chat_id,
                text=tex,
                parse_mode="HTML",
                disable_web_page_preview=True,
            )
