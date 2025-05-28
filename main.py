import requests
import time

BOT_TOKEN = '7771771486:AAGTLRVH-lZKOnxBz7C6UItii09xahxgjdk'
CHAT_ID = '651539039'

def send_telegram_message(text):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    data = {'chat_id': CHAT_ID, 'text': text}
    try:
        response = requests.post(url, data=data)
        if response.status_code == 200:
            print("✅ پیام ارسال شد:", text)
        else:
            print("❌ خطا در ارسال:", response.text)
    except Exception as e:
        print("⛔ استثناء:", str(e))

def main_loop():
    send_telegram_message("✨ ربات OR HANISTAR 333 فعال شد 🪬")
    while True:
        current_time = time.strftime("%H:%M:%S")
        send_telegram_message(f"⏰ زمان فعلی: {current_time}")
        time.sleep(60)

if __name__ == '__main__':
    main_loop()
