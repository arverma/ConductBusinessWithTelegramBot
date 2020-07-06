import requests
import json


class TelegramChatbot:
    def __init__(self):
        self.TOKEN = "********************"
        self.ADMIN_CHAT_ID = 12345667
        self.DEMO_MATERIAL_PUBLIC_LINK = "http://google_drive_link"
        self.MATERIAL_COST = 100
        self.UPI_QR_FILE_NAME = "upi.png"
        self.UPI_ID = "@paytm_merchant_or_any"
        self.BASE = "https://api.telegram.org/bot{}/".format(self.TOKEN)

    def get_updates(self, offset=None):
        url = self.BASE + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id, reply_markup=None):
        url = self.BASE + "sendMessage?chat_id={}&text={}".format(chat_id, msg)
        if reply_markup:
            url += "&reply_markup={}".format(reply_markup)
        if msg is not None:
            requests.get(url)

    def send_image(self, chat_id, file_id):
        url = self.BASE + 'sendPhoto?chat_id={}&photo={}'.format(chat_id, file_id)
        if file_id is not None:
            requests.get(url)

    def send_image_from_local(self, chat_id):
        url = self.BASE + "sendPhoto?chat_id={}".format(chat_id)
        files = {'photo': open(self.UPI_QR_FILE_NAME, 'rb')}
        requests.post(url, files=files)

