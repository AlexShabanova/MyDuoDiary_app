from aiogram.fsm.state import StatesGroup, State


class FSMTranslatePost(StatesGroup):
    post_state = State()
    translate_state = State()
