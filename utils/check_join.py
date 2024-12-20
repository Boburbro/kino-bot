from loader import bot

from utils.psql.psql_channels import channels
from data.models import ChannelModel


startus = [
    "administrator",
    "creator",
    "member",
]

async def checkJoin(user_id: int)->bool:
    ignored = []
    for channel in channels:
         if not await _checkJoin(user_id, channel):
              ignored.append(channel)
    
    if len(ignored) == 0:
         return True
    else:
         return False
              
    

async def _checkJoin(user_id: int, channel: ChannelModel)->bool:
    chat_member = await bot.get_chat_member(
            chat_id=channel.id, user_id=user_id
        )
    if chat_member.status in startus:
            return True
    else: return False