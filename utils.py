import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage
##########################################
from linebot.models import MessageEvent, URITemplateAction, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction, CarouselTemplate, CarouselColumn
##########################################
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        type='image',
        original_content_url=url,
        preview_image_url=url
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

#######################################################################################################
def send_restaurant_info(reply_token, image_url, info_url, map_url, rec_url):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='餐廳資訊',
            text='點擊看介紹、地圖、更多推薦!',
            thumbnail_image_url=image_url,
            actions=[
                URITemplateAction(
                    label='介紹',
                    uri=info_url
                ), URITemplateAction(
                    label='地圖',
                    uri=map_url
                ), URITemplateAction(
                    label='更多推薦',
                    uri=rec_url
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='餐點類型',
            text='點擊你有興趣的料理',
            thumbnail_image_url='https://i.imgur.com/ZWMxMBT.jpg',
            actions=[
                MessageTemplateAction(
                    label='飯類',
                    text='rice'
                ),
                MessageTemplateAction(
                    label='壽司、生魚片',
                    text='sushi'
                ),
                MessageTemplateAction(
                    label='拉麵',
                    text='ramen'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_thai_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='泰式餐廳',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://i.imgur.com/M5qC6xd.jpg',
            actions=[
                MessageTemplateAction(
                    label='山豬林',
                    text='thai1'
                ),
                MessageTemplateAction(
                    label='BITCH小姐',
                    text='thai2'
                ),
                MessageTemplateAction(
                    label='DEMO',
                    text='thai3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_korean_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='韓式餐廳',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://i.imgur.com/I4w6jPT.jpg',
            actions=[
                MessageTemplateAction(
                    label='豬對有',
                    text='korean1'
                ),
                MessageTemplateAction(
                    label='韓朝',
                    text='korean2'
                ),
                MessageTemplateAction(
                    label='老韓家韓式廚房',
                    text='korean3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_tainan_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='排隊美食',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://i.imgur.com/prSNnGs.jpg',
            actions=[
                MessageTemplateAction(
                    label='小赤佬',
                    text='tainan1'
                ),
                MessageTemplateAction(
                    label='文章牛肉湯',
                    text='tainan2'
                ),
                MessageTemplateAction(
                    label='富盛號',
                    text='tainan3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_hotpot_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='火鍋',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://i.imgur.com/80waVGx.jpg',
            actions=[
                MessageTemplateAction(
                    label='築間',
                    text='hotpot1'
                ),
                MessageTemplateAction(
                    label='五鮮極',
                    text='hotpot2'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_diner_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='美式餐廳',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://i.imgur.com/mupVQCY.jpg',
            actions=[
                MessageTemplateAction(
                    label='sk尚恩廚房',
                    text='diner1'
                ),
                MessageTemplateAction(
                    label='可可貝里',
                    text='diner2'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_rice_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='飯類',
            text='想吃什麼',
            thumbnail_image_url='https://i.imgur.com/aTWsQGB.jpg',
            actions=[
                MessageTemplateAction(
                    label='丼飯',
                    text='donburi'
                ),
                MessageTemplateAction(
                    label='豬排',
                    text='tonkatsu'
                ),
                MessageTemplateAction(
                    label='日式定食',
                    text='teishoku'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_rice_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='丼飯',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://i.imgur.com/aTWsQGB.jpg',
            actions=[
                MessageTemplateAction(
                    label='肉肉控',
                    text='donburi1'
                ),
                MessageTemplateAction(
                    label='職人雙響丼',
                    text='donburi2'
                ),
                MessageTemplateAction(
                    label='炙丼家',
                    text='donburi3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_teishoku_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='日式定食',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://i.imgur.com/TU6ESPm.jpg',
            actions=[
                MessageTemplateAction(
                    label='漁人食堂',
                    text='teishoku1'
                ),
                MessageTemplateAction(
                    label='櫻之庭',
                    text='teishoku2'
                ),
                MessageTemplateAction(
                    label='石火山碳燒蓋飯',
                    text='teishoku3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_sushi_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='壽司、生魚片',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://i.imgur.com/t7fcAMD.jpg',
            actions=[
                MessageTemplateAction(
                    label='毛丼',
                    text='sushi1'
                ),
                MessageTemplateAction(
                    label='鮨次郎',
                    text='sushi2'
                ),
                MessageTemplateAction(
                    label='日暮壽司',
                    text='sushi3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_ramen_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='拉麵',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://i.imgur.com/MXrZ5Bw.jpg',
            actions=[
                MessageTemplateAction(
                    label='覺丸',
                    text='ramen1'
                ),
                MessageTemplateAction(
                    label='八峰亭',
                    text='ramen2'
                ),
                MessageTemplateAction(
                    label='寶來軒',
                    text='ramen3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_japanese_tonkatsu_restaurant_type(reply_token, id):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='豬排',
            text='點擊餐廳看介紹',
            thumbnail_image_url='https://i.imgur.com/ZWMxMBT.jpg',
            actions=[
                MessageTemplateAction(
                    label='元味屋',
                    text='tonkatsu1'
                ),
                MessageTemplateAction(
                    label='豚讚',
                    text='tonkatsu2'
                ),
                MessageTemplateAction(
                    label='森井',
                    text='tonkatsu3'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"


def send_button_carousel(id):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/M5qC6xd.jpg',
                    title='餐廳推薦',
                    text='想吃什麼種類?',
                    actions=[
                        MessageTemplateAction(
                            label='美式',
                            text='diner'
                        ),
                        MessageTemplateAction(
                            label='泰式',
                            text='thai cuisine'
                        ),
                        MessageTemplateAction(
                            label='韓式',
                            text='korean cuisine'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/TU6ESPm.jpg',
                    title='餐廳推薦',
                    text='想吃什麼種類?',
                    actions=[
                        MessageTemplateAction(
                            label='日式',
                            text='japanese cuisine'
                        ),
                        MessageTemplateAction(
                            label='火鍋',
                            text='hotpot'
                        ),
                        MessageTemplateAction(
                            label='排隊美食',
                            text='tainan'
                        ),
                    ]
                )
            ]
        )
    )
    line_bot_api.push_message(id, message)

    return "OK"

###############################################################################################################
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
