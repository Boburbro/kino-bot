from helper.psql.psql import PSQL
from loader import bot


@bot.chat_join_request_handler()
async def join(msg):
    sql = PSQL()
    await sql.addAsk(channel_id=int(msg.chat.id), user_id=int(msg.from_user.id))
