from random import randint
from aiogram import types
from config.consts import TZAR, YES_TRUE, KICK_HIM, FULL_YES_TRUE_OFF


def get_chance(num_start: int = 17, num_end: int | None = None):
    if not num_end:
        return randint(1, 100) == num_start
    else:
        return num_start <= randint(1, 100) <= num_end


async def kick_him(message: types.Message):
    if message.from_user.id in KICK_HIM and get_chance():
        await message.answer(f'Да ебать. Опять @{message.from_user.username} кикнть не получилось')


async def kstati(message: types.Message, msg_txt: str):
    if "кстати" in msg_txt.lower():
        await message.answer('кстати насчeт фоты раком')


def tzar_detected(message: types.Message, ddlink: str):
    if message.from_user.id in TZAR and get_chance(6, 16):
        return f'ХОЛОПАМ МОЛЧАТЬ!\nЕго величество {message.from_user.username} вещает!\n\n{ddlink}'
    else:
        return ddlink


async def pdd_prikol(message: types.Message, link: str):
    if get_chance(12, 17):
        pddlink = link.replace('instagram.com', 'PDDinstagram.com')
        await message.answer(pddlink)
        await message.answer('А, ой. ПИДИДИ это плохо, исправляюсь')


async def yes_true(message: types.Message):
    if message.chat.id in FULL_YES_TRUE_OFF:
        if message.from_user.id in YES_TRUE and get_chance(80, 95):
            await message.reply('Да, верно')
    else:
        if get_chance(75, 80):
            await message.reply('Да, верно')
