# import requests
# from datetime import datetime
#
# def pay_bot(city_name):
#     api = '6670645347:AAE-etPa_ucuVZcz0PK7fVpzSoEhjmGIaE4'
#     url = f'https://api.openweathermap.org/data/2.5/weather'
#     parametr = {
#         'units': 'metric',
#         'q': city_name,
#         'appid': api,
#         'lang': 'ru'
#     }
#     response = requests.get(url, params=parametr)
#     data = response.json()
#     try:
#         lat = data['coord']['lat']
#         lon = data['coord']['lon']
#         main = data['weather'][0]['main']
#         description = data['weather'][0]['description']
#         temp = data['main']['temp']
#         humidity = data['main']['humidity']
#         wind = data['wind']['speed']
#         clouds = data['clouds']['all']
#         country = data['sys']['country']
#         sunrise = datetime.fromtimestamp(data['sys']['sunrise'])
#         sunset = datetime.fromtimestamp(data['sys']['sunset'])
#
#         text = f'''
#         Ob-havo ma'lumoti
#         Havo: {main}, {description}
#         Harorat: {temp} Cº
#         Namlik: {humidity}%
#         Shamol: {wind}m/s
#         Bulutlar: {clouds} ta
#         Davlat: {country}
#
#         Koordinatalri:
#         Kenglik: {lat} ºN
#         Uzunlik: {lon} ºE
#
#         Quyosh chiqishi: {sunrise}
#         Quyosh botishi: {sunset}
#         '''
#         return text
#     except:
#         return 'Bunaqa shahar yoq'
# from aiogram.types import Message
# from aiogram import Bot, Dispatcher, executor
#
# from b import pay_bot
#
# apitoken = '6670645347:AAE-etPa_ucuVZcz0PK7fVpzSoEhjmGIaE4'
# bot = Bot(apitoken)
# dp = Dispatcher(bot)
#
# @dp.message_handler(commands='start')
# async def start(message: Message):
#     chatid = message.chat.id
#     fullname = message.from_user.full_name
#
#     await bot.send_message(chatid, f'hi {fullname}')
#     # await message.reply('Hi')
#
#
# @dp.message_handler(commands='help')
# async def help(message: Message):
#
#     await message.reply('Botni ishga tushirish uchun /start ni bosing')
#
# @dp.message_handler()
# async def echo(message: Message):
#
#     info = pay_bot(message.text)
#
#     await message.reply(info)
#
#
# executor.start_polling(dp, skip_updates=True)
















