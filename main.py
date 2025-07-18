import logging
import os
import openai
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

load_dotenv()

# Получение токенов
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_API_KEY
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

# Клавиатура
keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton("🧠 Спросить AI"))
keyboard.add(KeyboardButton("📰 Новости"), KeyboardButton("ℹ️ О боте"))

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("👋 Привет! Я — бот-ассистент по крипте.\nВыбери действие ниже:", reply_markup=keyboard)

@dp.message_handler(commands=['about'])
async def about(message: types.Message):
    await message.answer("Этот бот отвечает на вопросы с помощью ChatGPT и выводит новости по криптовалюте.")

@dp.message_handler(commands=['help'])
async def help_cmd(message: types.Message):
    await message.answer("Напиши свой вопрос или выбери кнопку.\n\nДоступные
