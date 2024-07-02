import telebot
from config import TELEGRAM_BOT_TOKEN
from extensions import CurrencyConverter, APIException

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,
                 "Welcome to the Currency Converter Bot! Please send a message in the format: <currency_from> <currency_to> <amount>")


@bot.message_handler(commands=['values'])
def send_values(message):
    currencies = "Available currencies: USD, EUR, RUB, BTC, ETH, etc."
    bot.reply_to(message, currencies)


@bot.message_handler(func=lambda message: True)
def convert_currency(message):
    try:
        parts = message.text.split()
        if len(parts) != 3:
            raise APIException("Invalid format. Please use: <currency_from> <currency_to> <amount>")

        base, quote, amount = parts
        converted_amount = CurrencyConverter.get_price(base.upper(), quote.upper(), amount)
        response = f"{amount} {base} is equal to {converted_amount} {quote}"
        bot.reply_to(message, response)
    except APIException as e:
        bot.reply_to(message, f"Error: {e}")
    except Exception as e:
        bot.reply_to(message, f"Unexpected error: {e}")


bot.polling()





