import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage


channel_access_token = os.getenv("62zgrc/MjkQxz7HWYYgGb8RjhjLiVpfQkgDhATEfTqrKABNdNex8I8NAWnAqxMwna+k5RNAtphhFwUo19rsMEnNV2LbgWVx34ra0uO1qCfReJoCO4XaJ/WZPFQ/Bhp7qMIXiWR3nx3P7dUPJa2/YhQdB04t89/1O/w1cDnyilFU=", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
