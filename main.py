from config import TOKEN
from aiogram import Dispatcher, Bot, executor, types
from data_worker import Data

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
database = Data()


@dp.message_handler(commands='start')
async def start(message: types.Message):
    database.user_check(message.from_user.id)
    await message.reply('Поехали')


if __name__ == '__main__':
    executor.start_polling(dp)
