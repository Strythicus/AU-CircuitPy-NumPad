# SPDX-FileCopyrightText: 2021 Emma Humphries for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# MACROPAD Hotkeys example: Universal Numpad Modified by JKB

from adafruit_hid.keycode import Keycode # REQUIRED if using Keycode.* values

app = {                # REQUIRED dict, must be named 'app'
    'name' : 'Rainbow NumPad', # Application name
    'macros' : [       # List of button macros...
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x600000, '7', ['7']),
        (0x602000, '8', ['8']),
        (0x404000, '9', ['9']),
        # 2nd row ----------
        (0x602000, '4', ['4']),
        (0x404000, '5', ['5']),
        (0x006000, '6', ['6']),
        # 3rd row ----------
        (0x404000, '1', ['1']),
        (0x006000, '2', ['2']),
        (0x004040, '3', ['3']),
        # 4th row ----------
        (0x006000, '.', ['.']),
        (0x004040, '0', ['0']),
        (0x000060, 'Enter',  [Keycode.ENTER]),   # Enter key
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
