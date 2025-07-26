from aiogram import Router, F
from aiogram.types import Message








router = Router()



@router.message(F.text.lower().in_(["хай", "хелоу", "привет", "салам", 'hello', 'how are you?', 'salam', 'кандай','Кандай', 'hi']))
async def greetings(message: Message):
    await message.reply('Привет')
