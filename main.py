import asyncio
from aiogram import Bot, Dispatcher, types     #з 1 по 4 ми підключаєио бібліотеки
from aiogram.filters import Command
from aiogram.types import Message

API_TOKEN = '7388192040:AAE6ySUHROsj21UOZkSxs4uOmdVnRrKTmC4'   #апі токен бота

bot = Bot(token=API_TOKEN)   # тут ми підключаємо бота
dp = Dispatcher()

@dp.message(Command("start"))     # робимо функцію команди старт 
async def send_welcome(message: Message):        # Асинхронна функція, яка буде виконуватися при отриманні команди /start.Параметр message - об'єкт, що містить інформацію про отримане повідомлення.-----------------------------> !!!НЕ ПРАВИЛЬНО!!!
    await message.answer("Привіт!\n Введіть перше число, операцію (+, -, *, /), і друге число через пробіл.")  #використовуємо метод answer() для відправки відповіді користувачу.Відправляємо повідомлення з інструкціями для користувача  -----------------------------> !!!НЕ ПРАВИЛЬНО!!!

@dp.message()     # декоратор, що вказує, що ця функція оброблятиме повідомлення бота.  !!!НЕ ПРАВИЛЬНО!!!
async def calculate(message: Message):
    try:             #   -----------------------------> блок для спроби виконання коду, що може викликати помилки.
        parts = message.text.split() # -----------------------------> # розділяємо текст повідомлення на частини
        
        if len(parts) != 3:             # тут я поставив 3оперетора -- тобто потрібно, щоб було 1число, 1операція, і 1 число  -----------------------------> !!!НЕ ПРАВИЛЬНО!!!
            await message.answer("Будь ласка, введіть вираз у форматі: число оперрація число (наприклад: 5 + 3)")   # ост тут видно, що саме буде, яка написати більше символів ніж потрібно   ----------------------------->   !!!ПРАВИЛЬНО!!!
            return     # -----------------------------> виходимо з функції dp.message, і не продовжуємо виконання
        
        a = int(parts[0]) #перше число
        operation = parts[1] #оператор
        b = int(parts[2])  #друге число
        
        result = 0
        if operation == '+':
            result = a + b
        elif operation == '-':
            result = a - b
        elif operation == '*':                   # з 25 по 41 це сам калькулятор, його дії та вивід результату # ----------------------------->  !!!НЕ ПРАВИЛЬНО!!!
            result = a * b
        elif operation == '/':
            result = a / b
        else:
            await message.answer("Неправильний оператор! Використовуйте тільки +, -, *, або /.")  # -----------------------------> відправка повідомлення про помилку
            return
        
        await message.answer(f"Результат: {result}")  # -----------------------------> виводить результат
    
    except ValueError:
        await message.answer("Помилка! Переконайтесь, що ви ввели правильні числа.")      #тут запобігаю помилок  -----------------------------> !!!НЕ ПРАВИЛЬНО!!!

async def main():                              #викликаємо функцію полінг бот, і запускаємо безкінечний цикл на провірку нових смс    
    await dp.start_polling(bot)

if __name__ == "__main__":                 #запускаю асинхронну функцію і контролюю цикл в main до його завершення
    asyncio.run(main())
