import telebot

memes = 0
complains = 0

API_KEY = 5713675165:AAEtWebqoO7j5lCzJvLf6j_a2L7g_eQzYFk
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['meme'])
def meme(message):
  global memes
  memes += 1
  if memes == 1:
    bot.send_message(message.chat.id, 'Travis has memed ' + str(memes) + ' time!')
  else:
    bot.send_message(message.chat.id, 'Travis has memed ' + str(memes) + ' times!')

@bot.message_handler(commands=['resetmemes'])
def resetmemes(message):
  global memes
  memes = 0
  
@bot.message_handler(commands=['complain'])
def complain(message):
  global complains
  complains += 1
  if complains == 1:
    bot.send_message(message.chat.id, 'Travis has complained ' + str(complains) + ' time!')
  else:
    bot.send_message(message.chat.id, 'Travis has complained ' + str(complains) + ' times!')

@bot.message_handler(commands=['resetcomplains'])
def resetcomplains(message):
  global complains
  complains = 0
  
bot.polling()
