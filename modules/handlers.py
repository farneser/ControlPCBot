import keyboard
from time import sleep
from loader import bot, storage
from aiogram.dispatcher import FSMContext
from aiogram import Dispatcher
from modules.keyboards import *
from modules.states import *


dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands="start", state='*')
async def start(message: types.message):
    if not message['from']['id'] in admins:
        return 0
    await message.answer(f"Hello {message['from']['first_name']}", reply_markup=types.ReplyKeyboardRemove())
    await main(message)


async def main(message):
    if not message['from']['id'] in admins:
        return 0
    await message.answer("Main menu", reply_markup=keyboardM)


@dp.message_handler(lambda message: message.text in mainB)
async def power(message: types.message):
    if not message['from']['id'] in admins:
        return 0
    await message.answer(f"{message['text']} menu", reply_markup=mainB[message['text']][0])
    await mainB[message['text']][1].set()


@dp.message_handler(state=menuStates.power)
@dp.message_handler(state=menuStates.apps)
@dp.message_handler(state=menuStates.volume)
async def statesss(message: types.message, state: FSMContext):
    if not message['from']['id'] in admins:
        return 0
    if message['text'] == "Timer to shutdown":
        await message.answer("Enter the number of minutes before shutdown", reply_markup=backK)
        await menuStates.power0.set()
    elif message['text'] in (*powerB, *volumeB, *appsB):
        if type(allCommands[message['text']]) == (1, 2):
            for v in allCommands[message['text']]:
                os.system(v)
        else:
            os.system(allCommands[message['text']])
    else:
        await state.finish()
        await main(message)


@dp.message_handler(state=menuStates.power0)
async def power0S(message: types.message, state: FSMContext):
    if not message['from']['id'] in admins:
        return 0
    if message['text'] == "Back":
        await state.finish()
        await main(message)
        return 0
    try:
        minutes = int(message['text'])
        os.system(f"""{allCommands["Don't shutdown"]}""")
        os.system(f"{allCommands['Timer to shutdown']} {minutes * 60}")
        sleep(2)
        keyboard.send("enter")
        await message.answer(f"Computer will shut down after {message['text']} minutes", reply_markup=keyboardM)
    except:
        await message.answer("Enter an integer value")
        await menuStates.power0.set()
    await state.finish()


@dp.message_handler()
async def elseBack(message: types.message, state: FSMContext):
    if not message['from']['id'] in admins:
        return 0
    await main(message)
