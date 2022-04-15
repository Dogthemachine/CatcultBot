from django.http import HttpResponse
import telebot
from django.conf import settings


telegram_bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)

print("\n\n\n BOT TOKEN", settings.TELEGRAM_BOT_TOKEN)

def telegram_webhook(request):
    print("TEST PRINT DEF")
    if request.method == "POST" and request.content_type == "application/json":
        try:
            json_string = request.body.decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
        except:
            return HttpResponse(status=403)
        if update.message and update.message.text:
            # stat = BotQuery()
            # stat.telegram = True
            # stat.vacancy = update.message.text[:128]
            # stat.save()
            telegram_bot.process_new_messages([update.message])
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=403)


@telegram_bot.message_handler(commands=["help", "start"])
def telegram_welcome(message):
    text = "help / start commands"
    telegram_bot.send_message(message.chat.id, text)


@telegram_bot.message_handler(commands=["my_command"])
def telegram_channels(message):
    text = "my command"
    telegram_bot.send_message(message.chat.id, text)


@telegram_bot.message_handler(func=lambda message: True, content_types=["text"])
def telegram_message(message):

    # try:
    #     chat = Chat.objects.get(chat_id=message.chat.id)
    # except Chat.DoesNotExist:
    #     chat = Chat()
    #     chat.chat_id = message.chat.id
    #     chat.last_search = message.text
    #     chat.telegram = True
    #     chat.save()
    text = "Response " + message.text
    telegram_bot.send_message(message.chat.id, text)
