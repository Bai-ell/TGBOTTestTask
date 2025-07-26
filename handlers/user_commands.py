from aiogram import Router, types
from aiogram.filters import CommandStart
from keyboards.reply import main_keyboard
from aiogram.fsm.context import FSMContext

router = Router()



@router.message(CommandStart())
async def start(message:types.Message, state: FSMContext):
    await message.reply("""Привет! Это твой личный ассистент.
Я помогу тебе выбрать услугу и передам заявку нашей команде.
Нажми «Услуги», чтобы посмотреть, что мы предлагаем, или выбери действие из меню ниже.

""",reply_markup=main_keyboard())