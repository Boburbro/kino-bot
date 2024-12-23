from helper.psql.psql import PSQL
from loader import bot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.models.channel_model import ChannelModel
from helper.asynic_funcs import asynic_func


startus = [
    "administrator",
    "creator",
    "member",
]


async def checkJoin(user_id: int) -> bool:
    if await asynic_func.isAdmin(user_id=user_id):
        return True
    psql = PSQL()
    ignored = []
    channels = await psql.getChannels()
    for channel in channels:
        if not await _checkJoin(user_id, channel):
            ignored.append(InlineKeyboardButton(text=channel.title, url=channel.link))

    if len(ignored) == 0:
        return True
    else:
        bot_username = bot.user.username
        await bot.send_message(
            user_id,
            "Kannallarga obuna bo'ling!",
            reply_markup=InlineKeyboardMarkup(row_width=1)
            .add(*ignored)
            .add(
                InlineKeyboardButton(
                    text="A'zo bo'ldim ✅",
                    callback_data="delete_this_message_middleware",
                    # url=f"https://t.me/{bot_username}?start=None",
                )
            ),
        )

        return False


async def _checkJoin(user_id: int, channel: ChannelModel) -> bool:
    psql = PSQL()
    count = await psql.getCountByChannel(channel_id=channel.id)
    if count == channel.plan:
        return True
    if await psql.isAsked(channel_id=channel.id, user_id=user_id):
        return True
    chat_member = await bot.get_chat_member(chat_id=channel.id, user_id=user_id)
    print(f"{chat_member.status}:{channel.title}:{user_id}")
    if chat_member.status in startus:
        return True
    else:
        return False
