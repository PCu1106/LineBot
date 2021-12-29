import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from fsm import TocMachine
from utils import send_text_message
#####################################################################################
from utils import send_image_message
#####################################################################################
load_dotenv()


# machine = TocMachine(
#     states=["user", "state1", "state2"],
#     transitions=[
#         {
#             "trigger": "advance",
#             "source": "user",
#             "dest": "state1",
#             "conditions": "is_going_to_state1",
#         },
#         {
#             "trigger": "advance",
#             "source": "user",
#             "dest": "state2",
#             "conditions": "is_going_to_state2",
#         },
#         {"trigger": "go_back", "source": ["state1", "state2"], "dest": "user"},
#     ],
#     initial="user",
#     auto_transitions=False,
#     show_conditions=True,
# )

########################################################################################################
machine = TocMachine(
    states=["user", "start", "rice", "donburi", "tonkatsu", "teishoku", "sushi", "ramen",
            "japanese", "tainan", "tainan_restaurant1", "tainan_restaurant2", "tainan_restaurant3", "thai", "korean", "hotpot",  "hotpot_restaurant1",  "hotpot_restaurant2", "diner", "diner_restaurant1", "diner_restaurant2", "donburi_restaurant1", "donburi_restaurant2", "donburi_restaurant3", "tonkatsu_restaurant1", "tonkatsu_restaurant2", "tonkatsu_restaurant3", "teishoku_restaurant1", "teishoku_restaurant2", "teishoku_restaurant3", "sushi_restaurant1", "sushi_restaurant2", "sushi_restaurant3", "ramen_restaurant1", "ramen_restaurant2", "ramen_restaurant3", "thai_restaurant1", "thai_restaurant2",  "thai_restaurant3", "korean_restaurant1", "korean_restaurant2", "korean_restaurant3"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "start",
            "conditions": "is_going_to_start",
        },
        {
            "trigger": "advance",
            "source": "japanese",
            "dest": "rice",
            "conditions": "is_going_to_rice",
        },
        {
            "trigger": "advance",
            "source": "japanese",
            "dest": "sushi",
            "conditions": "is_going_to_sushi",
        },
        {
            "trigger": "advance",
            "source": "japanese",
            "dest": "ramen",
            "conditions": "is_going_to_ramen",
        },
        {
            "trigger": "advance",
            "source": "rice",
            "dest": "donburi",
            "conditions": "is_going_to_donburi",
        },
        {
            "trigger": "advance",
            "source": "donburi",
            "dest": "donburi_restaurant1",
            "conditions": "is_going_to_donburi_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "donburi",
            "dest": "donburi_restaurant2",
            "conditions": "is_going_to_donburi_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "donburi",
            "dest": "donburi_restaurant3",
            "conditions": "is_going_to_donburi_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "rice",
            "dest": "tonkatsu",
            "conditions": "is_going_to_tonkatsu",
        },
        {
            "trigger": "advance",
            "source": "tonkatsu",
            "dest": "tonkatsu_restaurant1",
            "conditions": "is_going_to_tonkatsu_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "tonkatsu",
            "dest": "tonkatsu_restaurant2",
            "conditions": "is_going_to_tonkatsu_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "tonkatsu",
            "dest": "tonkatsu_restaurant3",
            "conditions": "is_going_to_tonkatsu_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "rice",
            "dest": "teishoku",
            "conditions": "is_going_to_teishoku",
        },
        {
            "trigger": "advance",
            "source": "teishoku",
            "dest": "teishoku_restaurant1",
            "conditions": "is_going_to_teishoku_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "teishoku",
            "dest": "teishoku_restaurant2",
            "conditions": "is_going_to_teishoku_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "teishoku",
            "dest": "teishoku_restaurant3",
            "conditions": "is_going_to_teishoku_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "sushi",
            "dest": "sushi_restaurant1",
            "conditions": "is_going_to_sushi_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "sushi",
            "dest": "sushi_restaurant2",
            "conditions": "is_going_to_sushi_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "sushi",
            "dest": "sushi_restaurant3",
            "conditions": "is_going_to_sushi_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "ramen",
            "dest": "ramen_restaurant1",
            "conditions": "is_going_to_ramen_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "ramen",
            "dest": "ramen_restaurant2",
            "conditions": "is_going_to_ramen_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "ramen",
            "dest": "ramen_restaurant3",
            "conditions": "is_going_to_ramen_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "japanese",
            "conditions": "is_going_to_japanese",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "thai",
            "conditions": "is_going_to_thai",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "korean",
            "conditions": "is_going_to_korean",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "diner",
            "conditions": "is_going_to_diner",
        },

        {
            "trigger": "advance",
            "source": "diner",
            "dest": "diner_restaurant1",
            "conditions": "is_going_to_diner_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "diner",
            "dest": "diner_restaurant2",
            "conditions": "is_going_to_diner_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "tainan",
            "conditions": "is_going_to_tainan",
        },
        {
            "trigger": "advance",
            "source": "tainan",
            "dest": "tainan_restaurant1",
            "conditions": "is_going_to_tainan_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "tainan",
            "dest": "tainan_restaurant2",
            "conditions": "is_going_to_tainan_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "tainan",
            "dest": "tainan_restaurant3",
            "conditions": "is_going_to_tainan_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "hotpot",
            "conditions": "is_going_to_hotpot",
        },
        {
            "trigger": "advance",
            "source": "hotpot",
            "dest": "hotpot_restaurant1",
            "conditions": "is_going_to_hotpot_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "hotpot",
            "dest": "hotpot_restaurant2",
            "conditions": "is_going_to_hotpot_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "thai",
            "dest": "thai_restaurant1",
            "conditions": "is_going_to_thai_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "thai",
            "dest": "thai_restaurant2",
            "conditions": "is_going_to_thai_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "thai",
            "dest": "thai_restaurant3",
            "conditions": "is_going_to_thai_restaurant3",
        },
        {
            "trigger": "advance",
            "source": "korean",
            "dest": "korean_restaurant1",
            "conditions": "is_going_to_korean_restaurant1",
        },
        {
            "trigger": "advance",
            "source": "korean",
            "dest": "korean_restaurant2",
            "conditions": "is_going_to_korean_restaurant2",
        },
        {
            "trigger": "advance",
            "source": "korean",
            "dest": "korean_restaurant3",
            "conditions": "is_going_to_korean_restaurant3",
        },
        {"trigger": "go_back", "source": [
            "start", "rice", "ramen", "donburi", "tainan", "tainan_restaurant1", "tainan_restaurant2", "tainan_restaurant3", "tonkatsu", "teishoku", "sushi", "thai", "japanese", "korean", "hotpot",  "hotpot_restaurant1",  "hotpot_restaurant2", "diner", "diner_restaurant1", "diner_restaurant2", "donburi_restaurant1", "donburi_restaurant2", "donburi_restaurant3", "tonkatsu_restaurant1", "tonkatsu_restaurant2", "tonkatsu_restaurant3", "teishoku_restaurant1", "teishoku_restaurant2", "teishoku_restaurant3", "sushi_restaurant1", "sushi_restaurant2", "sushi_restaurant3", "ramen_restaurant1", "ramen_restaurant2", "ramen_restaurant3", "thai_restaurant1", "thai_restaurant2", "thai_restaurant3", "korean_restaurant1", "korean_restaurant2", "korean_restaurant3"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)
########################################################################################################

app = Flask(__name__, static_url_path="")


# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue

        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=event.message.text)
        )

    return "OK"


@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\nFSM STATE: {machine.state}")
        print(f"REQUEST BODY: \n{body}")
        response = machine.advance(event)
        # if response == False:
        #     send_text_message(event.reply_token, "多吃水果有益身體健康")
########################################################################################################
        if response == False:
            if event.message.text == 'fsm':
                send_image_message(event.reply_token,
                                   ' https://f27e-36-237-163-215.ngrok.io/show-fsm')

            else:
                send_text_message(event.reply_token,
                                  "不知道要吃什麼?輸入'start'來尋找成大周邊美食!")
########################################################################################################
    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
