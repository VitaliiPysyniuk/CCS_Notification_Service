from flask import Flask, request, Response
import os

from services import send_message_in_telegram

app = Flask(__name__)
app.debug = os.environ.get('DEBUG')
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/send-message', methods=['POST'])
async def main():
    request_body = {
        'receiver': request.json['receiver'],
        'message_text': request.json['message_text']
    }
    response = await send_message_in_telegram(request_body)
    print(response)
    return response



