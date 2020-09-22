def on_received_number(receivedNumber):
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    basic.show_string("RX")
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    music.play_tone(698, music.beat(BeatFraction.QUARTER))
    radio.send_string("TX")
    basic.show_string("TX")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    music.play_tone(262, music.beat(BeatFraction.QUARTER))
    basic.show_string("RX")
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    music.play_tone(698, music.beat(BeatFraction.WHOLE))
    radio.send_number(1)
    basic.show_string("TX")
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)

def on_forever():
    basic.show_leds("""
        # # . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(2)
    basic.show_leds("""
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        . . . . .
        """)
    basic.pause(1500)
basic.forever(on_forever)
