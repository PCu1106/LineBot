from transitions.extensions import GraphMachine
from utils import send_text_message
######################################################################
from utils import send_text_message, send_tainan_restaurant_type, send_hotpot_restaurant_type, send_diner_restaurant_type, send_korean_restaurant_type, send_thai_restaurant_type, send_japanese_ramen_restaurant_type, send_japanese_sushi_restaurant_type, send_japanese_teishoku_restaurant_type, send_japanese_tonkatsu_restaurant_type, send_restaurant_info, send_button_carousel, send_japanese_type, send_japanese_rice_type, send_japanese_rice_restaurant_type

######################################################################

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    # def is_going_to_state1(self, event):
    #     text = event.message.text
    #     return text.lower() == "go to state1"

    # def is_going_to_state2(self, event):
    #     text = event.message.text
    #     return text.lower() == "go to state2"

    # def on_enter_state1(self, event):
    #     print("I'm entering state1")

    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "Trigger state1")
    #     self.go_back()

    # def on_exit_state1(self):
    #     print("Leaving state1")

    # def on_enter_state2(self, event):
    #     print("I'm entering state2")

    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "Trigger state2")
    #     self.go_back()

    # def on_exit_state2(self):
    #     print("Leaving state2")

######################################################################
    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"

    def is_going_to_rice(self, event):
        text = event.message.text
        return text.lower() == "rice"

    def is_going_to_sushi(self, event):
        text = event.message.text
        return text.lower() == "sushi"

    def is_going_to_thai(self, event):
        text = event.message.text
        return text.lower() == "thai cuisine"

    def is_going_to_diner(self, event):
        text = event.message.text
        return text.lower() == "diner"

    def is_going_to_hotpot(self, event):
        text = event.message.text
        return text.lower() == "hotpot"

    def is_going_to_tainan(self, event):
        text = event.message.text
        return text.lower() == "tainan"

    def is_going_to_ramen(self, event):
        text = event.message.text
        return text.lower() == "ramen"

    def is_going_to_donburi(self, event):
        text = event.message.text
        return text.lower() == "donburi"

    def is_going_to_tonkatsu(self, event):
        text = event.message.text
        return text.lower() == "tonkatsu"

    def is_going_to_teishoku(self, event):
        text = event.message.text
        return text.lower() == "teishoku"

    def is_going_to_tainan_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "tainan1"

    def is_going_to_tainan_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "tainan2"

    def is_going_to_tainan_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "tainan3"

    def is_going_to_donburi_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "donburi1"

    def is_going_to_donburi_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "donburi2"

    def is_going_to_donburi_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "donburi3"

    def is_going_to_japanese(self, event):
        text = event.message.text
        return text.lower() == "japanese cuisine"

    def is_going_to_korean(self, event):
        text = event.message.text
        return text.lower() == "korean cuisine"

    def is_going_to_hotpot_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "hotpot1"

    def is_going_to_hotpot_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "hotpot2"

    def is_going_to_diner_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "diner1"

    def is_going_to_diner_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "diner2"

    def is_going_to_tonkatsu_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "tonkatsu1"

    def is_going_to_tonkatsu_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "tonkatsu2"

    def is_going_to_tonkatsu_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "tonkatsu3"

    def is_going_to_teishoku_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "teishoku1"

    def is_going_to_teishoku_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "teishoku2"

    def is_going_to_teishoku_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "teishoku3"

    def is_going_to_sushi_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "sushi1"

    def is_going_to_sushi_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "sushi2"

    def is_going_to_sushi_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "sushi3"

    def is_going_to_ramen_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "ramen1"

    def is_going_to_ramen_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "ramen2"

    def is_going_to_ramen_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "ramen3"

    def is_going_to_thai_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "thai1"

    def is_going_to_thai_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "thai2"

    def is_going_to_thai_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "thai3"

    def is_going_to_korean_restaurant1(self, event):
        text = event.message.text
        return text.lower() == "korean1"

    def is_going_to_korean_restaurant2(self, event):
        text = event.message.text
        return text.lower() == "korean2"

    def is_going_to_korean_restaurant3(self, event):
        text = event.message.text
        return text.lower() == "korean3"

    def on_enter_start(self, event):
        print("I'm entering start")

        userid = event.source.user_id
        send_button_carousel(userid)

    def on_enter_rice(self, event):
        print("I'm entering rice")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_japanese_rice_type(reply_token, userid)

    def on_enter_sushi(self, event):
        print("I'm entering sushi")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_japanese_sushi_restaurant_type(reply_token, userid)

    def on_enter_ramen(self, event):
        print("I'm entering ramen")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_japanese_ramen_restaurant_type(reply_token, userid)

    def on_enter_donburi(self, event):
        print("I'm entering donburi")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_japanese_rice_restaurant_type(reply_token, userid)

    def on_enter_tonkatsu(self, event):
        print("I'm entering tonkatsu")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_japanese_tonkatsu_restaurant_type(reply_token, userid)

    def on_enter_teishoku(self, event):
        print("I'm entering teishoku")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_japanese_teishoku_restaurant_type(reply_token, userid)

    def on_enter_donburi_restaurant1(self, event):
        print("I'm entering donburi_restaurant1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/ungADCq.jpg'
        info_url = 'https://www.tainanlohas.cc/2019/11/nikurourou.html'
        map_url = 'https://www.google.com/maps/search/%E8%82%89%E8%82%89%E6%8E%A7/@22.9953766,120.2108113,14z'
        rec_url = 'https://tainanfoodeat.blogspot.com/2020/01/blog-post_12.html'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_donburi_restaurant2(self, event):
        print("I'm entering donburi_restaurant2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/HlnC9N6.jpg'
        info_url = 'https://rabbit28bear.pixnet.net/blog/post/16597757-%E3%80%90%E5%8F%B0%E5%8D%97%E6%9D%B1%E5%8D%80%E7%BE%8E%E9%A3%9F%E3%80%91%E5%8F%B0%E5%8D%97%E6%88%90%E5%A4%A7%E8%82%B2%E6%A8%82%E8%A1%97%E7%BE%8E%E9%A3%9F-%E3%80%88%E8%81%B7'
        map_url = 'https://www.google.com/maps/place/%E8%81%B7%E4%BA%BA%E9%9B%99%E9%A5%97%E4%B8%BC+%E8%82%B2%E6%A8%82%E5%BA%97/@22.9944574,120.2126457,17z/data=!3m1!4b1!4m5!3m4!1s0x346e768dc4f5f831:0x43732136c613f9eb!8m2!3d22.9944574!4d120.2148344'
        rec_url = 'https://tainanfoodeat.blogspot.com/2020/01/blog-post_12.html'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_donburi_restaurant3(self, event):
        print("I'm entering donburi_restaurant3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/aTWsQGB.jpg'
        info_url = 'https://www.mrtainan.com/2020/05/062099933.html'
        map_url = 'https://www.google.com/maps?q=%E7%82%99%E4%B8%BC%E5%AE%B6&source=lmns&bih=722&biw=1536&hl=zh-TW&sa=X&ved=2ahUKEwj73sC22e3tAhUUxosBHZmdA_UQ_AUoAnoECAEQAg'
        rec_url = 'https://tainanfoodeat.blogspot.com/2020/01/blog-post_12.html'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_tonkatsu_restaurant1(self, event):
        print("I'm entering tonkatsu_restaurant1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/hvBpGNW.jpg'
        info_url = 'https://imsean.pixnet.net/blog/post/43287250'
        map_url = 'https://www.google.com/maps?q=%E5%85%83%E5%91%B3%E5%B1%8B&bih=722&biw=1536&hl=zh-TW&um=1&ie=UTF-8&sa=X&ved=2ahUKEwjxgNza3e3tAhVIHKYKHVONDa4Q_AUoAnoECAUQBA'
        rec_url = 'https://www.dcard.tw/f/food/p/233099641'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_tonkatsu_restaurant2(self, event):
        print("I'm entering tonkatsu_restaurant2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/ZWMxMBT.jpg'
        info_url = 'https://iammissgreedy.blogspot.com/2018/08/tuentzan.html'
        map_url = 'https://www.google.com/maps?hl=zh-TW&biw=1536&bih=722&sxsrf=ALeKk01zx4GOqcbTL3UnAGUTbJYpENRGCw:1609057820915&q=%E8%B1%9A%E8%AE%9A&gs_lcp=CgZwc3ktYWIQAzICCAAyBAgAEEMyAggAMgIIADoFCAAQsQM6CAgAELEDEIMBOggIABAFEAoQHjoGCAAQBRAeOgQIABANUKH_BFjHhAVg3IkFaABwAHgAgAFyiAGvA5IBAzYuMZgBAKABAaoBB2d3cy13aXrAAQE&uact=5&um=1&ie=UTF-8&sa=X&ved=2ahUKEwiqjfTm3-3tAhUOc5QKHXjABr4Q_AUoAXoECAUQAw'
        rec_url = 'https://www.dcard.tw/f/food/p/233099641'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_tonkatsu_restaurant3(self, event):
        print("I'm entering tonkatsu_restaurant3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/NztQ03c.jpg'
        info_url = 'https://hululu.tw/senjing/'
        map_url = 'https://www.google.com/maps/place/701%E5%8F%B0%E5%8D%97%E5%B8%82%E6%9D%B1%E5%8D%80%E6%9D%B1%E5%AE%89%E8%B7%AF80%E8%99%9F/@22.9927371,120.224382,17z/data=!3m1!4b1!4m5!3m4!1s0x346e7695be7a457f:0xfb5bd157bf368334!8m2!3d22.9927371!4d120.2265707?hl=zh-TW'
        rec_url = 'https://www.dcard.tw/f/food/p/233099641'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_teishoku_restaurant1(self, event):
        print("I'm entering teishoku_restaurant1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/d78p69K.jpg'
        info_url = 'https://chioutian.pixnet.net/blog/post/463174688'
        map_url = 'https://www.google.com/maps?hl=zh-TW&sxsrf=ALeKk00SkfuP1qPouUdZW3wHxiJD1ZHKSQ:1609059968221&q=%E6%BC%81%E4%BA%BA%E9%A3%9F%E5%A0%82&biw=1536&bih=722&um=1&ie=UTF-8&sa=X&ved=2ahUKEwjA9OHD5-3tAhViNKYKHZb7DqIQ_AUoAXoECAUQAw'
        rec_url = 'https://ifoodie.tw/city/%E5%8F%B0%E5%8D%97%E5%B8%82?q=%E6%97%A5%E5%BC%8F%E5%AE%9A%E9%A3%9F'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_teishoku_restaurant2(self, event):
        print("I'm entering teishoku_restaurant2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/YqMnklL.jpg'
        info_url = 'https://www.mrtainan.com/2019/12/062082068.html'
        map_url = 'https://www.google.com/maps?bih=722&biw=1536&hl=zh-TW&sxsrf=ALeKk03oPQ33e9Na1SDyrGUXYCKKbosGfA:1609059932220&q=%E6%AB%BB%E4%B9%8B%E5%BA%AD+%E5%8F%B0%E5%8D%97&gs_lcp=CgZwc3ktYWIQARgAMgQIABBDMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAOgUIABCwAzoHCAAQsAMQHjoJCAAQsAMQCBAeOgUIABDNAjoICAAQsQMQgwE6BQgAELEDOgcIIxDqAhAnUITSAVjz9QFgmowCaAJwAHgAgAFLiAGOBJIBATmYAQCgAQGqAQdnd3Mtd2l6sAEKyAEKwAEB&um=1&ie=UTF-8&sa=X&ved=2ahUKEwidy8--5-3tAhWbwosBHSgPAn8Q_AUoAnoECAUQBA'
        rec_url = 'https://ifoodie.tw/city/%E5%8F%B0%E5%8D%97%E5%B8%82?q=%E6%97%A5%E5%BC%8F%E5%AE%9A%E9%A3%9F'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_teishoku_restaurant3(self, event):
        print("I'm entering teishoku_restaurant3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/TU6ESPm.jpg'
        info_url = 'https://pai0916.pixnet.net/blog/post/352287649'
        map_url = 'https://www.google.com/maps/place/%E7%9F%B3%E7%81%AB%E5%B1%B1%E7%A2%B3%E7%87%92%E8%93%8B%E9%A3%AF/@22.9942189,120.2185924,17z/data=!3m1!4b1!4m5!3m4!1s0x346e77289656acef:0x4352849a773f3c95!8m2!3d22.9942189!4d120.2207811?hl=zh-TW'
        rec_url = 'https://ifoodie.tw/city/%E5%8F%B0%E5%8D%97%E5%B8%82?q=%E6%97%A5%E5%BC%8F%E5%AE%9A%E9%A3%9F'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_sushi_restaurant1(self, event):
        print("I'm entering sushi_restaurant1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/dVoR8H2.jpg'
        info_url = 'https://shu333.pixnet.net/blog/post/186013188'
        map_url = 'https://www.google.com/maps/place/%E6%AF%9B%E4%B8%BC+%E4%B8%BC%E9%A3%AF%E5%B0%88%E9%96%80%E5%BA%97/@22.9888063,120.2130652,17z/data=!3m1!4b1!4m5!3m4!1s0x346e768ff2b7578b:0x3e5032f6e73245e!8m2!3d22.9888063!4d120.2152539?hl=zh-TW'
        rec_url = 'https://zi.media/@AI-choiced/post/Bvav0Q'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_sushi_restaurant2(self, event):
        print("I'm entering sushi_restaurant2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/t7fcAMD.jpg'
        info_url = 'https://zi.media/@decing/post/5FL28J'
        map_url = 'https://www.google.com/maps/place/%E9%AE%A8%E6%AC%A1%E9%83%8E%E5%A3%BD%E5%8F%B8%E5%B0%88%E8%B3%A3/@22.9875573,120.2287199,17z/data=!3m1!4b1!4m8!1m2!2m1!1z5Y-w5Y2XIOeUn-mtmueJh-WjveWPuA!3m4!1s0x346e76bd011ffda7:0xa707c36f3943af7b!8m2!3d22.9875573!4d120.2309086?hl=zh-TW'
        rec_url = 'https://zi.media/@AI-choiced/post/Bvav0Q'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_sushi_restaurant3(self, event):
        print("I'm entering sushi_restaurant3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/Xx6qZIO.jpg'
        info_url = 'https://hululu.tw/day-sushi/'
        map_url = 'https://www.google.com/maps?hl=zh-TW&biw=1536&bih=722&sxsrf=ALeKk00dCLm_anyFol9UH2W0GQ1Rldvl4Q:1609062312513&q=%E5%8F%B0%E5%8D%97+%E6%97%A5%E6%9A%AE%E5%A3%BD%E5%8F%B8&gs_lcp=CgZwc3ktYWIQARgAMgIIADICCCYyAggmOgUIABCwAzoICAAQsQMQgwE6BAgAEEM6BQgAEM0CUNelAViAsAFg974BaAFwAHgAgAFTiAHXA5IBATaYAQCgAQGqAQdnd3Mtd2l6yAEBwAEB&um=1&ie=UTF-8&sa=X&ved=2ahUKEwi0--Co8O3tAhXww4sBHZh9AvUQ_AUoAXoECAUQAw'
        rec_url = 'https://zi.media/@AI-choiced/post/Bvav0Q'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_ramen_restaurant1(self, event):
        print("I'm entering ramen_restaurant1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/MXrZ5Bw.jpg'
        info_url = 'https://decing.tw/tainan-juewanramen/'
        map_url = 'https://www.google.com/maps/place/%E8%A6%BA%E4%B8%B8%E6%8B%89%E9%BA%B5/@22.9959558,120.2276917,17z/data=!3m1!4b1!4m5!3m4!1s0x346e76c075aa3a33:0x6399402cf32a429c!8m2!3d22.9959558!4d120.2298804?hl=zh-TW'
        rec_url = 'https://ku5553221.pixnet.net/blog/post/206988886'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_ramen_restaurant2(self, event):
        print("I'm entering ramen_restaurant2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/AeYIU5g.jpg'
        info_url = 'https://ku5553221.pixnet.net/blog/post/206615113'
        map_url = 'https://www.google.com/maps?sxsrf=ALeKk00UBM-1aKEkJ2S_7MXE1ULKVk8HlA:1609063231730&q=%E5%85%AB%E5%B3%B0%E4%BA%AD&gs_lcp=CgZwc3ktYWIQARgAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADICCAAyAggAMgIIADoFCAAQsQM6BAgAEEM6CAgAELEDEIMBULwGWMANYK8ZaABwAngAgAFBiAHPApIBATaYAQCgAQGqAQdnd3Mtd2l6wAEB&um=1&ie=UTF-8&sa=X&ved=2ahUKEwigxvre8-3tAhXGGKYKHTeFD_EQ_AUoAXoECAUQAw'
        rec_url = 'https://ku5553221.pixnet.net/blog/post/206988886'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_ramen_restaurant3(self, event):
        print("I'm entering ramen_restaurant3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/SDJeiOP.jpg'
        info_url = 'https://ku5553221.pixnet.net/blog/post/216776978'
        map_url = 'https://www.google.com/maps/place/%E5%AF%B6%E4%BE%86%E8%BB%92/@23.0019977,120.2036181,17z/data=!3m1!4b1!4m5!3m4!1s0x346e765fea7e7689:0xb6fff831dde12cb!8m2!3d23.0019977!4d120.2058068'
        rec_url = 'https://ku5553221.pixnet.net/blog/post/206988886'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_thai_restaurant1(self, event):
        print("I'm entering thai_restaurant1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/M5qC6xd.jpg'
        info_url = 'https://niceclaup313.pixnet.net/blog/post/229094642-%E3%80%90%E5%8F%B0%E5%8D%97%E6%9D%B1%E5%8D%80%E3%80%91%E3%80%8E%E5%B1%B1%E8%B1%AC%E6%9E%97shanzhulin%E3%80%8F~%E6%88%90%E5%A4%A7%E5%91%A8%E9%82%8A%EF%BC%8C'
        map_url = 'https://www.google.com/maps/place/%E5%B1%B1%E8%B1%AC%E6%9E%97+shanzhulin+%E6%B3%B0%E5%BC%8F%E6%96%99%E7%90%86/@22.9925441,120.2186532,17z/data=!3m1!4b1!4m5!3m4!1s0x346e7739c06ca7df:0xd2df5797794ff609!8m2!3d22.9925441!4d120.2208419'
        rec_url = 'https://bopomo.tw/2020-05-17/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_thai_restaurant2(self, event):
        print("I'm entering thai_restaurant2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/bp3GCKZ.jpg'
        info_url = 'https://hululu.tw/bitch/'
        map_url = 'https://www.google.com/maps/place/BitchFryFry+%E5%8F%B0%E5%8D%97%E5%BA%97/@22.9900427,120.2179623,17z/data=!3m1!4b1!4m5!3m4!1s0x346e776e00f8629d:0xbf860b80ebfc1d9d!8m2!3d22.9900427!4d120.220151'
        rec_url = 'https://bopomo.tw/2020-05-17/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_thai_restaurant3(self, event):
        print("I'm entering thai_restaurant3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/bp3GCKZ.jpg'
        info_url = 'https://hululu.tw/bitch/'
        map_url = 'https://www.google.com/maps/place/BitchFryFry+%E5%8F%B0%E5%8D%97%E5%BA%97/@22.9900427,120.2179623,17z/data=!3m1!4b1!4m5!3m4!1s0x346e776e00f8629d:0xbf860b80ebfc1d9d!8m2!3d22.9900427!4d120.220151'
        rec_url = 'https://bopomo.tw/2020-05-17/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_korean_restaurant1(self, event):
        print("I'm entering korean_restaurant1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/uiP2xDY.jpg'
        info_url = 'https://13shaniu.tw/pig-friend1/'
        map_url = 'https://www.google.com/maps/place/%E8%B1%AC%E5%B0%8D%E6%9C%89%E9%9F%93%E5%BC%8F%E7%83%A4%E8%82%89%E5%90%83%E5%88%B0%E9%A3%BD/@22.9873926,120.1924757,14.95z/data=!4m8!1m2!2m1!1z6LGs5bCN5pyJ!3m4!1s0x346e7712c2e49c85:0x22c3a9c5a0a3584d!8m2!3d22.9889962!4d120.187955?hl=zh-TW'
        rec_url = 'https://www.gomaji.com/blog/%E5%8F%B0%E5%8D%97%E9%9F%93%E5%BC%8F%E6%96%99%E7%90%86/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_korean_restaurant2(self, event):
        print("I'm entering korean_restaurant2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/I4w6jPT.jpg'
        info_url = 'https://flower033880.pixnet.net/blog/post/228005078-%E5%8F%B0%E5%8D%97%E9%9F%93%E5%BC%8F%E6%96%99%E7%90%86%E3%80%8E%E9%9F%93%E6%9C%9D-%E6%9D%B1%E5%AF%A7%E5%BA%97%E3%80%8F%E6%95%B8%E5%8D%81%E7%A8%AE%E5%B0%8F%E8%8F%9C%E5%90%83'
        map_url = 'https://www.google.com/maps?q=%E9%9F%93%E6%9C%9D&source=lmns&bih=722&biw=1536&hl=zh-TW&sa=X&ved=2ahUKEwjmh73h_u3tAhWCAd4KHU7-DAwQ_AUoAXoECAEQAQ'
        rec_url = 'https://www.gomaji.com/blog/%E5%8F%B0%E5%8D%97%E9%9F%93%E5%BC%8F%E6%96%99%E7%90%86/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_korean_restaurant3(self, event):
        print("I'm entering korean_restaurant3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/bqFV5LY.jpg'
        info_url = 'https://rabbit77610.pixnet.net/blog/post/45340812'
        map_url = 'https://www.google.com/maps?q=%E8%80%81%E9%9F%93%E5%AE%B6%E9%9F%93%E5%BC%8F%E5%BB%9A%E6%88%BF&bih=722&biw=1536&hl=zh-TW&um=1&ie=UTF-8&sa=X&ved=2ahUKEwi0g8-q_u3tAhVRCqYKHekQC-sQ_AUoAXoECAUQAw'
        rec_url = 'https://www.gomaji.com/blog/%E5%8F%B0%E5%8D%97%E9%9F%93%E5%BC%8F%E6%96%99%E7%90%86/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_diner_restaurant1(self, event):
        print("I'm entering diner_restaurant1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/mupVQCY.jpg'
        info_url = 'https://hululu.tw/sk/'
        map_url = 'https://www.google.com/maps/place/SK%E5%B0%9A%E6%81%A9%E5%BB%9A%E6%88%BF/@22.9867002,120.2114134,15z/data=!4m8!1m2!2m1!1z5Y-w5Y2XIOe-juW8j-a8ouWgoQ!3m4!1s0x346e76c00ad0c89d:0xb5f051b493f8c27e!8m2!3d22.995466!4d120.2280305?hl=zh-TW'
        rec_url = 'https://jeremyckt2.pixnet.net/blog/post/228688148-%5B%E7%BE%8E%E9%A3%9F%E6%87%B6%E4%BA%BA%E5%8C%85%5D-%E5%8F%B0%E5%8D%97%E5%B8%82%E7%BE%8E%E5%BC%8F%E9%A4%90%E5%BB%B3%E6%87%B6%E4%BA%BA%E5%8C%85-%E5%B7%B2%E9%80%A0%E8%A8%AA'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_diner_restaurant2(self, event):
        print("I'm entering diner_restaurant2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/uHUjOIa.jpg'
        info_url = 'https://www.tainanlohas.cc/2020/03/kokopeli-cafe.html'
        map_url = 'https://www.google.com/maps/place/%E5%8F%AF%E5%8F%AF%E8%B2%9D%E9%87%8C%E7%BE%8E%E5%BC%8F%E9%A4%90%E5%BB%B3/@22.9867002,120.2114134,15z/data=!4m8!1m2!2m1!1z5Y-w5Y2XIOe-juW8j-a8ouWgoQ!3m4!1s0x0:0x81af065864d7547e!8m2!3d22.9939406!4d120.2129683?hl=zh-TW'
        rec_url = 'https://jeremyckt2.pixnet.net/blog/post/228688148-%5B%E7%BE%8E%E9%A3%9F%E6%87%B6%E4%BA%BA%E5%8C%85%5D-%E5%8F%B0%E5%8D%97%E5%B8%82%E7%BE%8E%E5%BC%8F%E9%A4%90%E5%BB%B3%E6%87%B6%E4%BA%BA%E5%8C%85-%E5%B7%B2%E9%80%A0%E8%A8%AA'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_hotpot_restaurant1(self, event):
        print("I'm entering hotpot_restaurant1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/80waVGx.jpg'
        info_url = 'https://pingu.blog/jhujian-lukang/'
        map_url = 'https://www.google.com/maps/place/%E7%AF%89%E9%96%93%E5%B9%B8%E7%A6%8F%E9%8D%8B%E7%89%A9+%E5%8F%B0%E5%8D%97%E6%88%90%E5%A4%A7%E5%BA%97/@22.9922191,120.2159616,14z/data=!4m8!1m2!2m1!1z56-J6ZaT!3m4!1s0x346e77cc9f6bea71:0xedfb2416b5ed26ad!8m2!3d22.9959131!4d120.218392?hl=zh-TW'
        rec_url = 'https://decing.tw/hotpot-lazy/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_hotpot_restaurant2(self, event):
        print("I'm entering hotpot_restaurant2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/pZy3Lox.jpg'
        info_url = 'https://www.shiamilong.cc/2019/06/blog-post_91.html'
        map_url = 'https://www.google.com/maps/place/%E4%BA%94%E9%AE%AE%E7%B4%9A%E5%B9%B3%E5%83%B9%E9%8D%8B%E7%89%A9%E5%8F%B0%E5%8D%97%E5%8C%97%E9%96%80%E5%BA%97/@22.9922191,120.2159616,14z/data=!4m8!1m2!2m1!1z5LqU6a6u5qW1!3m4!1s0x346e77b8252bd4c3:0x6e79d6f25bc79904!8m2!3d23.0036471!4d120.2136585?hl=zh-TW'
        rec_url = 'https://decing.tw/hotpot-lazy/'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_tainan_restaurant1(self, event):
        print("I'm entering tainan_restaurant1")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/kkPedY5.jpg'
        info_url = 'https://pinkmayday0928.pixnet.net/blog/post/459150811'
        map_url = 'https://www.google.com/maps/place/%E5%B0%8F%E8%B5%A4%E4%BD%AC%E5%B9%B2%E9%8D%8B+%E8%82%B2%E6%A8%82%E5%BA%97/@22.9954051,120.2152844,17z/data=!3m1!4b1!4m5!3m4!1s0x346e769264b112d7:0xc618979fe2c749d8!8m2!3d22.9954051!4d120.2174731?hl=zh-TW'
        rec_url = 'https://kenalice.tw/blog/post/tainan'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_tainan_restaurant2(self, event):
        print("I'm entering tainan_restaurant2")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/prSNnGs.jpg'
        info_url = 'https://fashion.ettoday.net/news/1521636'
        map_url = 'https://www.google.com/maps/place/%E6%96%87%E7%AB%A0%E7%89%9B%E8%82%89%E6%B9%AF-%E9%80%B1%E6%9C%AB%E5%8F%8A%E5%81%87%E6%97%A5%E6%AD%A1%E8%BF%8E%E8%87%B3%E6%96%B0%E5%BA%97+%E5%AE%89%E5%B9%B3%E8%B7%AF300%E8%99%9F%E7%94%A8%E9%A4%90/@22.9987751,120.1675532,17z/data=!3m1!4b1!4m5!3m4!1s0x346e761abb62710d:0xc31bcd84dd49574a!8m2!3d22.9987751!4d120.1697419?hl=zh-TW'
        rec_url = 'https://www.storm.mg/lifestyle/376033?page=1'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_tainan_restaurant3(self, event):
        print("I'm entering tainan_restaurant3")
        reply_token = event.reply_token
        image_url = 'https://i.imgur.com/FotJop0.jpg'
        info_url = 'https://anikolife.com/fushenghao/'
        map_url = 'https://www.google.com/maps/place/%E5%B1%B1%E8%B1%AC%E6%9E%97+shanzhulin+%E6%B3%B0%E5%BC%8F%E6%96%99%E7%90%86/@22.9925441,120.2186532,17z/data=!3m1!4b1!4m5!3m4!1s0x346e7739c06ca7df:0xd2df5797794ff609!8m2!3d22.9925441!4d120.2208419'
        rec_url = 'https://www.google.com/maps?q=%E5%AF%8C%E7%9B%9B%E8%99%9F&source=lmns&bih=722&biw=1536&hl=zh-TW&sa=X&ved=2ahUKEwibw5q_ju7tAhVMMt4KHWIaCXoQ_AUoAXoECAEQAQ'
        send_restaurant_info(reply_token, image_url,
                             info_url, map_url, rec_url)
        self.go_back()

    def on_enter_japanese(self, event):
        print("I'm entering japanese")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_japanese_type(reply_token, userid)

    def on_enter_thai(self, event):
        print("I'm entering thai")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_thai_restaurant_type(reply_token, userid)

    def on_enter_korean(self, event):
        print("I'm entering korean")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_korean_restaurant_type(reply_token, userid)

    def on_enter_diner(self, event):
        print("I'm entering korean")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_diner_restaurant_type(reply_token, userid)

    def on_enter_hotpot(self, event):
        print("I'm entering hotpot")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_hotpot_restaurant_type(reply_token, userid)

    def on_enter_tainan(self, event):
        print("I'm entering tainan")

        reply_token = event.reply_token
        userid = event.source.user_id
        send_tainan_restaurant_type(reply_token, userid)
######################################################################
