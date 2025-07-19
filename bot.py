import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import os

API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

user_data = {}

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Salom! Buyurtma berish uchun ismingizni yuboring.")
    user_data[message.from_user.id] = {}

@dp.message(lambda message: message.from_user.id in user_data and 'name' not in user_data[message.from_user.id])
async def get_name(message: types.Message):
    user_data[message.from_user.id]['name'] = message.text
    await message.answer("Telefon raqamingizni yuboring.")

@dp.message(lambda message: message.from_user.id in user_data and 'phone' not in user_data[message.from_user.id])
async def get_phone(message: types.Message):
    user_data[message.from_user.id]['phone'] = message.text
    await message.answer("Nima buyurtma bermoqchisiz?")

@dp.message(lambda message: message.from_user.id in user_data and 'order' not in user_data[message.from_user.id])
async def get_order(message: types.Message):
    user_data[message.from_user.id]['order'] = message.text
    await message.answer("Manzilingizni yuboring.")

@dp.message(lambda message: message.from_user.id in user_data and 'address' not in user_data[message.from_user.id])
async def get_address(message: types.Message):
    user_data[message.from_user.id]['address'] = message.text
    data = user_data[message.from_user.id]

    text = (
        f"🛒 *Yangi Buyurtma!*\n\n"
        f"👤 Ism: {data['name']}\n"
        f"📞 Telefon: {data['phone']}\n"
        f"📦 Buyurtma: {data['order']}\n"
        f"📍 Manzil: {data['address']}"
    )

    await message.answer("✅ Buyurtmangiz qabul qilindi, tez orada bog'lanamiz. Rahmat!")
    await bot.send_message(chat_id=message.from_user.id, text=text, parse_mode="Markdown")

    del user_data[message.from_user.id]

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
