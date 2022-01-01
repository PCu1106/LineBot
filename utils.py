import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage,CarouselTemplate,CarouselColumn,MessageTemplateAction,ImageSendMessage,ButtonsTemplate,URITemplateAction


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

def send_button_carousel(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://imgur.com/DMuabwX.jpg',
                    title='春季',
                    text='搜尋當月水果',
                    actions=[
                        MessageTemplateAction(
                            label='二月',
                            text='feb'
                        ),
                        MessageTemplateAction(
                            label='三月',
                            text='mar'
                        ),
                        MessageTemplateAction(
                            label='四月',
                            text='apr'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/pqKqQzU.jpg',
                    title='夏季',
                    text='搜尋當月水果',
                    actions=[
                        MessageTemplateAction(
                            label='五月',
                            text='may'
                        ),
                        MessageTemplateAction(
                            label='六月',
                            text='jun'
                        ),
                        MessageTemplateAction(
                            label='七月',
                            text='jul'
                        )
                    ]
                ) ,
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/hkOiLZu.jpg',
                    title='秋季',
                    text='搜尋當月水果',
                    actions=[
                        MessageTemplateAction(
                            label='八月',
                            text='aug'
                        ),
                        MessageTemplateAction(
                            label='九月',
                            text='sep'
                        ),
                        MessageTemplateAction(
                            label='十月',
                            text='oct'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i.imgur.com/0dLlL4L.jpg',
                    title='冬季',
                    text='搜尋當月水果',
                    actions=[
                        MessageTemplateAction(
                            label='十一月',
                            text='nov'
                        ),
                        MessageTemplateAction(
                            label='十二月',
                            text='dec'
                        ),
                        MessageTemplateAction(
                            label='一月',
                            text='jan'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_feb(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='二月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='香蕉',
                            text='banana'
                        ),
                        MessageTemplateAction(
                            label='芭樂',
                            text='guava'
                        ),
                        MessageTemplateAction(
                            label='釋迦',
                            text='sugarapple'
                        )
                    ]
                ),
                CarouselColumn(
                    title='二月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='奇異果',
                            text='kiwi'
                        ),
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        ),
                        MessageTemplateAction(
                            label='茂谷柑',
                            text='murcott'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_mar(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='三月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='香蕉',
                            text='banana'
                        ),
                        MessageTemplateAction(
                            label='芭樂',
                            text='guava'
                        ),
                        MessageTemplateAction(
                            label='奇異果',
                            text='kiwi'
                        )
                    ]
                ),
                CarouselColumn(
                    title='三月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        ),
                        MessageTemplateAction(
                            label='茂谷柑',
                            text='murcott'
                        ),
                        MessageTemplateAction(
                            label='茂谷柑',
                            text='murcott'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"
    
def send_apr(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='四月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='香蕉',
                            text='banana'
                        ),
                        MessageTemplateAction(
                            label='芭樂',
                            text='guava'
                        ),
                        MessageTemplateAction(
                            label='奇異果',
                            text='kiwi'
                        )
                    ]
                ),
                CarouselColumn(
                    title='四月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        ),
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        ),
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"
        
def send_may(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='五月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='香蕉',
                            text='banana'
                        ),
                        MessageTemplateAction(
                            label='芭樂',
                            text='guava'
                        ),
                        MessageTemplateAction(
                            label='火龍果',
                            text='dragonfruit'
                        )
                    ]
                ),
                CarouselColumn(
                    title='五月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='百香果',
                            text='passionfruit'
                        ),
                        MessageTemplateAction(
                            label='芒果',
                            text='mango'
                        ),
                        MessageTemplateAction(
                            label='西瓜',
                            text='watermelon'
                        )
                    ]
                ),
                CarouselColumn(
                    title='五月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        ),
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        ),
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_jun(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='六月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='香蕉',
                            text='banana'
                        ),
                        MessageTemplateAction(
                            label='芭樂',
                            text='guava'
                        ),
                        MessageTemplateAction(
                            label='火龍果',
                            text='dragonfruit'
                        )
                    ]
                ),
                CarouselColumn(
                    title='六月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='百香果',
                            text='passionfruit'
                        ),
                        MessageTemplateAction(
                            label='芒果',
                            text='mango'
                        ),
                        MessageTemplateAction(
                            label='西瓜',
                            text='watermelon'
                        )
                    ]
                ),
                CarouselColumn(
                    title='六月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='鳳梨',
                            text='pineapple'
                        ),
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        ),
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_jul(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='七月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='香蕉',
                            text='banana'
                        ),
                        MessageTemplateAction(
                            label='芭樂',
                            text='guava'
                        ),
                        MessageTemplateAction(
                            label='火龍果',
                            text='dragonfruit'
                        )
                    ]
                ),
                CarouselColumn(
                    title='七月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='百香果',
                            text='passionfruit'
                        ),
                        MessageTemplateAction(
                            label='芒果',
                            text='mango'
                        ),
                        MessageTemplateAction(
                            label='鳳梨',
                            text='pineapple'
                        )
                    ]
                ),
                CarouselColumn(
                    title='七月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='釋迦',
                            text='sugarapple'
                        ),
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        ),
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_aug(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='八月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='香蕉',
                            text='banana'
                        ),
                        MessageTemplateAction(
                            label='芭樂',
                            text='guava'
                        ),
                        MessageTemplateAction(
                            label='火龍果',
                            text='dragonfruit'
                        )
                    ]
                ),
                CarouselColumn(
                    title='八月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='百香果',
                            text='passionfruit'
                        ),
                        MessageTemplateAction(
                            label='芒果',
                            text='mango'
                        ),
                        MessageTemplateAction(
                            label='鳳梨',
                            text='pineapple'
                        )
                    ]
                ),
                CarouselColumn(
                    title='八月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='釋迦',
                            text='sugarapple'
                        ),
                        MessageTemplateAction(
                            label='木瓜',
                            text='papaya'
                        ),
                        MessageTemplateAction(
                            label='柚子',
                            text='pomelo'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_sep(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='九月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='香蕉',
                            text='banana'
                        ),
                        MessageTemplateAction(
                            label='芭樂',
                            text='guava'
                        ),
                        MessageTemplateAction(
                            label='火龍果',
                            text='dragonfruit'
                        )
                    ]
                ),
                CarouselColumn(
                    title='九月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='百香果',
                            text='passionfruit'
                        ),
                        MessageTemplateAction(
                            label='釋迦',
                            text='sugarapple'
                        ),
                        MessageTemplateAction(
                            label='木瓜',
                            text='papaya'
                        )
                    ]
                ),
                CarouselColumn(
                    title='九月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='柚子',
                            text='pomelo'
                        ),
                        MessageTemplateAction(
                            label='奇異果',
                            text='kiwi'
                        ),
                        MessageTemplateAction(
                            label='奇異果',
                            text='kiwi'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_oct(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='十月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='香蕉',
                            text='banana'
                        ),
                        MessageTemplateAction(
                            label='芭樂',
                            text='guava'
                        ),
                        MessageTemplateAction(
                            label='火龍果',
                            text='dragonfruit'
                        )
                    ]
                ),
                CarouselColumn(
                    title='十月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='百香果',
                            text='passionfruit'
                        ),
                        MessageTemplateAction(
                            label='釋迦',
                            text='sugarapple'
                        ),
                        MessageTemplateAction(
                            label='木瓜',
                            text='papaya'
                        )
                    ]
                ),
                CarouselColumn(
                    title='十月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='柚子',
                            text='pomelo'
                        ),
                        MessageTemplateAction(
                            label='奇異果',
                            text='kiwi'
                        ),
                        MessageTemplateAction(
                            label='奇異果',
                            text='kiwi'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_nov(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='十一月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='香蕉',
                            text='banana'
                        ),
                        MessageTemplateAction(
                            label='芭樂',
                            text='guava'
                        ),
                        MessageTemplateAction(
                            label='火龍果',
                            text='dragonfruit'
                        )
                    ]
                ),
                CarouselColumn(
                    title='十一月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='釋迦',
                            text='sugarapple'
                        ),
                        MessageTemplateAction(
                            label='木瓜',
                            text='papaya'
                        ),
                        MessageTemplateAction(
                            label='奇異果',
                            text='kiwi'
                        )
                    ]
                ),
                CarouselColumn(
                    title='十一月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        ),
                        MessageTemplateAction(
                            label='茂谷柑',
                            text='murcott'
                        ),
                        MessageTemplateAction(
                            label='柳丁',
                            text='orange'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_dec(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='十二月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='香蕉',
                            text='banana'
                        ),
                        MessageTemplateAction(
                            label='芭樂',
                            text='guava'
                        ),
                        MessageTemplateAction(
                            label='火龍果',
                            text='dragonfruit'
                        )
                    ]
                ),
                CarouselColumn(
                    title='十二月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='釋迦',
                            text='sugarapple'
                        ),
                        MessageTemplateAction(
                            label='木瓜',
                            text='papaya'
                        ),
                        MessageTemplateAction(
                            label='奇異果',
                            text='kiwi'
                        )
                    ]
                ),
                CarouselColumn(
                    title='十二月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        ),
                        MessageTemplateAction(
                            label='茂谷柑',
                            text='murcott'
                        ),
                        MessageTemplateAction(
                            label='柳丁',
                            text='orange'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_jan(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    title='一月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='香蕉',
                            text='banana'
                        ),
                        MessageTemplateAction(
                            label='芭樂',
                            text='guava'
                        ),
                        MessageTemplateAction(
                            label='釋迦',
                            text='sugarapple'
                        )
                    ]
                ),
                CarouselColumn(
                    title='一月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='奇異果',
                            text='kiwi'
                        ),
                        MessageTemplateAction(
                            label='蓮霧',
                            text='waxapple'
                        ),
                        MessageTemplateAction(
                            label='茂谷柑',
                            text='murcott'
                        )
                    ]
                ),
                CarouselColumn(
                    title='一月水果',
                    text='選擇水果',
                    actions=[
                        MessageTemplateAction(
                            label='柳丁',
                            text='orange'
                        ),
                        MessageTemplateAction(
                            label='柳丁',
                            text='orange'
                        ),
                        MessageTemplateAction(
                            label='柳丁',
                            text='orange'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_fruit_info(reply_token, image_url, nutrition_url, pick_url, preserve_url):
    line_bot_api = LineBotApi(channel_access_token)
    buttons_template = TemplateSendMessage(
        alt_text='Buttons Template',
        template=ButtonsTemplate(
            title='水果資訊',
            text='點擊看更多!',
            thumbnail_image_url=image_url,
            actions=[
                URITemplateAction(
                    label='營養功效',
                    uri=nutrition_url
                ), URITemplateAction(
                    label='怎麼挑？',
                    uri=pick_url
                ), URITemplateAction(
                    label='保存方法',
                    uri=preserve_url
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, buttons_template)

    return "OK"
# def send_feb(reply_token, id):
#     line_bot_api = LineBotApi(channel_access_token)
#     buttons_template = TemplateSendMessage(
#         alt_text='Buttons Template',
#         template=ButtonsTemplate(
#             title='二月水果',
#             text='選擇水果',
#             actions=[
#                 MessageTemplateAction(
#                     label='香瓜',
#                     text='Muskmelon'
#                 ),
#                 MessageTemplateAction(
#                     label='香蕉',
#                     text='banana'
#                 ),
#                 MessageTemplateAction(
#                     label='芭樂',
#                     text='gava'
#                 )
#             ]
#         )
#     )
#     line_bot_api.reply_message(reply_token, buttons_template)

#     return "OK"
"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
