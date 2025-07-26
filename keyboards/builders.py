from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


services = [
    "1️⃣ Разработка Telegram-ботов под ключ\n"
    "– Автоматизация заявок, рассылок, FAQ, квизов\n"
    "– Воронки, формы, CRM-интеграции",

    "2️⃣ Создание Mini Apps (встроенных приложений в Telegram)\n"
    "– Интерфейс с кнопками, формами, каталогами\n"
    "– Подключение к API, базам данных, платёжным системам",

    "3️⃣ Сопровождение и доработка ботов\n"
    "– Поддержка существующих решений\n"
    "– Рефакторинг, добавление новых функций\n"
    "– Оптимизация скорости",

    "4️⃣ Консультации и проектирование\n"
    "– Поможем спроектировать логику бота от А до Я под вашу задачу\n"
    "– Оценим сложность, сроки, подскажем лучшие практики"
]





def get_carousel_keyboard(current_index: int) -> InlineKeyboardMarkup:
    buttons = []

    if current_index > 0:
        buttons.append(InlineKeyboardButton(text="⬅️ Назад", callback_data=f"carousel:{current_index - 1}"))
    if current_index < len(services) - 1:
        buttons.append(InlineKeyboardButton(text="Вперёд ➡️", callback_data=f"carousel:{current_index + 1}"))

    return InlineKeyboardMarkup(inline_keyboard=[buttons])
