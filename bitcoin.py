from bs4 import BeautifulSoup
import requests
import schedule

def bot_send_text(bot_message):
    bot_token = 'Mi_Token' #Ver el token en botfther
    bot_chatID = 'Mi ChatID'
    """     Para obtener este último tienes que ejecutar tu bot en Telegram, lo puedes hacer a través del link t.me/nombreDeTuBot que recibiste al crearlo o poniendo en el buscador el username de tu bot.
    Una vez lo abras, dale a /start. Luego en una nueva pestaña del navegador coloca:
    https://api.telegram.org/bot(yourtoken)/getUpdates
    Reemplazando (yourtoken) por tu token privado. Dale a enter y te saldrá algo como esto:
    {"ok":true,"result":[{"update_id":49xxxxxx,
    "message":{"message_id":2,"from":{"id":68xxxxxxx,"is_bot":false,"first_name":"Tony","last_name":"\ud83c\uddea\ud83c\udde8","username":"AnthonyManotoa","language_code":"en"},"chat":{"id":68xxxxxxx,"first_name":"Tony","last_name":"\ud83c\uddea\ud83c\udde8","username":"AnthonyManotoa","type":"private"},"date":1616777242,"text":"/start","entities":[{"offset":0,"length":6,"type":"bot_command"}]}}]}

    Si no te sale, vuelve a enviar /start a tu bot y luego recarga la página.
    Copia el número de “id” (68xxxxxxx), no lo confundas con “update_id” o “message_id”. Esto lo vas a utilizar para que te conectes con tu propio chat más adelante. """

    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)

    return response

def btc_scrapping():
    url=requests.get('https://awebanalysis.com/es/coin-details/bitcoin/')
    soup = BeautifulSoup(url.content, 'html.parser')
    result = soup.find('td', {'class': 'wbreak_word align-middle coin_price'})
    format_result = result.text

    return format_result

def report():
    btc_price = f'El precio de Bitcoin es de {btc_scrapping()}'
    bot_send_text(btc_price)

if __name__ == '__main__':
    #test_bot = bot_send_text('Hola, Telegram')
    #print(test_bot)
    #print(report())

    schedule.every().day.at("17:39").do(report)

    while True:
        schedule.run_pending()