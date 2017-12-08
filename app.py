import os, sys
from flask import Flask, request
from pymessenger import Bot

app = Flask(__name__)

PAGE_ACCESS_TOKEN = "EAAdYVJ5PjIMBAPUzBjaV6TPATCvJ7CGuylm0kQ1ILmEsZAcwvakZAzQawKDPiikNbZCenOdKCQ0PpulN36qRk3hw3ciKwAJ979loLFac9jjZBtLwuHAuMB3k4u8rh9x9Am7hhMlHQSdyW1TelwTePwlQ81L1TvmfWkogmQN9flYU80JqUkJp"

bot = Bot(PAGE_ACCESS_TOKEN)
'''
@app
It is a decorator. When decorated by @app.route('/') 
(which is a function), calling index() becomes the same as calling app.route('/')(index)().

https://stackoverflow.com/questions/35334958/flask-what-exactly-is-app
https://wiki.python.org/moin/PythonDecorators
'''
@app.route('/', methods=['GET'])
def verify():

    # Webhook verification
    # if request.args.get("hub.mod") == "subscribe" and request.args.get("hub.challenge"):
    if not request.args.get("hub.verify_token") == "hello":
        return "Verification token mismatch", 403
    return request.args["hub.challenge"], 200
    # return "Hello world", 200

@app.route('/', methods=['POST'])
def webhook():
    data=request.get_json()
    log(data)

    if data['object'] == 'page':
        for entry in data['entry']:
            for messaging_event in entry['messaging']:

                # IDs
                sender_id = messaging_event['sender']['id']
                recipient_id = messaging_event['recipient']['id']

                if messaging_event.get('message'):
                    if 'text' in messaging_event['message']:
                        messaging_text = messaging_event['message']['text']
                    else:
                        messaging_event = 'no_text'

                    #Echo
                    response = messaging_text

                    bot.send_text_message(sender_id, response)



    return "Ok", 200

def log(message):
    print(message)
    sys.stdout.flush()

if __name__ =="__main__":
    app.run(debug = True, port = 80)
