from config import TOKEN
from aiogram import Dispatcher, Bot, executor, types
from data_worker import Data

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply('Поехали')


if __name__ == '__main__':
    executor.start_polling(dp)
