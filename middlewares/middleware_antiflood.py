from loader import bot

from telebot.asyncio_handler_backends import BaseMiddleware
from telebot.async_telebot import CancelUpdate

from utils.check_join import checkJoin


class SimpleMiddleware(BaseMiddleware):
    def __init__(self, limit) -> None:
        self.last_time = {}
        self.limit = limit
        self.update_types = ["message"]

    async def pre_process(self, message, data):
        print("pre_process")
        if message.chat.type != "private":
            print("middleware: 1")
            return CancelUpdate()
        elif not message.from_user.id in self.last_time:
            print("middleware: 2")
            self.last_time[message.from_user.id] = message.date
            if not await checkJoin(message.from_user.id):
                return CancelUpdate()
            return
        elif message.date - self.last_time[message.from_user.id] < self.limit:
            print("middleware: 3")
            await bot.send_message(message.chat.id, "Siz juda ko'p murojaat qilyabsiz!")
            return CancelUpdate()
        else:
            print("middleware: 4")
            if not await checkJoin(message.from_user.id):
                return CancelUpdate()

        self.last_time[message.from_user.id] = message.date

    async def post_process(self, message, data, exception):
        print("post_process")
        pass


bot.setup_middleware(SimpleMiddleware(limit=2))
