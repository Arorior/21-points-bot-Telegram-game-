"""Bot start file"""
import telebot

TOKEN = '' # place your token here
bot = telebot.Telebot(TOKEN)

if __name__ == '__main__':
    bot.polling()
