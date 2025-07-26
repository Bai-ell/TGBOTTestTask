from aiogram.types import ReplyKeyboardMarkup, KeyboardButton







def main_keyboard() -> ReplyKeyboardMarkup:
    kb = [
        [KeyboardButton(text="📋 Услуги"), KeyboardButton(text="🔧Технологии")],
        [KeyboardButton(text="📝 Оставить заявку"), KeyboardButton(text="📱Связь")]
    ]
    return ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите действие"
    )
