import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from random import randint

from config.consts import API_KEY, USERS


HELLO_MESSAGE = '''Привет, я переделываю ссылки для инсты так, чтобы у них был предпросмотр.

Для работы нужно просто добавить бота в чат и дать ему доступ к сообщениям (сделать админом). '''


logging.basicConfig(level=logging.INFO)

inst_base_link = 'https://www.instagram.com'
bot = Bot(token=API_KEY)

dp = Dispatcher()


def get_chance(num_start: int = 17, num_end: int | None = None):
    if not num_end:
        return randint(1, 100) == num_start
    else:
        return num_start <= randint(1, 100) <= num_end


async def text_process(message: types.Message, msg_txt: str):
    link_index = msg_txt.find(inst_base_link)
    
    if link_index >= 0:
        link = msg_txt[link_index:].split(' ')[0]
        ddlink = link.replace('instagram.com', 'ddinstagram.com')
        
        if message.from_user.id == USERS[0] and get_chance(6, 16):
            await message.answer(f'ХОЛОПАМ МОЛЧАТЬ!\nЕго величество МАРК вещает!\n\n{ddlink}')
        else:
            await message.answer(ddlink)
    
    if "кстати" in msg_txt.lower():
        await message.answer('кстати насчeт фоты раком')
    
    # Пока не нужно, потом пригодится
    # if message.from_user.id == USERS[2] and message.entities:
    #     for entity in message.entities:
    #         if entity.type == 'blockquote':
    #             await message.answer('Да, верно')
    #             break
    
    if message.from_user.id in [USERS[2]] and get_chance(80, 95):
        await message.reply('Да, верно')
    
    if message.from_user.id == USERS[1] and get_chance():
        await message.answer(f'Да ебать. Опять @{message.from_user.username} кикнть не получилось')


@dp.message(Command('start'))
async def on_start(message: types.Message):
    if 'www.instagram.com' in message.text:
        logging.info(f'Instagram link: {message.text}')
    await message.answer(HELLO_MESSAGE)


@dp.message(F.text)
async def text_handler(message: types.Message):
    await text_process(message, message.text)


@dp.message(F.photo)
async def photo_handler(message: types.Message):
    if message.caption:
        await text_process(message, message.caption)
    

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
    
