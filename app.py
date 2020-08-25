from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, TemplateSendMessage, ConfirmTemplate,
    MessageAction, URIAction, ButtonsTemplate, PostbackAction, Postback, PostbackEvent,
    QuickReply, QuickReplyButton, ImageSendMessage
)
import json
import csv
import os

app = Flask(__name__)

line_bot_api = LineBotApi(
    'nbE0Yqi3KGYDpWH579IgAtS1ggxub+PUUgy0tUvNlkKAfIoRdo4D2GOiaPOQgqA6wr47BQdZ/6S4C'
    '/uhLmphZ2EpCs7xHhRwVC2kzpmdwVIyAnWRxdxEw3JKJvl1uY64mLntrp2GqPwUJccqeEc4owdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('784899c6df4a550a6b1d11f2fb5ad363')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


# 興趣變數暫存

interest = ""
_id = ""
# todo 兩人同時使用bot的問題

# 歡迎訊息


@handler.add(FollowEvent)
def handle_follow(event):
    global _id
    user_profile = line_bot_api.get_profile(event.source.user_id)
    with open("namelist.txt", "a") as myfile:
        myfile.write(
            json.dumps(
                vars(user_profile)
            )
        )
        _id = user_profile.user_id
        myfile.write("\r")

    follow_text_send_message = TextSendMessage(
        "Hello，\n"
        "我是「食米不知米價」機器人，\n"
        "對你生活周遭的食衣住行開銷，\n"
        "你到底了解了多少呢？\n"
        "\n"
        "先試試看你對甚麼領域有興趣吧！"
    )

    # 詢問喜好

    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://c0.wallpaperflare.com/preview/124/695/733/doors-choices-choose-open.jpg',
            title='我想猜這個',
            text='選一個有興趣的領域吧！',
            actions=[
                PostbackAction(
                    label='3c (iPhone)',
                    display_text='我想猜猜iPhone的價格',
                    data='iphone,'
                ),
                PostbackAction(
                    label='電玩 (Switch)',
                    display_text='我想猜猜看Switch的價格',
                    data='switch,'
                ),
                # PostbackAction(
                #     label='甜點',
                #     display_text='我想猜猜甜點價位',
                #     data='"theme":3,'
                # )
            ]
        )
    )

    line_bot_api.reply_message(event.reply_token, [follow_text_send_message,
                                                   buttons_template_message])
    return

# 詢問經驗


