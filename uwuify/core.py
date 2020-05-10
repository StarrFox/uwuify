#  Copyright (c) 2020 StarrFox
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.

import re
from enum import IntFlag
from typing import Union


class UwuifyFlag(IntFlag):
    SMILEY = 1
    YU = 2


# from https://cutekaomoji.com/characters/uwu/
SMILEYS = [
    "(ᵘʷᵘ)",
    "(ᵘﻌᵘ)",
    "(◡ ω ◡)",
    "(◡ ꒳ ◡)",
    "(◡ w ◡)",
    "(◡ ሠ ◡)",
    "(˘ω˘)",
    "(⑅˘꒳˘)",
    "(˘ᵕ˘)",
    "(˘ሠ˘)",
    "(˘³˘)",
    "(˘ε˘)",
    "(´˘`)",
    "(´꒳`)",
    "(˘˘˘)",
    "( ᴜ ω ᴜ )",
    "( ´ω` )۶",
    "(„ᵕᴗᵕ„)",
    "(ㅅꈍ ˘ ꈍ)",
    "(⑅˘꒳˘)",
    "( ｡ᵘ ᵕ ᵘ ｡)",
    "( ᵘ ꒳ ᵘ ✼)",
    "( ˘ᴗ˘ )",
    "(ᵕᴗ ᵕ⁎)",
    "*:･ﾟ✧(ꈍᴗꈍ)✧･ﾟ:*",
    "*˚*(ꈍ ω ꈍ).₊̣̇.",
    "(。U ω U。)",
    "(U ᵕ U❁)",
    "(U ﹏ U)",
    "(◦ᵕ ˘ ᵕ◦)",
    "ღ(U꒳Uღ)",
    "♥(。U ω U。)",
    "– ̗̀ (ᵕ꒳ᵕ) ̖́-",
    "( ͡U ω ͡U )",
    "( ͡o ᵕ ͡o )",
    "( ͡o ꒳ ͡o )",
    "( ˊ.ᴗˋ )",
    "(灬´ᴗ`灬)",
    "uwu",
    "owo",
]

UWU = str.maketrans({"r": "w", "l": "w", "R": "W", "L": "W"})

YU = str.maketrans({"u": "yu", "U": "yU"})

ER_REPLACE = re.compile(r"(\b\w{2,})er\b", re.IGNORECASE)


def _do_yu(entry: str) -> str:
    final = []
    for word in entry.split(" "):
        if word:
            final.append(word[0] + word[1:].translate(YU))
        else:
            final.append(" ")
    return " ".join(final)


def _do_uwu(entry: str) -> str:
    regexed = ER_REPLACE.sub(r"\g<1>a", entry)
    translated = regexed.translate(UWU)
    return translated


def _do_smily(entry: str) -> str:
    if not isinstance(entry, list):
        entry = entry.split(" ")

    import random

    final = []
    for word in entry:
        if word.endswith((".", "?", "!")):
            final.append(word + " " + random.choice(SMILEYS))

        else:
            final.append(word)

    return " ".join(final)


def uwu(entry: Union[list, str], *, flags: UwuifyFlag = 0) -> str:
    if len(entry) == 0:  # Maybe this should error??
        return entry

    if flags & UwuifyFlag.YU:
        entry = _do_yu(entry)

    entry = _do_uwu(entry)

    if flags & UwuifyFlag.SMILEY:
        entry = _do_smily(entry)

    return entry
