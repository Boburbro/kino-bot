from telebot.types import KeyboardButton, ReplyKeyboardMarkup

main_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
    *[
        KeyboardButton("🔊Channels"),
    ],
    row_width=2
)


channels_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
    *[
        KeyboardButton("Add Channel"),
        KeyboardButton("Delete Channel"),
        KeyboardButton("Channel list"),
    ],
    row_width=2
)
