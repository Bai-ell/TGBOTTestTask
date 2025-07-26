from aiogram import Router, types, F
from utils.states import Form, add_row
from aiogram.fsm.context import FSMContext



router = Router()





@router.message(Form.text)
async def process_application(message: types.Message, state: FSMContext):
    text = message.text.strip()
    

    
    add_row(text)  

    await message.answer("✅ Ваша заявка успешно отправлена! Спасибо.")
    await state.clear() 
