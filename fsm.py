from transitions.extensions import GraphMachine
from utils import send_text_message,send_button_carousel,send_feb,send_mar,send_apr,send_may,send_jun,send_jul,send_aug,send_sep,send_oct,send_nov,send_dec,send_jan,send_fruit_info


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"

    def is_going_to_feb(self, event):
        text = event.message.text
        return text.lower() == "feb"
        
    def is_going_to_mar(self, event):
        text = event.message.text
        return text.lower() == "mar"

    def is_going_to_apr(self, event):
        text = event.message.text
        return text.lower() == "apr"

    def is_going_to_may(self, event):
        text = event.message.text
        return text.lower() == "may"

    def is_going_to_jun(self, event):
        text = event.message.text
        return text.lower() == "jun"

    def is_going_to_jul(self, event):
        text = event.message.text
        return text.lower() == "jul"

    def is_going_to_aug(self, event):
        text = event.message.text
        return text.lower() == "aug"

    def is_going_to_sep(self, event):
        text = event.message.text
        return text.lower() == "sep"

    def is_going_to_oct(self, event):
        text = event.message.text
        return text.lower() == "oct"

    def is_going_to_nov(self, event):
        text = event.message.text
        return text.lower() == "nov"

    def is_going_to_dec(self, event):
        text = event.message.text
        return text.lower() == "dec"

    def is_going_to_jan(self, event):
        text = event.message.text
        return text.lower() == "jan"

    def is_going_to_banana(self, event):
        text = event.message.text
        return text.lower() == "banana"

    def on_enter_start(self, event):
        print("I'm entering start")
        reply_token = event.reply_token
        send_button_carousel(reply_token)

    def on_enter_feb(self,event):
        print("I'm entering feb")
        reply_token = event.reply_token
        send_feb(reply_token)
        
    def on_enter_mar(self,event):
        print("I'm entering mar")
        reply_token = event.reply_token
        send_mar(reply_token)

    def on_enter_apr(self,event):
        print("I'm entering apr")
        reply_token = event.reply_token
        send_apr(reply_token)
        
    def on_enter_may(self,event):
        print("I'm entering may")
        reply_token = event.reply_token
        send_may(reply_token)
        
    def on_enter_jun(self,event):
        print("I'm entering jun")
        reply_token = event.reply_token
        send_jun(reply_token)
        
    def on_enter_jul(self,event):
        print("I'm entering jul")
        reply_token = event.reply_token
        send_jul(reply_token)
        
    def on_enter_aug(self,event):
        print("I'm entering aug")
        reply_token = event.reply_token
        send_aug(reply_token)

    def on_enter_sep(self,event):
        print("I'm entering sep")
        reply_token = event.reply_token
        send_sep(reply_token)
        
    def on_enter_oct(self,event):
        print("I'm entering oct")
        reply_token = event.reply_token
        send_oct(reply_token)
        
    def on_enter_nov(self,event):
        print("I'm entering nov")
        reply_token = event.reply_token
        send_nov(reply_token)
        
    def on_enter_dec(self,event):
        print("I'm entering dec")
        reply_token = event.reply_token
        send_dec(reply_token)
        
    def on_enter_jan(self,event):
        print("I'm entering jan")
        reply_token = event.reply_token
        send_jan(reply_token)
        
    def on_enter_banana(self,event):
        print("I'm entering banana")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/zpHUUhI.jpg'
        nutrition_url = 'https://www.edh.tw/article/19460'
        pick_url = 'https://food.ltn.com.tw/article/1440'
        preserve_ur = 'https://www.chinatimes.com/realtimenews/20201010003310-260405?chdtv'
        send_fruit_info(reply_token, image_url,nutrition_url, pick_url, preserve_ur)
        
        self.go_back()
    # def on_exit_start(self):
    #     print("Leaving state1")

    # def on_enter_state2(self, event):
    #     print("I'm entering state2")

    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "Trigger state2")
    #     self.go_back()

    # def on_exit_state2(self):
    #     print("Leaving state2")
