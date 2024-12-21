from helper.psql.psql import PSQL
from loader import bot

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
            ignored.append(channel)

    if len(ignored) == 0:
        return True
    else:
        return False


async def _checkJoin(user_id: int, channel: ChannelModel) -> bool:
    chat_member = await bot.get_chat_member(chat_id=channel.id, user_id=user_id)
    if chat_member.status in startus:
        return True
    else:
        return False
