let MOISTURE = 0
basic.forever(function () {
    MOISTURE = pins.analogReadPin(AnalogPin.P1)
    if (MOISTURE > 1010) {
        basic.showIcon(IconNames.Surprised)
    } else if (MOISTURE > 900) {
        basic.showIcon(IconNames.Happy)
    } else {
        basic.showIcon(IconNames.Sad)
        basic.showString("WATER NOW")
        music.playMelody("C D E D C - - - ", 120)
    }
})
