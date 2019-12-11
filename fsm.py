from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_image_url


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        text = event.message.text
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        text = event.message.text
        return text.lower() == "go to state2"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "go to state3"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "你好>//<")
        self.go_back()
    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        send_text_message(reply_token, "不要去state3 回頭好媽")     

    def on_enter_state3(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        send_image_url(reply_token,'https://scontent.fkhh1-2.fna.fbcdn.net/v/t1.0-9/24774761_2250793221613519_5707360604129341045_n.jpg?_nc_cat=110&_nc_ohc=XXR8yABVBrAAQmD2cWtOwOh10YT_Uw_b3Oig9cNICaHeuWmUnENvKUa9Q&_nc_ht=scontent.fkhh1-2.fna&oh=238042de7aabf3b7b4d12a5e6b1d4672&oe=5E6FCCEE')
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")
