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

# 兩人同時使用bot的問題

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
        "Hello,\n" 
        "歡迎使用電影評分查詢\n"
        "目前資料庫建置中\n"
        "請耐心等候\n\n"
        "請輸入你要查詢的電影"
    )

    line_bot_api.reply_message(event.reply_token, follow_text_send_message)
    return

    # 輸入電影名稱

@handler.add(MessageEvent, message=TextMessage)
def handle_ranking_system(event):    
    # 想查詢的系統

    buttons_template_message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i1.wp.com/popbee.com/image/2020/10/tenet-things-you-need-to-konw-easter-eggs-fun-fact-teaser.jpg',
            title='請選擇一個電影評分系統',
            text='IMDb, Rotten Tomatoes, PTT, \n或是全部評分',
            actions=[
                PostbackAction(
                    label='IMDb',
                    display_text='我想看看IMDb',
                    data='IMDb,'
                ),
                PostbackAction(
                    label='Rotten Tomatoes',
                    display_text='我想看看爛番茄',
                    data='Tomatoes,'
                ),
                PostbackAction(
                    label='PTT',
                    display_text='我想看看電影版',
                    data='PTT,'
                ),
                PostbackAction(
                    label='全部評分',
                    display_text='我想看所有評分',
                    data='ALL,'
                )
            ]
        )
    )

    line_bot_api.reply_message(event.reply_token, buttons_template_message)
    return

# 詢問經驗

# 圖文選單


if __name__ == "__main__":
    app.run()

# https://howimuchisthis.herokuapp.com
# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=os.environ['PORT'])