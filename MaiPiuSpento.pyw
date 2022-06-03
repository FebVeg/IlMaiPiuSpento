from pynput.keyboard import Key, Controller, Listener
from pynput import keyboard, mouse
from time import sleep


global var
var = 0


keyboard_click = Controller()
soglia         = 120
tempo          = soglia


def click():
    keyboard_click.press(Key.shift)
    sleep(0.1)
    keyboard_click.release(Key.shift)


def on_press(key):
    global var
    var = 1
    print(f"Fermi tutti! Qualcuno mi ha toccato :D")


def on_titilling(ev):
    global var
    var = 1


with keyboard.Listener(on_press=on_press) as listener:
    print("Allora io vado eh...")
    while True:
        with mouse.Events() as events:
            event = events.get(1.0)
            if event is None:
                print("Non mi sta titillando nessuno")
            else:
                print("Mi si strusciano :D")
                var = 1
                sleep(1)

        if var == 0:
            sleep(1)
            tempo -= 1
            print(f"Nada - T:{tempo} V:{var}")
        else:
            print("AHI!!!")
            tempo = soglia
            var = 0
        
        if tempo == 0:
            print("Beccati questa! Farabrutto!")
            click()
            tempo = soglia

listener.join()
