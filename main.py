from bot import TelegramChatbot
import generate_reply
import json


def make_reply(bot, text, photo_id, from_, user):
    return generate_reply.response(bot, text, photo_id, from_, user)


def get_update(bot, update_id):
    updates = bot.get_updates(offset=update_id)
    return updates.get("result")


def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"keyboard": keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)


def main():
    bot = TelegramChatbot()
    update_id = None
    while True:
        updates = get_update(bot, update_id)
        if updates:
            for item in updates:
                message = item.get("message")
                if message:
                    text = message.get("text")
                    try:
                        photo_id = None
                        if text is None:
                            photo_id = str(message.get("photo")[0].get('file_id'))
                        from_ = message["from"]["id"]
                        is_bot = message["from"]["is_bot"]
                        user = message.get("chat")
                        print(user)
                    except Exception as e:
                        photo_id, from_, user = None, None, None
                        is_bot = True

                    if is_bot is False:
                        reply, keypad_input = make_reply(bot, text, photo_id, from_, user)
                        if keypad_input:
                            keyboard = build_keyboard(keypad_input)
                            bot.send_message(reply, from_, keyboard)
                        else:
                            bot.send_message(reply, from_)
                    else:
                        bot.send_message("SomeThing went wrong!! Send /start to restart the process.", from_)


if __name__ == '__main__':
    main()
