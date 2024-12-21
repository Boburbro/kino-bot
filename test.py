import asyncio
from helper.psql.psql import PSQL
from data.models.channel_model import ChannelModel

psql = PSQL()


async def aa():
    # await psql.createChannel(
    #     channel=ChannelModel(
    #         id=-1001726187507,
    #         title="Channel 1",
    #         link="https://t.me/+g3UBTcc33cNiNmQy",
    #         plan=10,
    #     ),
    # )
    # await psql.updateChannel(
    #     channel=ChannelModel(
    #         id=-1001726187507,
    #         title="Channel title",
    #         link="https://t.me/+g3UBTcc33cNiNmQy",
    #         plan=100,
    #     ),
    # )
    channels = await psql.getChannels()
    print(channels)
    # await psql.addAsk(
    #     channel_id=1,
    #     user_id=1,
    # )
    # print(await psql.isAsked(channel_id=11, user_id=1))


asyncio.run(aa())
