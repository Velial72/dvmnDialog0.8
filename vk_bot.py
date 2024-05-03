import random
import requests.exceptions
import logging
from time import sleep
import vk_api as vk
from vk_api.longpoll import VkLongPoll, VkEventType
from environs import Env
from tg_bot import bot
from logs import LogHandler

from dialog import detect_intent_text


env = Env()
env.read_env()

VK_TOKEN = env('VK_TOKEN')

logging.basicConfig(
        handlers=[LogHandler(tg_bot=bot, chat_id=env('CHAT_ID'))]
    )
logging.warning("VK_bot запущен")


def send_answer(answer, user_id, vk_api):
    vk_api.messages.send(
        user_id=user_id,
        message=answer,
        random_id=random.randint(1,1000)
    )


if __name__ == "__main__":
    VK_TOKEN = env('VK_TOKEN')
    vk_session = vk.VkApi(token=VK_TOKEN)
    vk_api = vk_session.get_api()
    while True:
        try:
            longpoll = VkLongPoll(vk_session)
            for event in longpoll.listen():
                if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                    serialized_answer = detect_intent_text(env('DIALOG_ID'), event.user_id, event.text)
                    if serialized_answer is not None:
                        send_answer(serialized_answer['answer'], event.user_id, vk_api)
        except requests.exceptions.ConnectionError:
            logging.exception("VK_bot упал с ошибкой")
            sleep(120)
