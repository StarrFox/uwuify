# -*- coding: utf-8 -*-

"""
Copyright (c) 2020 StarrFox

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from typing import Union
import re
from enum import Enum

__version__ = '0.2.0'


class UwuifyMode(Enum):
    translate = 0
    regex = 1
    smiley = 2


# from https://cutekaomoji.com/characters/uwu/
SMILEYS = [
    '(ᵘʷᵘ)', '(ᵘﻌᵘ)', '(◡ ω ◡)', '(◡ ꒳ ◡)', '(◡ w ◡)', '(◡ ሠ ◡)', '(˘ω˘)', '(⑅˘꒳˘)', '(˘ᵕ˘)', '(˘ሠ˘)', '(˘³˘)',
    '(˘ε˘)', '(´˘`)', '(´꒳`)', '(˘˘˘)', '( ᴜ ω ᴜ )', '( ´ω` )۶', '(„ᵕᴗᵕ„)', '(ㅅꈍ ˘ ꈍ)', '(⑅˘꒳˘)', '( ｡ᵘ ᵕ ᵘ ｡)',
    '( ᵘ ꒳ ᵘ ✼)', '( ˘ᴗ˘ )', '(ᵕᴗ ᵕ⁎)', '*:･ﾟ✧(ꈍᴗꈍ)✧･ﾟ:*', '*˚*(ꈍ ω ꈍ).₊̣̇.', '(。U ω U。)', '(。U⁄ ⁄ω⁄ ⁄ U。)',
    '(U ᵕ U❁)', '(U ﹏ U)', '(◦ᵕ ˘ ᵕ◦)', 'ღ(U꒳Uღ)', '♥(。U ω U。)', '– ̗̀ (ᵕ꒳ᵕ) ̖́-',
    '( ͡U ω ͡U )', '( ͡o ᵕ ͡o )', '( ͡o ꒳ ͡o )', '( ˊ.ᴗˋ )', '(灬´ᴗ`灬)', 'uwu', 'owo'
]

WREPLACE = str.maketrans(
    {
        'r': 'w',
        'l': 'w',
        'R': 'W',
        'L': 'W'
    }
)

NOTSTART = str.maketrans(
    {
        'u': 'yu',
        'U': 'yU'
    }
)

UWU = WREPLACE.copy()
UWU.update(NOTSTART)

ERREPLACE = re.compile(r'(\b\w{2,})er\b', re.IGNORECASE)


def _do_translate(entry: Union[list, str]) -> str:
    if not isinstance(entry, list):
        entry = entry.split(' ')  # list of words

    final = []
    for word in entry:
        if word:
            final.append(word[0].translate(WREPLACE) + word[1:].translate(UWU))
        else:
            final.append(' ')
    return ' '.join(final)


def _do_regex(entry: Union[list, str]) -> str:
    if isinstance(entry, list):
        entry = ' '.join(entry)

    regexed = re.sub(ERREPLACE, r'\g<1>a', entry)

    return _do_translate(regexed)


def _do_smily(entry: Union[list, str]) -> str:
    if not isinstance(entry, list):
        entry = entry.split(' ')

    import random

    final = []
    for word in entry:
        if word.endswith(('.', '?', '!')) and random.choice((True, False)):
            final.append(word + ' ' + random.choice(SMILEYS))

        else:
            final.append(word)

    return _do_regex(final)


def uwu_text(entry: Union[list, str], *, mode: UwuifyMode = UwuifyMode.regex) -> str:
    if len(entry) == 0:  # Maybe this should error??
        return entry

    if mode.value == 0:
        return _do_translate(entry)

    elif mode.value == 1:
        return _do_regex(entry)

    elif mode.value == 2:
        return _do_smily(entry)
