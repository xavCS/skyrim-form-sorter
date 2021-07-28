from pynput import keyboard
#bind a listener to alt gr that breaks from a while loop that depends on x being True
COMBINATIONS = [
    {keyboard.Key.alt_gr} #ALT GR  
]

current = set()

x = True
def execute():
    global x
    x = False

#this probably isn't the most efficient way to go about it, but as of right now i'm not very good with this module
def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

listener = keyboard.Listener(on_press=on_press,on_release=on_release)
listener.start() #used this instead of context manager because with statement was blocking all other code from running.
