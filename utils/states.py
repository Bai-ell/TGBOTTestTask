from aiogram.fsm.state import StatesGroup, State

class Form(StatesGroup):
    name = State()
    phone = State()
    comment = State()




import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

SPREADSHEET_ID = "1h3nTqhcE9NbV14gn7JZCnnG6h7DbXuTS5XAs1ipkWJE"
sheet = client.open_by_key(SPREADSHEET_ID).sheet1  # первый лист

# ✅ Обновлённая функция записи
def add_row(name: str, phone: str, comment: str):
    try:
        sheet.append_row([name, phone, comment])
        return True
    except Exception as e:
        print(f"[Ошибка Google Sheets]: {e}")
        return False