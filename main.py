import requests
import telebot
import kucoinbot
import coinmarket_bot
import config
tkn = config.tkn
bot = telebot.TeleBot(tkn)


# kucoinbot.check()


@bot.message_handler(commands = ['start' ])
def start_command(message):
  bot.send_message(message.chat.id, 'welcome to pricebot')


@bot.message_handler(commands = ['price' ])
def pr_command(message):
  price = coinmarket_bot.check(message.text)
  print(price)
  bot.send_message(message.chat.id, str(price))

@bot.message_handler(func=lambda m:True)
def text_command(message):
  msg  = message.text
  price = coinmarket_bot.check(message.text)
  print(f"coinmarket - {price}")
  price2 = kucoinbot.check(message.text)
  print(f"kucoin - {price2}")
  prices = "coinmarket - "+str(price)+"\n"+"kucoin - "+str(price2)
  bot.reply_to(message, prices)

  
  
  
  

  

bot.infinity_polling(timeout=10, long_polling_timeout = 5)