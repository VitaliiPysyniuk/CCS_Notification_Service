from flask import Flask, request
import os

from services import send_message_in_telegram
from middlewares import CustomSecurityMiddleware

app = Flask(__name__)
app.debug = os.environ.get('DEBUG')
app.secret_key = os.environ.get('SECRET_KEY')

app.wsgi_app = CustomSecurityMiddleware(app.wsgi_app)


@app.route('/send-message', methods=['POST'])
async def main():
    request_body = {
        'receiver': request.json['receiver'],
        'message_text': request.json['message_text']
    }
    response = await send_message_in_telegram(request_body)
    return response
