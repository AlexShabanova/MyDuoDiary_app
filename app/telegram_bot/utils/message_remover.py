import logging
from typing import Union

from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

logger = logging.getLogger(__name__)


def auto_delete_history(func):
    async def wrapper(event: Union[Message, CallbackQuery], state: FSMContext):
        hint_messages_to_delete: list = await state.get_value("messages_to_delete")
        if hint_messages_to_delete:
            for msg in hint_messages_to_delete:
                if isinstance(msg, Message):
                    await msg.delete()
                elif isinstance(msg, CallbackQuery):
                    await msg.message.delete()

            await state.update_data(messages_to_delete=[])

        result = await func(event, state)

        if isinstance(result, Message) or isinstance(result, CallbackQuery):
            new_message: list = [result]
        elif isinstance(result, list):
            new_message: list = [msg for msg in result if isinstance(msg, Message)]
        else:
            new_message: list = []

        await state.update_data(messages_to_delete=new_message)
        return result

    return wrapper
