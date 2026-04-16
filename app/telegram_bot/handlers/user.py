import logging

from aiogram import Router, F
from aiogram.filters import Command, CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    CallbackQuery,
)

from telegram_bot.keyboards.inline_keyboards import (
    inline_keyboard,
    inline_cancel_keyboard,
)
from telegram_bot.lexicon.lexicon import LEXICON
from telegram_bot.states.states import FSMTranslatePost
from telegram_bot.utils import auto_delete_history

logger = logging.getLogger(__name__)
user_router = Router()


# start command handler
@user_router.message(CommandStart(), StateFilter(None))
@auto_delete_history
async def process_start_command(message: Message, state: FSMContext):
    msg: Message = await message.answer(
        text=LEXICON["/start"],
        reply_markup=inline_keyboard,
    )
    await state.update_data(messages_to_delete=[])
    return msg


# if user pressed "write a post" button
@user_router.callback_query(F.data == "post_button_click", StateFilter(None))
@auto_delete_history
async def process_post_command(callback: CallbackQuery, state: FSMContext):
    try:
        msg: CallbackQuery = await callback.message.edit_text(text=LEXICON["brackets"])
    except:
        # TODO сделать свой exception
        msg: Message = await callback.message.answer(text=LEXICON["brackets"])
    await state.set_state(FSMTranslatePost.post_state)
    return msg


# handler for correct post
@user_router.message(
    StateFilter(FSMTranslatePost.post_state), lambda x: "(" in x.text and ")" in x.text
)
@auto_delete_history
async def process_post_sent(message: Message, state: FSMContext):
    await state.update_data(post=message.text)
    await state.set_state(FSMTranslatePost.translate_state)
    # FIXME тут должен быть перевод
    translated_text: str = message.text.upper()
    await state.update_data(translated_post=translated_text)

    await message.reply(text=translated_text)
    await state.clear()

    return await message.answer(text=LEXICON["saved"], reply_markup=inline_keyboard)


# handler for a post with no unfamiliar words
@user_router.message(StateFilter(FSMTranslatePost.post_state))
@auto_delete_history
async def warning_no_words_to_translate(message: Message, state: FSMContext):
    return await message.answer(
        text=LEXICON["no_words"],
        reply_markup=inline_cancel_keyboard,
    )


# handler for "cancel" button
@user_router.callback_query(F.data == "cancel_button_click", ~StateFilter(None))
@auto_delete_history
async def process_cancel_command_state(callback: CallbackQuery, state: FSMContext):
    try:
        msg = await callback.message.edit_text(
            text=LEXICON["exit"],
            reply_markup=inline_keyboard,
        )
    except:
        # TODO сделать свой exception
        msg = await callback.message.answer(
            text=LEXICON["exit"],
            reply_markup=inline_keyboard,
        )
    await state.clear()
    return msg


# handler for "save post" button
@user_router.callback_query(F.data == "save_button_click", ~StateFilter(None))
@auto_delete_history
async def process_save_command_state(callback: CallbackQuery, state: FSMContext):
    try:
        msg = await callback.message.edit_text(
            text=LEXICON["saved"],
            reply_markup=inline_keyboard,
        )
    except:
        # TODO сделать свой exception
        msg = await callback.message.answer(
            text=LEXICON["saved"],
            reply_markup=inline_keyboard,
        )
    await state.clear()
    return msg


# /help handler
@user_router.message(Command(commands="help"), StateFilter(None))
@auto_delete_history
async def process_help_command(message: Message, state: FSMContext):
    return await message.answer(
        text=LEXICON["/help"],
        reply_markup=inline_keyboard,
    )


# web app jisho dictionary handler
@user_router.message(
    Command(commands="web_app"),
    F.text == LEXICON["jisho_dict"],
    StateFilter(None),
)
async def process_web_app_command(message: Message):
    await message.answer(
        text="jisho dictionary",
        reply_markup=inline_keyboard,
    )


# web app tanoshii dictionary handler
@user_router.message(
    Command(commands="web_app"),
    F.text == LEXICON["tanoshii_dict"],
    StateFilter(None),
)
async def process_web_app_command(message: Message):
    await message.answer(
        text="tanoshii dictionary",
        reply_markup=inline_keyboard,
    )


# if user instead of clicking a button is trying to input text
@user_router.message(StateFilter(None))
@user_router.message(F.text, StateFilter(FSMTranslatePost.post_state))
@auto_delete_history
async def warning_no_button_pressed(message: Message, state: FSMContext):
    return await message.answer(text=LEXICON["no_post"], reply_markup=inline_keyboard)
