from aiogram import Router
from aiogram.types import Message

from telegram_bot.keyboards.inline_keyboards import inline_keyboard
from telegram_bot.lexicon.lexicon import LEXICON

# Инициализируем роутер уровня модуля
other_router = Router()


# Этот хэндлер будет срабатывать на любые ваши сообщения,
# кроме команд "/start" и "/help"
@other_router.message()
async def send_echo(message: Message):
    await message.reply(
        text=LEXICON["no_post"],
        # reply_markup=inline_keyboard,
    )
