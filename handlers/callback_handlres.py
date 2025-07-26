
from aiogram import Router, types, F
from aiogram.types import Message
from keyboards.reply import main_keyboard
from keyboards.builders import get_carousel_keyboard, services
from utils.states import Form
from aiogram.fsm.context import FSMContext




router = Router()



@router.message(F.text == "📋 Услуги")
async def show_first_service(message: types.Message):
    await message.answer(
        services[0],
        reply_markup=get_carousel_keyboard(0)
    )

@router.callback_query(F.data.startswith("carousel:"))
async def process_carousel(callback: types.CallbackQuery):
    index = int(callback.data.split(":")[1])
    text = services[index]

    await callback.message.edit_text(
        text,
        reply_markup=get_carousel_keyboard(index)
    )
    await callback.answer()











@router.message(F.text == "🔧Технологии")
async def show_services(message: types.Message):
    text = """
<b>🔧 Используемые технологии:</b>

<b>👨‍💻 Языки программирования:</b>
– <code>Python</code>
– <code>JavaScript</code>
– <code>Node.js</code>
– <i>No-code решения</i> (при необходимости)

<b>📡 Telegram Bot API:</b>
Работаем напрямую с официальным Telegram API.

<b>🧠 Фреймворки:</b>
– <code>aiogram</code> (v2 / v3)
– <code>FastAPI / Flask</code> (для API и мини-приложений)

<b>🗄️ Базы данных:</b>
– <code>PostgreSQL</code>, <code>Redis</code>, <code>MongoDB</code>

<b>☁️ Хостинг и деплой:</b>
– <code>Railway</code>, <code>Render</code>, <code>Docker</code>, VPS
"""
    await message.answer(text, parse_mode="HTML", reply_markup=main_keyboard())







@router.message(F.text == "📝 Оставить заявку")
async def start_application(message: types.Message, state: FSMContext):
    await message.answer(
        "Пожалуйста, введите заявку в формате:\nИмя, Телефон, Комментарий"
    )
    await state.set_state(Form.text)








@router.message(F.text == "📱Связь")
async def show_services(message: types.Message):
    text = """
<b>📍 Адрес:</b> г. Бишкек, ул. Ибраимова 103\n
<b>📞 Телефон:</b> <a href="tel:+996700123456">+996 700 123 456</a>\n
<b>📩 Email:</b> <a href="mailto:info@example.com">info@example.com</a>\n
<b>🌐 Сайт:</b> <a href="https://example.com">example.com</a>\n
<b>📱 Telegram:</b> <a href="https://t.me/b.osmn">@b.osmn</a>
"""

    await message.answer(text, parse_mode="HTML", reply_markup=main_keyboard())
