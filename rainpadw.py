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
        (0x600000, 'Seven', ['7']),
        (0x602000, 'Eight', ['8']),
        (0x404000, 'Nine', ['9']),
        # 2nd row ----------
        (0x602000, 'Four', ['4']),
        (0x404000, 'Five', ['5']),
        (0x006000, 'Six', ['6']),
        # 3rd row ----------
        (0x404000, 'One', ['1']),
        (0x006000, 'Two', ['2']),
        (0x004040, 'Three', ['3']),
        # 4th row ----------
        (0x006000, 'Dot', ['.']),
        (0x004040, 'Zero', ['0']),
        (0x000060, 'Enter',  [Keycode.ENTER]),   # Enter key
        # Encoder button ---
        (0x000000, '', [Keycode.BACKSPACE])
    ]
}
