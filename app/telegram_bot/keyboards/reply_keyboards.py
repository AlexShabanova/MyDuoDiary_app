from aiogram.types import KeyboardButton, WebAppInfo, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from telegram_bot.lexicon import LEXICON

# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаём кнопки
jisho_web_app_btn: KeyboardButton = KeyboardButton(
    text=LEXICON["jisho_dict"], web_app=WebAppInfo(url="https://jisho.org/")
)
tanoshii_web_app_btn: KeyboardButton = KeyboardButton(
    text=LEXICON["tanoshii_dict"],
    web_app=WebAppInfo(url="https://www.tanoshiijapanese.com/dictionary/"),
)

post_btn: KeyboardButton = KeyboardButton(text=LEXICON["post"])

# Создаём список с кнопками
buttons: list = [
    post_btn,
    jisho_web_app_btn,
    tanoshii_web_app_btn,
]

# Распаковываем второй список с кнопками методом add
kb_builder.row(*buttons)
kb_builder.adjust(1, 2)

# Создаём клавиатуру с кнопками
reply_keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
    one_time_keyboard=True, resize_keyboard=True
)
