from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove,\
    InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог 👟').add('Корзина 🗑').add('Контакты 📲')

admin_main = ReplyKeyboardMarkup(resize_keyboard=True)
admin_main.add('Каталог 👟').add('Корзина 🗑').add('Контакты 📲').add('Добавить товар')

catalog = InlineKeyboardMarkup(row_width=2)
catalog.add('Adidas').add('Назад')
