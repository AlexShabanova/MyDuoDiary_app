from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    Message,
    ReplyKeyboardRemove,
)

from telegram_bot.keyboards import keyboard
from telegram_bot.lexicon.lexicon import LEXICON_RU

user_router = Router()


# Этот хэндлер срабатывает на команду /start
@user_router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU["/start"],
        reply_markup=keyboard,
    )


# Этот хэндлер срабатывает на команду /help
@user_router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"])


# Этот хэндлер будет срабатывать на ответ "write a post" и удалять клавиатуру
@user_router.message(F.text == LEXICON_RU["post"])
async def process_dog_answer(message: Message):
    await message.answer(
        text="Write a post, put unfamiliar words in []",
        reply_markup=ReplyKeyboardRemove(),
    )


# Этот хэндлер будет срабатывать на команду "open jisho dictionary"
@user_router.message(Command(commands="web_app"), F.text == LEXICON_RU["jisho_dict"])
async def process_web_app_command(message: Message):
    await message.answer(
        text="jisho dictionary",
        reply_markup=keyboard,
    )


# Этот хэндлер будет срабатывать на команду "open tanoshii dictionary"
@user_router.message(Command(commands="web_app"), F.text == LEXICON_RU["tanoshii_dict"])
async def process_web_app_command(message: Message):
    await message.answer(
        text="tanoshii dictionary",
        reply_markup=keyboard,
    )
