import config
from telebot import TeleBot 

bot = TeleBot(config.API_TOKEN)


@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    bot.send_message(message.chat.id,text='Приветствуем в нашем чате!\nНаши правила:\nНе материться\nНе засорять чат оффтопом\nЖелаю удачи!')

if __name__ == '__main__':
    bot.polling(none_stop=True)