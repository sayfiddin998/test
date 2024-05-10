
import sqlite3

from aiogram.types import Message, CallbackQuery
from aiogram import Bot, Dispatcher, executor

from kinopka import asosiymenubutton, maxsulotlarbutoon, orqagabutton
api = '7040984792:AAG8Qqg-UeUr11Oot3ljyjRGtFASRzGS-rw'

bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: Message):
    chatid= message.chat.id
    await bot.send_message(chat_id=chatid, text='Xush kelibsiz', reply_markup=asosiymenubutton())

@dp.message_handler()
async def getcategory(message: Message):
    chatid = message.chat.id
    kategoriya = message.text
    await bot.send_message(chat_id=chatid, text=kategoriya,
                           reply_markup=maxsulotlarbutoon(kategoriya))


@dp.callback_query_handler(lambda call: 'foods' in call.data)
async def getitem(callback: CallbackQuery):
    chatid = callback.message.chat.id
    item = callback.data.split('_')[1]
    print(item)

    database = sqlite3.connect('magazin.sqlite')
    cursor = database.cursor()

    cursor.execute('''SELECT name, about, price, category, image FROM foods WHERE id = ?''', (item, ))

    maxsulot = cursor.fetchone()
    name = maxsulot[0]
    about = maxsulot[1]
    price = maxsulot[2]
    category = maxsulot[3]
    image = maxsulot[4]
    text = f'Maxsulot nomi: {name}\n\nNaarxi: {price}\n\n{about}\n\n{category}'
    await bot.delete_message(chat_id=chatid, message_id=callback.message.message_id)

    await bot.send_photo(chat_id=chatid, photo=image,  caption=text,reply_markup=orqagabutton(category))

@dp.callback_query_handler(lambda call: 'orqaga' in call.data)
async def orqaga(callback: CallbackQuery):
    chatid = callback.message.chat.id
    category = callback.data.split('_')[1]
    await bot.delete_message(chat_id=chatid, message_id=callback.message.message_id)
    await bot.send_message(chat_id=chatid, text=category,  reply_markup=maxsulotlarbutoon(category))


executor.start_polling(dp, skip_updates=True)