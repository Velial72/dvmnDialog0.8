import random
import requests.exceptions
import logging
import telebot
from time import sleep
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from environs import Env
from logs import LogHandler

from dialog import detect_intent_text


logger = logging.getLogger('Logger')


def send_answer(answer, user_id, vk_api):
    vk_api.messages.send(
        user_id=user_id,
        message=answer,
        random_id=random.randint(1, 1000)
    )


def main():
    env = Env()
    env.read_env()

    bot_token = env('BOT_TOKEN')
    bot = telebot.TeleBot(token=bot_token)
    logger.setLevel(logging.WARNING)
    logger.addHandler(
        LogHandler(tg_bot=bot, chat_id=env('CHAT_ID'))
    )
    logger.warning("VK_bot запущен")
    vk_token = env('VK_TOKEN')
    vk_session = vk.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    while True:
        try:
            longpoll = VkLongPoll(vk_session)
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    serialized_answer = detect_intent_text(env('DIALOG_ID'), event.user_id, event.text)
                    if not serialized_answer['fallback']:
                        send_answer(serialized_answer['answer'], event.user_id, vk_api)
        except requests.exceptions.ConnectionError:
            logging.exception("VK_bot упал с ошибкой")
            sleep(120)


if __name__ == "__main__":
    main()
