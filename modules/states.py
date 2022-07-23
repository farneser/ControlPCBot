from aiogram.dispatcher.filters.state import StatesGroup, State


class menuStates(StatesGroup):
    power = State()
    volume = State()
    apps = State()
    power0 = State()
