from loader import types
from config import *
from modules.states import *


backK = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
backK.add("Back")

powerK = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
powerB = [_ for _ in powerCommands]
powerK.add(*powerB, "Back")

volumeK = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
volumeB = [_ for _ in volumeCommands]
volumeK.add(*volumeB, "Back")

appsK = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
appsB = [_ for _ in appsCommands]
appsK.add(*appsB, "Back")

keyboardM = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
mainB = {"Power": (powerK, menuStates.power),
         "Volume": (volumeK, menuStates.volume),
         "Apps": (appsK, menuStates.apps)}

keyboardM.add(*mainB)




