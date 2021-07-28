from pynput import keyboard

COMBINATIONS = [
    {keyboard.Key.alt_gr} #ALT GR
   
]

current = set()

x = True
def execute():
    global x
    x = False


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start()