def on_button_pressed_a():
    basic.show_icon(IconNames.HEART)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_shake():
    for _1 in range(11):
        basic.show_number(_1)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    if Gread >= 90:
        basic.show_string("excellent")
    elif Gread >= 50:
        basic.show_string("Pass")
    else:
        basic.show_string("Fail")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global X
    X += 1
    basic.show_number(X)
input.on_button_pressed(Button.B, on_button_pressed_b)

X = 0
Gread = 0
Gread = 50
basic.show_string("Reham Masoud")