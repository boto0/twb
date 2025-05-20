from flask import Flask, request
import requests
import os
from datetime import datetime

app = Flask(__name__)

BOT_TOKEN = os.environ.get("8182824052AAHKbzd-9bmKTmiJ7CiwI16HW5lCTUJYuzA")
CHAT_ID = os.environ.get("1002516895861")
SECRET_KEY = os.environ.get("SECRET_KEY")

@app.route("/")
def home():
    return "Webhook is running"

@app.route("/webhook/<key>", methods=["POST"])
def webhook(key):
    if key != SECRET_KEY:
        return "Unauthorized", 403

    data = request.json
    message = data.get("message", "⚠️ Алерт без текста")

    now = datetime.now().strftime("%d-%b-%Y %H:%M:%S")
    text = f"{message}\n{now}"

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "HTML"
    }
    r = requests.post(url, json=payload)

    return "OK", 200
