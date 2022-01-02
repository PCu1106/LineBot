import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from fsm import TocMachine
from utils import send_text_message,send_image_message

load_dotenv()


machine = TocMachine(
    states=["user", "start", "feb", "mar", "apr","may","jun","jul","aug","sep","oct","nov","dec","jan","banana","guava","dragonfruit","passionfruit","mango","watermelon","pineapple","sugarapple","papaya","pomelo","kiwi","waxapple","murcott","orange"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "start",
            "conditions": "is_going_to_start",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "feb",
            "conditions": "is_going_to_feb",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "mar",
            "conditions": "is_going_to_mar",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "apr",
            "conditions": "is_going_to_apr",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "may",
            "conditions": "is_going_to_may",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "jun",
            "conditions": "is_going_to_jun",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "jul",
            "conditions": "is_going_to_jul",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "aug",
            "conditions": "is_going_to_aug",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "sep",
            "conditions": "is_going_to_sep",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "oct",
            "conditions": "is_going_to_oct",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "nov",
            "conditions": "is_going_to_nov",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "dec",
            "conditions": "is_going_to_dec",
        },
        {
            "trigger": "advance",
            "source": "start",
            "dest": "jan",
            "conditions": "is_going_to_jan",
        },
        {
            "trigger": "advance",
            "source": [ "feb", "mar", "apr","may","jun","jul","aug","sep","oct","nov","dec","jan"],
            "dest": "banana",
            "conditions": "is_going_to_banana",
        },
        {
            "trigger": "advance",
            "source": [ "feb", "mar", "apr","may","jun","jul","aug","sep","oct","nov","dec","jan"],
            "dest": "guava",
            "conditions": "is_going_to_guava",
        },
        {
            "trigger": "advance",
            "source": [ "may","jun","jul","aug","sep","oct","nov","dec"],
            "dest": "dragonfruit",
            "conditions": "is_going_to_dragonfruit",
        },
        {
            "trigger": "advance",
            "source": [ "may","jun","jul","aug","sep","oct"],
            "dest": "passionfruit",
            "conditions": "is_going_to_passionfruit",
        },
        {
            "trigger": "advance",
            "source": [ "may","jun","jul","aug"],
            "dest": "mango",
            "conditions": "is_going_to_mango",
        },
        {
            "trigger": "advance",
            "source": [ "may","jun"],
            "dest": "watermelon",
            "conditions": "is_going_to_watermelon",
        },
        {
            "trigger": "advance",
            "source": [ "jun","jul","aug"],
            "dest": "pineapple",
            "conditions": "is_going_to_pineapple",
        },
        {
            "trigger": "advance",
            "source": ["feb","jul","aug","sep","oct","nov","dec","jan"],
            "dest": "sugarapple",
            "conditions": "is_going_to_sugarapple",
        },
        {
            "trigger": "advance",
            "source": ["aug","sep","oct","nov","dec"],
            "dest": "papaya",
            "conditions": "is_going_to_papaya",
        },
        {
            "trigger": "advance",
            "source": ["aug","sep","oct"],
            "dest": "pomelo",
            "conditions": "is_going_to_pomelo",
        },
        {
            "trigger": "advance",
            "source": ["feb", "mar", "apr","sep","oct","nov","dec","jan"],
            "dest": "kiwi",
            "conditions": "is_going_to_kiwi",
        },
        {
            "trigger": "advance",
            "source": ["feb", "mar", "apr","may","jun","jul","nov","dec","jan"],
            "dest": "waxapple",
            "conditions": "is_going_to_waxapple",
        },
        {
            "trigger": "advance",
            "source": ["feb", "mar","nov","dec","jan"],
            "dest": "murcott",
            "conditions": "is_going_to_murcott",
        },
        {
            "trigger": "advance",
            "source": ["nov","dec","jan"],
            "dest": "orange",
            "conditions": "is_going_to_orange",
        },
        {"trigger": "go_back", "source": ["banana","guava","dragonfruit","passionfruit","mango","watermelon","pineapple","sugarapple","papaya","pomelo","kiwi","waxapple","murcott","orange"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)

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
        if response == False:
            if event.message.text == 'fsm':
                send_image_message(event.reply_token,
                                   ' https://drfruit.herokuapp.com/show-fsm')

            else:
                send_text_message(event.reply_token,
                                  "輸入'start'來呼叫水果博士!")

    return "OK"


@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")


if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
