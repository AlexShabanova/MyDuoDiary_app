from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardBuilder

from telegram_bot.lexicon import LEXICON

# Инициализируем билдер
kb_builder = InlineKeyboardBuilder()

# Создаем объекты инлайн-кнопок
post_button = InlineKeyboardButton(
    text=LEXICON["post"], callback_data="post_button_click"
)

jisho_web_app_btn: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON["jisho_dict"], web_app=WebAppInfo(url="https://jisho.org/")
)
tanoshii_web_app_btn: InlineKeyboardButton = InlineKeyboardButton(
    text=LEXICON["tanoshii_dict"],
    web_app=WebAppInfo(url="https://www.tanoshiijapanese.com/dictionary/"),
)

buttons: list = [
    post_button,
    jisho_web_app_btn,
    tanoshii_web_app_btn,
]


# Распаковываем список с кнопками в билдер методом `row` c параметром `width`
kb_builder.row(*buttons)
kb_builder.adjust(1, 2)

# Возвращаем объект инлайн-клавиатуры
inline_keyboard: InlineKeyboardMarkup = kb_builder.as_markup()


# Инициализируем билдер
kb_cancel_builder = InlineKeyboardBuilder()

# Создаем объекты инлайн-кнопок
cancel_button = InlineKeyboardButton(
    text="cancel ❌", callback_data="cancel_button_click"
)
save_button = InlineKeyboardButton(
    text="save post 📩", callback_data="save_button_click"
)

buttons: list = [
    save_button,
    cancel_button,
]


# Распаковываем список с кнопками в билдер методом `row` c параметром `width`
kb_cancel_builder.row(*buttons)
# kb_builder.adjust(1, 2)

# Возвращаем объект инлайн-клавиатуры
inline_cancel_keyboard: InlineKeyboardMarkup = kb_cancel_builder.as_markup()
