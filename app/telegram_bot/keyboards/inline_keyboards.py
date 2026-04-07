from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from telegram_bot.lexicon import LEXICON

# Инициализируем билдер
kb_builder = InlineKeyboardBuilder()

# Создаем объекты инлайн-кнопок
post_button = InlineKeyboardButton(
    text=LEXICON["post"], callback_data="post_button_click"
)

# Распаковываем список с кнопками в билдер методом `row` c параметром `width`
kb_builder.row(post_button)

# Возвращаем объект инлайн-клавиатуры
inline_keyboard: InlineKeyboardMarkup = kb_builder.as_markup()
