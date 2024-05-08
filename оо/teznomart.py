from aiogram.types import Message
from aiogram import Bot, Dispatcher, executor
from kurs_narxlari import getvalut, getsymbols

api = '7002774385:AAE0Gh5ssDf9pGe0nsz4lS8yuo3jx30Nrvs'
bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='hi')


@dp.message_handler(commands='valuta')
async def valuta(message: Message):
    chatid = message.chat.id
    symbols = getsymbols()
    for i, p in symbols.items():
        await bot.send_message(chat_id=chatid, text=f'{i}: {p}')
    await bot.send_message(chat_id=chatid, text=f'Qaysi valutadan, qaysi valyutaga, qancha. masalan: USD UZS 200')


@dp.message_handler()
async def kurs(message: Message):
    chatid = message.chat.id
    text = message.text.split()
    valutadan = text[0]
    valutaga = text[1]
    qancha = int(text[2])

    natija = getvalut(to_=valutaga, from_=valutadan, amount=qancha)
    await bot.send_message(chat_id=chatid, text=natija)