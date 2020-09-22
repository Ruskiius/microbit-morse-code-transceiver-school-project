radio.onReceivedNumber(function on_received_number(receivedNumber: number) {
    music.playTone(262, music.beat(BeatFraction.Quarter))
    basic.showString("RX")
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.playTone(698, music.beat(BeatFraction.Quarter))
    radio.sendString("TX")
    basic.showString("TX")
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    music.playTone(262, music.beat(BeatFraction.Quarter))
    basic.showString("RX")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    music.playTone(698, music.beat(BeatFraction.Whole))
    radio.sendNumber(1)
    basic.showString("TX")
})
radio.setGroup(1)
basic.forever(function on_forever() {
    basic.showLeds(`
        # # . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(2)
    basic.showLeds(`
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        `)
    basic.pause(1500)
})
