import time

import vk_api
from requests import get
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

from VkUsers import VkUsers

user_list = []


def delete_user_message(user_id, message_id):
    test = vk.messages.delete(message_ids={message_id}, delete_for_all=1)
    pass


def get_all_user(chat_id):
    profiles = vk.messages.getConversationMembers(peer_id=2000000000 + chat_id)["profiles"]
    for profile in profiles:
        user_list.append(VkUsers(profile.get("id"), profile.get("first_name"), profile.get("screen_name"), False))


def send_message(message, user_id):
    vk.messages.send(peer_id=user_id, message=message, random_id=0)


vk_session = vk_api.VkApi(token='117599719829ec648674d5dc04f434f6ace002680a35b84f068104a17e20f209aee27b1b4c9559f1d8054')
vk_session._auth_token()
vk = vk_session.get_api()
longPoll = VkBotLongPoll(vk_session, 191731917)
get_all_user(2)


def is_banned(user_id):
    return True


def get_user_name_for_id(user_id):
    for user in user_list:
        if user.id == user_id:
            return user.first_name
    pass


def send_hello(conversation_event):
    if conversation_event.message['text'].lower() == 'привет':
        send_message("Привет " + get_user_name_for_id(conversation_event.message['from_id']) + '!',
                     conversation_event.message['peer_id'])
    pass


def send_goodbye(conversation_event):
    if conversation_event.message['text'].lower() == 'пока':
        send_message("Пока " + get_user_name_for_id(conversation_event.message['from_id']) + '!',
                     conversation_event.message['peer_id'])
    pass


while True:
    try:
        for event in longPoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_chat:
                    send_hello(event)
                    send_goodbye(event)

    except Exception as E:
        print(E)
        time.sleep(1)
