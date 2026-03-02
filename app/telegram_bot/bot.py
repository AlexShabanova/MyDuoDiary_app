import os
import dotenv
import yaml

import logging
import logging.config
from telegram_bot.logging_settings import logging_config

import asyncio
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.types import Message, BotCommand
from aiogram.filters import CommandStart, Command

import bot_config

# # FIXME logger = logging.getLogger(__name__)
# # BOT_TOKEN = bot_config.BOT_TOKEN
# dotenv.load_dotenv("..")
# BOT_TOKEN = os.getenv("BOT_TOKEN")
# dp = Dispatcher()
#
# menu_commands: dict[str, str] = {
#     "/help": "Click here for help",
#     "/post": "Write a post",
#     "/start": "Click here for start",
# }
#
#
# async def set_main_menu(bot: Bot):
#     main_menu_commands = [
#         BotCommand(command=command, description=description)
#         for command, description in menu_commands.items()
#     ]
#     await bot.set_my_commands(main_menu_commands)
#
#
# @dp.message(CommandStart())
# async def handle_start(message: Message):
#     await message.answer(text=f"Hello, {message.from_user.full_name}!")
#
#
# @dp.message(Command("help"))
# async def handle_help(message: Message):
#     text = "Это бот для ведения дневника на японском языке.\nВы пишите пост, а он переводит неизвестные слова"
#     await message.answer(text=text)
#
#
# @dp.message(CommandStart())
# async def handle_start(message: Message):
#     await message.answer(text=f"Hello, {message.from_user.full_name}!")
#
#
# # TODO выбрать или yaml или словарь
# # with open('logging_config.yaml', 'rt') as f:
# #     config = yaml.safe_load(f.read())
#
#
# async def main():
#     # FIXME перенести конфиг в main
#     logging.config.dictConfig(logging_config)
#     bot = Bot(token=BOT_TOKEN)
#     await set_main_menu(bot)
#     await dp.start_polling(bot)


import asyncio
import logging

from aiogram import Bot, Dispatcher


# Функция конфигурирования и запуска бота
async def main() -> None:

    # Загружаем конфиг в переменную config
    # FIXME убрать абсолютный путь - при переносе нужно проверить загрузка в венв переменных из .env (должно вернуть True) dotenv.load_dotenv(dotenv_path='C:\\Users\\user\\PycharmProjects\\MyDuoDiary_app\\app\\.env', override=True)
    config: bot_config.BotConfig = bot_config.load_bot_config(
        "C:\\Users\\user\\PycharmProjects\\MyDuoDiary_app\\app\\.env"
    )
    # Задаём базовую конфигурацию логирования
    logging.basicConfig(
        level=logging.getLevelName(level=config.log.level),
        format=config.log.format,
    )
    # Инициализируем бот и диспетчер
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


# if __name__ == "__main__":
asyncio.run(main())


# TODO ЛОГИ -- залогировать что-то в проекте
# TODO ЛОГИ -- поправить структуру
# TODO ЛОГИ -- sentry
