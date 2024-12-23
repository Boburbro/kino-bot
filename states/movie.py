from telebot.asyncio_handler_backends import StatesGroup, State


class MovieState(StatesGroup):
    addMovie = State()
    editMovie = State()
    removeMovie = State()
