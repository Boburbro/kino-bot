from telebot.asyncio_handler_backends import State, StatesGroup


class Channels(StatesGroup):
    addChannels = State()
    removeChannels = State()
