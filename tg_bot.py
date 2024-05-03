import requests.exceptions
import telebot
import logging
from environs import Env
from time import sleep

from dialog import detect_intent_text
from logs import LogHandler


logger = logging.getLogger('Logger')


def main():
    env = Env()
    env.read_env()

    BOT_TOKEN = env('BOT_TOKEN')
    bot = telebot.TeleBot(token=BOT_TOKEN)
    logger.setLevel(logging.WARNING)
    logger.addHandler(
        LogHandler(tg_bot=bot, chat_id=env('CHAT_ID'))
    )
    logger.warning("TG_bot запущен")


    @bot.message_handler(commands=['start'])
    def process_start_command(message):
        bot.send_message(chat_id=message.chat.id, text='Zzz...')


    @bot.message_handler(commands=['help'])
    def process_help_command(message):
        bot.send_message(chat_id=message.chat.id,
                         text='Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение'
                        )


    @bot.message_handler(content_types=['text'])
    def send_answer(message):
        serialized_answer = detect_intent_text(env('DIALOG_ID'), message.from_user.id, message.text, flag=False)
        if serialized_answer is not None:
            bot.send_message(chat_id=message.chat.id, text=serialized_answer['answer'])
    while True:
        try:
            bot.polling()
        except requests.exceptions.ReadTimeout:
            pass
        except requests.exceptions.ConnectionError:
            logging.exception("TG_bot упал с ошибкой")
            sleep(120)


if __name__ == '__main__':
    main()
