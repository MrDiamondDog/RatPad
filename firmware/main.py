print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP27, board.GP28, board.GP29,)
keyboard.row_pins = (board.GP1, board.GP2, board.GP3, board.GP4,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.extensions.append(MediaKeys())

# Not final, just basic until I figure out what I want
keyboard.keymap = [
    [
        KC.MEDIA_PREV_TRACK, KC.MEDIA_PLAY_PAUSE, KC.MEDIA_NEXT_TRACK,
        KC.KP_1, KC.KP_2, KC.KP_3,
        KC.KP_4, KC.KP_5, KC.KP_6,
        KC.KP_7, KC.KP_8, KC.KP_9,
    ]
]

if __name__ == '__main__':
    keyboard.go()