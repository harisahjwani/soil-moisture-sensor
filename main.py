MOISTURE = 0

def on_forever():
    global MOISTURE
    MOISTURE = pins.analog_read_pin(AnalogPin.P1)
    if MOISTURE > 1010:
        basic.show_icon(IconNames.SURPRISED)
    elif MOISTURE > 900:
        basic.show_icon(IconNames.HAPPY)
    else:
        basic.show_icon(IconNames.SAD)
        basic.show_string("WATER NOW")
        music.play_melody("C D E D C - - - ", 120)
basic.forever(on_forever)
