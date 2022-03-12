from aiogram.types import KeyboardButton,ReplyKeyboardMarkup


menu_default = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📦Menu"),
            KeyboardButton(text="🆘Yordam")
        ],
    ],
    resize_keyboard=True
)

