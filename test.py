import asyncio
from helper.psql.psql import PSQL


psql = PSQL()


# psql.initDataBase()

print(asyncio.run(psql.getChannelById(-1001726187507)))
