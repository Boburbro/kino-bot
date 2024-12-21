from loader import bot
import asyncio
import middlewares
import handlers
import utils

if __name__ == "__main__":
    import tracemalloc

    tracemalloc.start()
    asyncio.run(bot.infinity_polling(skip_pending=True))
