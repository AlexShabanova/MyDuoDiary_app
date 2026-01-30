import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

BOT_TOKEN = "8271403373:AAH4zJnUX2b1_H6FfzjPa4fX02Akf82Vsrg"

dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: Message):
    await message.answer(text=f"Hello, {message.from_user.full_name}!")

async def main():
    logging.basicConfig(level=logging.DEBUG)
    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot)

# if __name__ == "__bot_test__":
asyncio.run(main())