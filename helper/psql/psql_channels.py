from data.models.channel_model import ChannelModel
from helper.psql.base_psql import BasePSQL, check_func


class PSQLChannel(BasePSQL):
    @check_func
    async def getChannels(self):
        print(f"{__file__} is running")
        self.cur.execute("SELECT * FROM channels")
        rows = self.cur.fetchall()
        return [ChannelModel.fromJson(row) for row in rows]

    @check_func
    async def getChannelById(self, id: int):
        print(f"{__file__} is running")
        self.cur.execute(
            "SELECT * FROM channels WHERE id=%s",
            (id,),
        )
        row = self.cur.fetchone()
        if row:
            return ChannelModel(**row)
        else:
            return None

    @check_func
    async def createChannel(self, channel: ChannelModel):
        print(f"{__file__} is running")
        try:
            self.cur.execute(
                """
                INSERT INTO channels 
                (id, title, link, plan) 
                VALUES (%s, %s, %s, %s)
            """,
                (
                    channel.id,
                    channel.title,
                    channel.link,
                    channel.plan,
                ),
            )
        except Exception as e:
            print(f"Error creating channel: {e}")
            self.conn.commit()
            return False

        self.conn.commit()
        return True

    @check_func
    async def updateChannel(self, channel: ChannelModel):
        print(f"{__file__} is running")
        try:
            self.cur.execute(
                """
                UPDATE channels 
                SET title=%s, link=%s, plan=%s 
                WHERE id=%s
            """,
                (
                    channel.title,
                    channel.link,
                    channel.plan,
                    channel.id,
                ),
            )
        except Exception as e:
            print(f"Error updating channel: {e}")
            self.conn.commit()
            return False

        self.conn.commit()
        return True

    @check_func
    async def deleteChannel(self, id: int):
        print(f"{__file__} is running")
        self.cur.execute(
            "DELETE FROM channels WHERE id=%s",
            (id,),
        )
        self.conn.commit()
        return True
