from flask import Response
from telethon import TelegramClient
import os
import json
from datetime import datetime

API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
OWNER_CREDS = os.environ.get('OWNER_CREDS')


async def send_message_in_telegram(message_detail):
    client = TelegramClient('current', API_ID, API_HASH)
    await client.connect()
    if not await client.is_user_authorized():
        await client.send_code_request(OWNER_CREDS)
        await client.sign_in(OWNER_CREDS, input("Enter the code: "))

    silent = resolve_time()
    try:
        sent_message = await client.send_message(message_detail['receiver'], message_detail['message_text'],
                                                 silent=silent)
    except ValueError as error:
        payload = {'detail': str(error)}
        response = Response(response=json.dumps(payload), status=404, mimetype='application/json')
    else:
        payload = {
            'message_id': sent_message.id,
            'sending_time': str(sent_message.date)
        }
        response = Response(response=json.dumps(payload), status=200, mimetype='application/json')
    finally:
        await client.disconnect()

    return response


def resolve_time():
    current_hour = int(datetime.now().hour)
    if 8 <= current_hour <= 22:
        return False
    return True
