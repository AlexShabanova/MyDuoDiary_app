import asyncio
import logging

from aiogram import Bot, Dispatcher
from handlers import other, user
from telegram_bot.bot_config import BotConfig, load_bot_config

# Инициализируем логгер
logger = logging.getLogger(__name__)


# Функция конфигурирования и запуска бота
async def main():

    # Загружаем конфиг в переменную config
    # FIXME убрать абсолютный путь - при переносе нужно проверить загрузка в венв переменных из .env (должно вернуть True) dotenv.load_dotenv(dotenv_path='C:\\Users\\user\\PycharmProjects\\MyDuoDiary_app\\app\\.env', override=True)
    config: BotConfig = load_bot_config(
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

    # Регистриуем роутеры в диспетчере
    dp.include_router(user.router)
    dp.include_router(other.router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())

# TODO ЛОГИ -- залогировать что-то в проекте
# TODO ЛОГИ -- поправить структуру
# TODO ЛОГИ -- sentry
