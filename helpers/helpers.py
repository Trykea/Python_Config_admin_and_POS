import requests
def sendnotify(msg):
    bot_token = "7007744504:AAGuWNHDDXiIYjmypXovRU32WwLIa4m85Kk"
    chat_id = "@st89_message"
    html = msg

    html = requests.utils.quote(html)
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={html}&parse_mode=HTML"
    res = requests.get(url)
    return res