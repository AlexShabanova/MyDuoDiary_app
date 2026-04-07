import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import other, user
from telegram_bot.bot_config import BotConfig, load_bot_config
from telegram_bot.keyboards import set_main_menu

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
    # Инициализируем хранилище (создаем экземпляр класса MemoryStorage)
    storage = MemoryStorage()

    # Инициализируем бот и диспетчер
    bot = Bot(
        token=config.bot.token,
        storage=storage,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()

    # Настраиваем кнопку Menu
    await set_main_menu(bot)

    # Регистриуем роутеры в диспетчере
    dp.include_router(user.user_router)
    dp.include_router(other.other_router)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())

# TODO ЛОГИ -- залогировать что-то в проекте
# TODO ЛОГИ -- поправить структуру
# TODO ЛОГИ -- sentry
# TODO ЛОГИ -- fluentogram
# TODO ЛОГИ -- генераторы клавиатур
