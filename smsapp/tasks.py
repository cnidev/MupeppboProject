import os
import requests
from celery import shared_task
from django.core.cache import cache

from dotenv import load_dotenv

load_dotenv()

def get_sms_api_key():
    """Récupère la clé API SMS depuis l'API Orange"""

    headers = {
        'Authorization': f"{os.getenv('AUTH_HEADER')}",
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }
    data = { 'grant_type': 'client_credentials' }

    response = requests.post('https://api.orange.com/oauth/v3/token', headers=headers, data=data)

    return response.json().get('access_token')


@shared_task()
def send_sms(phone_number, message_content):
    """Envoie un SMS à un numéro de téléphone donné"""

    api_key = cache.get('sms_api_key')
    if not api_key:
        api_key = get_sms_api_key()
        cache.set('sms_api_key', api_key, timeout=3600)

    headers = {
        "content-type": "application/json",
    }

    data = {
        "outboundSMSMessageRequest": {
            "address": f"tel:+225{phone_number}",
            "senderAddress": f"tel:+225{os.getenv('SENDER_NUMBER')}",
            "senderName": f"{os.getenv('SENDER_NAME')}",
            "outboundSMSTextMessage": {
                "message": message_content
            }
        }
    }

    url = f"https://api.orange.com/smsmessaging/v1/outbound/tel%3A%2B225{os.getenv('SENDER_NUMBER')}/requests"

    response = requests.post(url, json=data, headers=headers)