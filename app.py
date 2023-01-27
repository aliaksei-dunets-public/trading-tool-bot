# pipenv run python botAiogram.py
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandObject
from dotenv import dotenv_values

config = dotenv_values(".env")

try:
    if not config['BOT_TOKEN']:
        raise Exception('Bot token is not maintained in the environment values')
except KeyError:
    raise Exception('Bot token is not maintained in the environment values')

# Объект бота
bot = Bot(token=config['BOT_TOKEN'])
# Диспетчер для бота
dp = Dispatcher()

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Хэндлер на команду /start
@dp.message(Command(commands=["start"]))
async def cmd_start(message: types.Message):
    await message.answer('Hello')

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
