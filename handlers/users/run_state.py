from data.models.channel_model import ChannelModel
from helper.psql.psql import PSQL
from keyboards.default import admin_buttons
from loader import bot
from telebot.types import Message
from telebot.asyncio_filters import StateFilter

from states.channels import Channels

from helper.asynic_funcs import asynic_func


@bot.message_handler(state=Channels.addChannels)
async def add_channel(message: Message):
    text = message.text
    chat_id = message.chat.id
    if text == "Cancel":
        await bot.send_message(
            chat_id=chat_id,
            text="Bekor qilindi!",
            reply_markup=admin_buttons.channels_markup,
        )
        await bot.delete_state(user_id=message.from_user.id, chat_id=message.chat.id)
        return

    not_found = []
    if "(id)" not in text:
        not_found.append("id")
    if "(name)" not in text:
        not_found.append("name")
    if "(url)" not in text:
        not_found.append("url")
    if "(plan)" not in text:
        not_found.append("plan")

    if not_found:
        missing_elements = ", ".join(not_found)
        await bot.send_message(
            chat_id=chat_id,
            text=f"Quyidagi elementlar matnda topilmadi: {missing_elements}. Iltimos, to'liq ma'lumot kiriting.",
        )
        return
    else:
        result = asynic_func.parse_telegram_data(text)
        if result == None:
            await bot.send_message(
                chat_id=chat_id,
                text="Ma'lumot formatida xato kiritilgan qayta kiriting!",
            )
            return
        else:
            print(result)
            print(result["id"].lstrip("-").isdigit())
            print(result["plan"].isdigit())
            if not (result["id"].lstrip("-").isdigit() and result["plan"].isdigit()):
                await bot.send_message(
                    chat_id=chat_id,
                    text="id yoki plan formati xato kiritilgan qayta kiriting!",
                )
                return
            else:
                psql = PSQL()
                channel = await psql.getChannelById(result["id"])
                if channel:
                    await bot.send_message(
                        chat_id=chat_id,
                        text=f"Kanal {channel.title} ro'yhatda mavjud!",
                    )
                    return
                else:
                    channel = ChannelModel(
                        id=int(result["id"]),
                        title=result["name"],
                        link=result["url"],
                        plan=int(result["plan"]),
                    )
                    if await psql.createChannel(channel):
                        await bot.send_message(
                            chat_id=chat_id,
                            text="Kanal muvaffaqiyatli qo'shildi!",
                            reply_markup=admin_buttons.channels_markup,
                        )
                    else:
                        await bot.send_message(
                            chat_id=chat_id,
                            text="Kanal qo'shishda xatolik yuz berdi!",
                        )
                        return

    await bot.delete_state(
        user_id=message.from_user.id,
        chat_id=message.chat.id,
    )


bot.add_custom_filter(StateFilter(bot))
