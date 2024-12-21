from psql.base_psql import BasePSQL, check_func


class PSQLAsks(BasePSQL):
    @check_func
    async def getAsks(self):
        print(f"{__file__} is running")
        self.cur.execute("SELECT * FROM asks;")
        return self.cur.fetchall()

    @check_func
    async def getAskByUserId(self, user_id: int):
        print(f"{__file__} is running")

        query = "SELECT * FROM asks WHERE user_id = %s;"
        self.cur.execute(query, (user_id,))
        result = self.cur.fetchall()
        return result

    @check_func
    async def addAsk(self, channel_id: int, user_id: int):
        print(f"{__file__} is running")

        if not await self.isAsked(channel_id, user_id):
            query = "INSERT INTO asks (channel_id, user_id) VALUES (%s, %s);"
            self.cur.execute(query, (channel_id, user_id))
            self.conn.commit()

    @check_func
    async def isAsked(self, channel_id: int, user_id: int):
        print(f"{__file__} is running")

        query = "SELECT * FROM asks WHERE channel_id = %s AND user_id = %s;"
        self.cur.execute(query, (channel_id, user_id))
        result = self.cur.fetchall()
        return bool(result)

    @check_func
    async def removeAskByChannelId(self, channel_id: int):
        print(f"{__file__} is running")

        query = "DELETE FROM asks WHERE channel_id = %s;"
        self.cur.execute(query, (channel_id,))
        self.conn.commit()

    @check_func
    async def getCountByChannel(self, channel_id: int) -> int:
        print(f"{__file__} is running")

        query = "SELECT COUNT(*) FROM asks WHERE channel_id = %s;"
        self.cur.execute(query, (channel_id,))
        result = self.cur.fetchone()
        return result["count"]
