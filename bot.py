from config import TOKEN
from aiogram import Dispatcher, Bot, executor, types

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Поехали')


def run_bot():
    executor.start_polling(dp)
