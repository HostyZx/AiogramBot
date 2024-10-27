from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram import F, Router

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):   
    await message.reply("Привет, я бот") 

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.reply("Привет, это помощь")

@router.message(F.text == "тест")
async def cmd_test(message: Message):
    await message.reply("Привет, это тестовое сообщение!")
