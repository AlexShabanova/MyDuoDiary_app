import os
import dotenv
from pydantic import BaseModel


class TgBot(BaseModel):
    token: str


class LogSettings(BaseModel):
    level: str
    format: str


class BotConfig(BaseModel):
    bot: TgBot
    log: LogSettings


def load_bot_config(path: str | None = None) -> BotConfig:
    dotenv.load_dotenv(dotenv_path=path, override=True)
    return BotConfig(
        bot=TgBot(token=os.getenv("BOT_TOKEN")),
        log=LogSettings(level=os.getenv("LOG_LEVEL"), format=os.getenv("LOG_FORMAT")),
    )