@handler.add(PostbackEvent)
def postback_data(event):
    global interest
    if event.postback.data == 'iphone,':
        interest = interest + event.postback.data
        confirm_template_message = TemplateSendMessage(
            alt_text='你有用過iPhone嗎？',
            template=ConfirmTemplate(
                text='你有用過或正在使用iPhone嗎？',
                actions=[
                    PostbackAction(
                        label='有',
                        display_text='我有用過iPhone',
                        data='have,'
                    ),
                    PostbackAction(
                        label='沒有',
                        display_text='我沒有用過iPhone',
                        data='not_have,'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, confirm_template_message)

    elif event.postback.data == 'switch,':
        interest = interest + event.postback.data
        confirm_template_message = TemplateSendMessage(
            alt_text='你有用過Switch嗎？',
            template=ConfirmTemplate(
                text='你現在有自己的Switch嗎？',
                actions=[
                    PostbackAction(
                        label='有',
                        display_text='我有Switch',
                        data='have,'
                    ),
                    PostbackAction(
                        label='沒有',
                        display_text='我沒有Switch',
                        data='not_have,'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, confirm_template_message)

    elif interest == 'iphone,':
        interest = interest + event.postback.data
        price_asking = TextSendMessage("現在請你猜猜看現在一台\n"
                                       "iPhone 11 Pro 64G\n"
                                       "售價大概多少錢呢？")
        line_bot_api.reply_message(event.reply_token, price_asking)

    elif interest == 'switch,':
        interest = interest + event.postback.data
        price_asking = TextSendMessage("現在猜猜看現在一台\n"
                                       "Switch紅藍款 (主機only)\n"
                                       "售價大概多少錢呢？")
        line_bot_api.reply_message(event.reply_token, price_asking)
    return interest


# 問題2 購買意願

# 估計價錢、回傳高估or低估 要用postback

@handler.add(MessageEvent, message=TextMessage)
def handle_price_message(event):
    global interest
    try:
        if int(event.message.text):
            a = int(event.message.text)
            if interest in ['iphone,not_have,', 'iphone,have,']:
                interest = interest + event.message.text
                if a > 35900 * 1.05:
                    result = "你高估囉！官方價格目前是35900元"
                elif a < 35900 * 0.95:
                    result = "你低估囉！官方價格目前是35900元"
                else:
                    result = "猜得很準喔！官方價格目前是35900元"
                reply_message = TextSendMessage("你猜的價格為" + event.message.text + "元\n" + result)

            elif interest in ['switch,not_have,', 'switch,have,']:
                interest = interest + event.message.text
                if a > 9780 * 1.05:
                    result = "你高估囉！官方價格目前是9780元"
                elif a < 9780 * 0.95:
                    result = "你低估囉！官方價格目前是9780元"
                else:
                    result = "猜得很準喔！官方價格目前是9780元"
                reply_message = TextSendMessage("你猜的價格為" + event.message.text + "元\n" + result)

            text_quickreply1 = QuickReplyButton(action=MessageAction(label="正確", text="就猜這個"))
            text_quickreply2 = QuickReplyButton(action=MessageAction(label="錯誤", text="再玩一次"))
            quick_reply_array = QuickReply(items=[text_quickreply1, text_quickreply2])

            reply_text_message = TextSendMessage(reply_message.text, quick_reply=quick_reply_array)
            line_bot_api.reply_message(event.reply_token, reply_text_message)
            with open("guesslist.csv", "a") as csvfile:
                writer = csv.writer(csvfile)
                li = interest.split(",")
                writer.writerow(li)

    except:
        if event.message.text == "就猜這個":
            static_chart = ImageSendMessage(
                original_content_url="https://images.plurk.com/29raxzfw1iC52tLqlPTVz1.jpg",
                preview_image_url="https://images.plurk.com/2nA3V4zBaRMtPicEvrK4pC.jpg"
            )
            # text_quickreply1 = QuickReplyButton(action=MessageAction(label="猜猜別的", text="再玩一次"))
            # text_quickreply2 = QuickReplyButton(action=MessageAction(label="不想猜了", text="我不玩了"))
            # quick_reply_array = QuickReply(items=[text_quickreply1, text_quickreply2])
            # test_reply = TextSendMessage("要猜猜看別的嗎？")
            # reply_text_message = TextSendMessage(test_reply, quick_reply=quick_reply_array)
            line_bot_api.reply_message(event.reply_token, [static_chart])
        elif event.message.text == "再玩一次":
            buttons_template_message = TemplateSendMessage(
                alt_text='Buttons template',
                template=ButtonsTemplate(
                    thumbnail_image_url='https://c0.wallpaperflare.com/preview/124/695/733/doors-choices-choose-open.jpg',
                    title='我想猜這個',
                    text='選一個有興趣的領域吧！',
                    actions=[
                        PostbackAction(
                            label='3c (iPhone)',
                            display_text='我想猜猜iPhone的價格',
                            data='iphone,'
                        ),
                        PostbackAction(
                            label='電玩 (Switch)',
                            display_text='我想猜猜看Switch的價格',
                            data='switch,'
                        ),
                        # PostbackAction(
                        #     label='甜點',
                        #     display_text='我想猜猜甜點價位',
                        #     data='"theme":3,'
                        # )
                    ]
                )
            )
            line_bot_api.reply_message(event.reply_token, buttons_template_message)
    interest = ""
    return interest


# TODO 圖文選單


if __name__ == "__main__":
    app.run()

# https://howimuchisthis.herokuapp.com
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=os.environ['PORT'])