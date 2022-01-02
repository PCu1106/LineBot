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

    def is_going_to_guava(self, event):
        text = event.message.text
        return text.lower() == "guava"

    def is_going_to_dragonfruit(self, event):
        text = event.message.text
        return text.lower() == "dragonfruit"

    def is_going_to_passionfruit(self, event):
        text = event.message.text
        return text.lower() == "passionfruit"

    def is_going_to_mango(self, event):
        text = event.message.text
        return text.lower() == "mango"

    def is_going_to_watermelon(self, event):
        text = event.message.text
        return text.lower() == "watermelon"

    def is_going_to_pineapple(self, event):
        text = event.message.text
        return text.lower() == "pineapple"

    def is_going_to_sugarapple(self, event):
        text = event.message.text
        return text.lower() == "sugarapple"

    def is_going_to_papaya(self, event):
        text = event.message.text
        return text.lower() == "papaya"

    def is_going_to_pomelo(self, event):
        text = event.message.text
        return text.lower() == "pomelo"

    def is_going_to_kiwi(self, event):
        text = event.message.text
        return text.lower() == "kiwi"

    def is_going_to_waxapple(self, event):
        text = event.message.text
        return text.lower() == "waxapple"

    def is_going_to_murcott(self, event):
        text = event.message.text
        return text.lower() == "murcott"

    def is_going_to_orange(self, event):
        text = event.message.text
        return text.lower() == "orange"

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

    def on_enter_guava(self,event):
        print("I'm entering guava")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/koDez1n.jpg'
        nutrition_url = 'https://blog.worldgymtaiwan.com/healthy-food-12-amazing-guava-benefits'
        pick_url = 'https://health.udn.com/health/story/6036/3744844'
        preserve_ur = 'https://bobabobax.blogspot.com/2019/12/blog-post_11.html'
        send_fruit_info(reply_token, image_url,nutrition_url, pick_url, preserve_ur)
        
        self.go_back()
        
    def on_enter_dragonfruit(self,event):
        print("I'm entering dragonfruit")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/dWL0iB3.jpg'
        nutrition_url = 'https://health.ltn.com.tw/article/breakingnews/3571015'
        pick_url = 'https://food.ltn.com.tw/article/9284'
        preserve_ur = 'https://kknews.cc/zh-tw/agriculture/ppa34l8.html'
        send_fruit_info(reply_token, image_url,nutrition_url, pick_url, preserve_ur)
        
        self.go_back()
                
    def on_enter_passionfruit(self,event):
        print("I'm entering passionfruit")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/9LNJy47.jpg'
        nutrition_url = 'https://www.edh.tw/media_article/550'
        pick_url = 'https://blog.wonderfulfood.com.tw/2015/10/26/%E8%AA%A4%E6%9C%83%E5%A4%A7%E4%BA%86%EF%BC%81%E5%8E%9F%E4%BE%86%E5%A4%96%E7%9A%AE%E7%9A%BA%E5%8F%88%E9%86%9C%E7%9A%84%E7%99%BE%E9%A6%99%E6%9E%9C%E6%9C%80%E9%A6%99%E7%94%9C%EF%BC%81/'
        preserve_ur = 'https://www.ysbkg.com/yangshengguwen/zhinan/270186.html'
        send_fruit_info(reply_token, image_url,nutrition_url, pick_url, preserve_ur)
        
        self.go_back()
                    
    def on_enter_mango(self,event):
        print("I'm entering mango")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/74bxFLd.jpg'
        nutrition_url = 'https://health.tvbs.com.tw/nutrition/328717'
        pick_url = 'https://greenbox.tw/Blog/BlogPostNew/4263/'
        preserve_ur = 'https://blog.wonderfulfood.com.tw/2015/06/18/%E7%84%A1%E6%95%B5%E5%A6%99%E6%8B%9B%EF%BC%81%E8%8A%92%E6%9E%9C%E4%BF%9D%E5%AD%98%E8%A1%93/'
        send_fruit_info(reply_token, image_url,nutrition_url, pick_url, preserve_ur)
        
        self.go_back()
                   
    def on_enter_watermelon(self,event):
        print("I'm entering watermelon")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/EvYerNb.jpg'
        nutrition_url = 'https://health.udn.com/health/story/6037/3240933'
        pick_url = 'https://www.epochtimes.com/b5/20/4/29/n12069777.htm'
        preserve_ur = 'https://www.ysbks.com/zh-tw/yszs/zhinan/309078.html'
        send_fruit_info(reply_token, image_url,nutrition_url, pick_url, preserve_ur)
        
        self.go_back()
                           
    def on_enter_pineapple(self,event):
        print("I'm entering pineapple")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/CioYSnK.jpg'
        nutrition_url = 'https://health.udn.com/health/story/6037/5289280'
        pick_url = 'https://www.storm.mg/lifestyle/1047906'
        preserve_ur = 'https://food.ltn.com.tw/article/7478'
        send_fruit_info(reply_token, image_url,nutrition_url, pick_url, preserve_ur)
        
        self.go_back()
                                   
    def on_enter_sugarapple(self,event):
        print("I'm entering sugarapple")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/keZlh6x.jpg'
        nutrition_url = 'https://www.commonhealth.com.tw/article/75928'
        pick_url = 'https://food.ltn.com.tw/article/7151'
        preserve_ur = 'https://kknews.cc/zh-tw/health/ovvkekp.html'
        send_fruit_info(reply_token, image_url,nutrition_url, pick_url, preserve_ur)
        
        self.go_back()
                                           
    def on_enter_papaya(self,event):
        print("I'm entering papaya")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/DOpK07h.jpg'
        nutrition_url = 'https://www.commonhealth.com.tw/article/81913'
        pick_url = 'https://food.ltn.com.tw/article/6177'
        preserve_ur = 'https://kknews.cc/zh-tw/health/l83b8ab.html'
        send_fruit_info(reply_token, image_url,nutrition_url, pick_url, preserve_ur)
        
        self.go_back()
                                                   
    def on_enter_pomelo(self,event):
        print("I'm entering pomelo")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/i8Xnk0e.jpg'
        nutrition_url = 'https://health.tvbs.com.tw/nutrition/318463'
        pick_url = 'https://www.newsmarket.com.tw/blog/123252/'
        preserve_ur = 'https://madoupim.pixnet.net/blog/post/305283791'
        send_fruit_info(reply_token, image_url,nutrition_url, pick_url, preserve_ur)
        
        self.go_back()
                                                           
    def on_enter_kiwi(self,event):
        print("I'm entering kiwi")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/9Hyqmr5.jpg'
        nutrition_url = 'https://www.canceraway.org.tw/page.asp?IDno=1136'
        pick_url = 'http://www.story543.com/post06270041085453'
        preserve_ur = 'https://www.weisfruitshop.com/blog/posts/%E3%80%90%E5%B0%8F%E8%96%87%E6%84%9B%E5%88%86%E4%BA%AB%E3%80%91%E5%A5%87%E7%95%B0%E6%9E%9C%E7%9A%84%E4%BF%9D%E5%AD%98%E7%A7%98%E8%A8%A3%EF%BC%81%F0%9F%A5%9D'
        send_fruit_info(reply_token, image_url,nutrition_url, pick_url, preserve_ur)
        
        self.go_back()
                                                                   
    def on_enter_waxapple(self,event):
        print("I'm entering waxapple")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/zJwxxqS.jpg'
        nutrition_url = 'https://heho.com.tw/archives/149016'
        pick_url = 'https://food.ltn.com.tw/article/7150'
        preserve_ur = 'https://www.ysbks.com/yszs/zhinan/303968.html'
        send_fruit_info(reply_token, image_url,nutrition_url, pick_url, preserve_ur)
        
        self.go_back()
                                                                           
    def on_enter_murcott(self,event):
        print("I'm entering murcott")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/uGqo3Xo.jpg'
        nutrition_url = 'https://www.edh.tw/media_article/321'
        pick_url = 'https://blog.wonderfulfood.com.tw/2017/02/09/%E8%8C%82%E8%B0%B7%E6%9F%91%E7%9A%84%E6%8C%91%E9%81%B8%E3%80%81%E4%BF%9D%E5%AD%98%E3%80%81%E8%88%87%E5%90%83%E6%B3%95/'
        preserve_ur = 'https://www.hucc-coop.tw/event/event_prod/13928'
        send_fruit_info(reply_token, image_url,nutrition_url, pick_url, preserve_ur)
        
        self.go_back()
                                                                                   
    def on_enter_orange(self,event):
        print("I'm entering orange")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/A80aC6z.jpg'
        nutrition_url = 'https://health.tvbs.com.tw/nutrition/322726'
        pick_url = 'https://fresh438.pixnet.net/blog/post/41825692'
        preserve_ur = 'https://www.seasonal-fruit.com/copy-of-33'
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
