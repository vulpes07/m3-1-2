from aiogram import Router, types
from aiogram.filters import Command
from bot import bot
router = Router()
@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Привет, я бот!")