from pynput import mouse, keyboard
import pyautogui


def on_press(key):
    try:
        print('K ' + key.char)
    except AttributeError:
        print('S ' + str(key).replace('Key.', ''))


key_listener = keyboard.Listener(on_press=on_press)
key_listener.start()


def on_move(x, y):
    print('M ' + str(x) + ' ' + str(y))


def on_click(x, y, button, pressed):
    print(str(button).replace('Button.', '').upper()[0] + ' ' + str(x) + ' ' + str(y))


def on_scroll(x, y, dx, dy):
    if dy < 0:
        print('D' + str(abs(dy)))
    else:
        print('U' + str(dy))


# Collect events until released
with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
    listener.join()
