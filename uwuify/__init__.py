# -*- coding: utf-8 -*-

from typing import Union
import re
from enum import Enum


class UwuifyMode(Enum):
    translate = 0
    regex = 1


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


def do_translate(entry: Union[list, str]) -> str:
    if not isinstance(entry, list):
        entry = entry.split(' ')  # list of words

    final = []
    for word in entry:
        final.append(word[0].translate(WREPLACE) + word[1:].translate(UWU))
    return ' '.join(final)


def do_regex(entry: Union[list, str]) -> str:
    if isinstance(entry, list):
        entry = ' '.join(entry)

    regexed = re.sub(ERREPLACE, r'\g<1>a', entry)

    return do_translate(regexed)


def uwu_text(entry: Union[list, str], *, mode: UwuifyMode = UwuifyMode.regex) -> str:
    if len(entry) == 0:  # Maybe this should error??
        return entry

    if mode.value == 0:
        return do_translate(entry)

    elif mode.value == 1:
        return do_regex(entry)
