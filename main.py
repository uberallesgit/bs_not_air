from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
from core.handlers.basic import get_bs_not_air, alm_rep
from aiogram.filters import Command, CommandStart
import asyncio
import logging
# from core.settings import settings
# from core.utils.commands import set_commands

AKASHA = "6505383049:AAHcit-EyccZVa0hvXXPKVhBOSzhgEDeNsw"
JARVIS_TOKEN = '6357305111:AAHzb68csA1ojiDn620m7FFvDXcTP9tYu_s'

CURRENT_BOT = JARVIS_TOKEN
# CURRENT_BOT = AKASHA



async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=CURRENT_BOT,parse_mode="HTML")

    dp = Dispatcher()
    # dp.message.register(get_photo, F.photo)
    dp.message.register(get_bs_not_air, F.document.file_name.startswith("bs_not_air"))
    dp.message.register(alm_rep, F.document.file_name.startswith("alm_rep_"))
    # dp.message.register(get_location, F.location)
    # dp.message.register(get_start,Command(commands=["start","run"]))
    # dp.message.register(get_start,CommandStart())
    # dp.message.register(get_phone,F.text =="тел.")


    # dp.startup.register(start_bot)
    # dp.shutdown.register(stop_bot)



    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())