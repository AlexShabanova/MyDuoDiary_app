import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import user
from telegram_bot.bot_config import BotConfig, load_bot_config
from telegram_bot.keyboards import set_main_menu

logger = logging.getLogger(__name__)


async def main():
    # FIXME убрать абсолютный путь - при переносе нужно проверить загрузка в венв переменных из .env (должно вернуть True) dotenv.load_dotenv(dotenv_path='C:\\Users\\user\\PycharmProjects\\MyDuoDiary_app\\app\\.env', override=True)
    config: BotConfig = load_bot_config(
        "C:\\Users\\user\\PycharmProjects\\MyDuoDiary_app\\app\\.env"
    )

    logging.basicConfig(
        level=logging.getLevelName(level=config.log.level),
        format=config.log.format,
    )

    # TODO заменить на Redis
    storage = MemoryStorage()
    bot = Bot(
        token=config.bot.token,
        storage=storage,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    await set_main_menu(bot)
    dp.include_router(user.user_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())

# TODO ЛОГИ -- залогировать что-то в проекте
# TODO -- поправить структуру
# TODO ЛОГИ -- sentry
# TODO -- fluentogram
# TODO -- генераторы клавиатур
