from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardRemove,
    WebAppInfo,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from telegram_bot.lexicon.lexicon import LEXICON_RU

# Инициализируем роутер уровня модуля
router = Router()


# Инициализируем билдер
kb_builder = ReplyKeyboardBuilder()

# Создаём кнопку
jisho_web_app_btn = KeyboardButton(
    text="open jisho dictionary", web_app=WebAppInfo(url="https://jisho.org/")
)
tanoshii_web_app_btn = KeyboardButton(
    text="open tanoshii dictionary",
    web_app=WebAppInfo(url="https://www.tanoshiijapanese.com/dictionary/"),
)

# Создаём список с кнопками
buttons = [
    KeyboardButton(text="write a post"),
    jisho_web_app_btn,
    tanoshii_web_app_btn,
]

# Распаковываем второй список с кнопками методом add
kb_builder.add(*buttons)
kb_builder.adjust(1, 2)


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU["/start"],
        reply_markup=kb_builder.as_markup(resize_keyboard=True),
    )


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands="help"))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU["/help"])


# Этот хэндлер будет срабатывать на ответ "write a post" и удалять клавиатуру
@router.message(F.text == "write a post")
async def process_dog_answer(message: Message):
    await message.answer(
        text="Write a post, put unfamiliar words in []",
        reply_markup=ReplyKeyboardRemove(),
    )


# Этот хэндлер будет срабатывать на команду "open jisho dictionary"
@router.message(Command(commands="web_app"), F.text == "open jisho dictionary")
async def process_web_app_command(message: Message):
    await message.answer(
        text="jisho dictionary", reply_markup=kb_builder.as_markup(resize_keyboard=True)
    )


# Этот хэндлер будет срабатывать на команду "open tanoshii dictionary"
@router.message(Command(commands="web_app"), F.text == "open tanoshii dictionary")
async def process_web_app_command(message: Message):
    await message.answer(
        text="tanoshii dictionary",
        reply_markup=kb_builder.as_markup(resize_keyboard=True),
    )
