from config import TOKEN
import data_worker as db
from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    if db.user_check(message.from_user.id):
        await message.reply('')
    else:

        await message.reply('Кажется вы не пользовались до этого ботом.\nСкажите как вас зовут:')


if __name__ == '__main__':
    db.create_db()
    executor.start_polling(dp)
