import cryptocompare  # pip3 install cryptocompare
from time import sleep
from pygame import mixer
import pyttsx3
from win10toast import ToastNotifier # pip install win10toast

toast = ToastNotifier()
mixer.init()
engine = pyttsx3.init()

# START constants
sleep_timer = 10

toast_duration = 5
toast_icon = "icon.ico"
toast_info = "mohseng.ir | info@mohseng.ir"
# END constants

coin = input("Enter coin symbol (Ex: TRX, BTC, EOX, XRP , ...) : ").upper()
now_price = cryptocompare.get_price(coin, currency='USD')[coin]["USD"]
print("Now", coin, "price is", now_price,"$")

thresh_down = float(input("Enter DOWN threshold: "))
thresh_up = float(input("Enter UP threshold: "))
threshold = float(input("Enter threshold: "))

while True:
    coin_price = cryptocompare.get_price(coin, currency='USD')[coin]["USD"]

    if coin_price < thresh_down:
        status = "Coin went low"
        print(status, coin_price)

        thresh_up -= threshold
        thresh_down -= threshold

        mixer.music.load('down.mp3')
        mixer.music.play()

        toast.show_toast(coin, status + " \n" + str(coin_price) + " \n" + toast_info,duration=toast_duration,icon_path=toast_icon)

        engine.say("coin is {}".format(coin_price))
        engine.runAndWait()

    elif coin_price > thresh_up:
        status = "Coin went high"
        print(status, coin_price)

        thresh_up += threshold
        thresh_down += threshold

        mixer.music.load('up.mp3')
        mixer.music.play()

        toast.show_toast(coin, status + " \n" + str(coin_price) + " \n" + toast_info,duration=toast_duration,icon_path=toast_icon)

        engine.say("coin is {}".format(coin_price))
        engine.runAndWait()

    else:
        print(thresh_down, "<", coin_price, "<", thresh_up)

    sleep(sleep_timer)