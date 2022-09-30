def on_button_pressed_a():
    global worp, totaal
    worp = randint(1, 6)
    basic.show_number(worp)
    totaal += worp
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_number(totaal)
input.on_button_pressed(Button.B, on_button_pressed_b)

worp = 0
totaal = 0
basic.show_icon(IconNames.YES)
totaal = 0