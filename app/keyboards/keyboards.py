from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove,\
    InlineKeyboardMarkup, InlineKeyboardButton
from database import rows

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог 👟').add('Корзина 🗑').add('Контакты 📲')

admin_main = ReplyKeyboardMarkup(resize_keyboard=True)
admin_main.add('Каталог 👟').add('Корзина 🗑').add('Контакты 📲').add('Добавить товар')

cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add('Отмена')

catalog = InlineKeyboardMarkup(row_width=2)
for i in rows:
    catalog.add(InlineKeyboardButton(text=i))

