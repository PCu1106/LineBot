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
    states=["user", "start", "feb", "mar", "apr","may","jun","jul","aug","sep","oct","nov","dec","jan","banana"],
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
        # {"trigger": "go_back", "source": ["start", "feb", "mar", "apr","may","jun","jul","aug","sep","oct","nov","dec","jan","banana"], "dest": "user"},
        {"trigger": "go_back", "source": ["banana"], "dest": "user"},
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
                                   ' https://ccdd-36-237-89-62.ngrok.io/show-fsm')

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
