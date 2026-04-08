import logging

from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import (
    Message,
)

from telegram_bot.keyboards import reply_keyboard
from telegram_bot.lexicon.lexicon import LEXICON
from telegram_bot.states.states import FSMTranslatePost

logger = logging.getLogger(__name__)

user_router = Router()


# Этот хэндлер срабатывает на команду /start
@user_router.message(CommandStart(), StateFilter(default_state))
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON["/start"],
        reply_markup=reply_keyboard,
    )


# Этот хэндлер будет срабатывать на команду "/cancel" в состоянии
# по умолчанию и сообщать, что эта команда работает внутри машины состояний
@user_router.message(Command(commands="cancel"), StateFilter(default_state))
async def process_cancel_command(message: Message):
    await message.answer(
        text="Отменять нечего. Вы вне машины состояний\n\n"
        "Чтобы перейти к заполнению анкеты - "
        "отправьте команду /post"
    )


# Этот хэндлер будет срабатывать на команду "/cancel" в любых состояниях,
# кроме состояния по умолчанию, и отключать машину состояний
@user_router.message(Command(commands="cancel"), ~StateFilter(default_state))
async def process_cancel_command_state(message: Message, state: FSMContext):
    await message.answer(
        text="Вы вышли из машины состояний",
        reply_markup=reply_keyboard,
    )
    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    await state.clear()


# Этот хэндлер будет срабатывать на нажатие кнопки post
# и переводить бота в состояние ожидания ввода имени
@user_router.message(F.text == LEXICON["post"], StateFilter(default_state))
async def process_post_command(message: Message, state: FSMContext):
    await message.answer(text="Write a post, put unfamiliar words in ()")
    # Устанавливаем состояние ожидания написания поста
    await state.set_state(FSMTranslatePost.post_state)
    # Удаляем кнопку,
    # чтобы у пользователя не было желания тыкать кнопки
    await message.edit_reply_markup(reply_markup=None)


# Этот хэндлер будет срабатывать, если написан корректный пост
# и переводить в состояние ожидания перевода
@user_router.message(
    StateFilter(FSMTranslatePost.post_state), lambda x: "(" in x.text and ")" in x.text
)
async def process_post_sent(message: Message, state: FSMContext):
    # Сохраняем пост в хранилище по ключу "post"
    await state.update_data(post=message.text)
    await message.answer(text="Переводим пост...")
    # Устанавливаем состояние ожидания перевода
    await state.set_state(FSMTranslatePost.translate_state)

    translated_text = message.text.upper()
    await state.update_data(translated_post=translated_text)

    await message.reply(text=translated_text)

    # Сбрасываем состояние и очищаем данные, полученные внутри состояний
    await state.clear()
    # Отправляем в чат сообщение о выходе из машины состояний
    await message.answer(
        text="Крутой пост!\n\n" "Вы вышли из машины состояний",
        reply_markup=reply_keyboard,
    )


# Этот хэндлер будет срабатывать, если во время ввода поста
# будет введено что-то некорректное
@user_router.message(
    StateFilter(FSMTranslatePost.post_state),
)
async def warning_no_words_to_translate(message: Message):
    await message.answer(
        text="В посте не найдены слова, которые нужно перевести\n\n"
        "Пожалуйста, пишите неизвестные слова в ()\n\n"
        "Если вы хотите прервать написание поста - "
        "отправьте команду /cancel"
    )


# Этот хэндлер срабатывает на команду /help
@user_router.message(Command(commands="help"), StateFilter(default_state))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON["/help"])


# Этот хэндлер будет срабатывать на команду "open jisho dictionary"
@user_router.message(
    Command(commands="web_app"),
    F.text == LEXICON["jisho_dict"],
    StateFilter(default_state),
)
async def process_web_app_command(message: Message):
    await message.answer(
        text="jisho dictionary",
        reply_markup=reply_keyboard,
    )


# Этот хэндлер будет срабатывать на команду "open tanoshii dictionary"
@user_router.message(
    Command(commands="web_app"),
    F.text == LEXICON["tanoshii_dict"],
    StateFilter(default_state),
)
async def process_web_app_command(message: Message):
    await message.answer(
        text="tanoshii dictionary",
        reply_markup=reply_keyboard,
    )


# TODO сделать кнопку cancel
