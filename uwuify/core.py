import re
from enum import IntFlag
from typing import Union


class UwuifyFlag(IntFlag):
    NONE = 0
    SMILEY = 1
    YU = 2
    STUTTER = 4
    NOUWU = 8


# from https://cutekaomoji.com/characters/uwu/ and https://textfac.es/
# (and some made by Plextora: https://github.com/Plextora)
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
    "(˘˘˘)",
    "( ᴜ ω ᴜ )",
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
    "(ᴜ‿ᴜ✿)",
    "~(˘▾˘~)",
    "(｡ᴜ‿‿ᴜ｡)",
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


def _do_smiley(entry: str) -> str:
    if not isinstance(entry, list):
        entry_split = entry.split(" ")

    import random

    final = []
    for word in entry_split:
        if word.endswith((".", "?", "!")):
            final.append(word + " " + random.choice(SMILEYS))

        else:
            final.append(word)

    return " ".join(final)


def _do_stutter(entry: str, stutter_every_nth_word: int = 4) -> str:
    if stutter_every_nth_word < 1:
        raise ValueError(
            f"stutter_every_nth_word must be above 0; passed {stutter_every_nth_word}"
        )

    listofstr = entry.split(" ")
    result = []
    for index, word in enumerate(listofstr):
        if index % stutter_every_nth_word == 0:
            result.append("{}-{}{}".format(word[0], word[0], word[1:]))
        else:
            result.append(word)
    return " ".join(result)


def uwu(entry: Union[list, str], *, flags: UwuifyFlag = UwuifyFlag.NONE) -> str:
    if isinstance(entry, list):
        entry = " ".join(entry)

    if len(entry) == 0:  # Maybe this should error??
        return entry

    if flags & UwuifyFlag.YU:
        entry = _do_yu(entry)

    if not flags & UwuifyFlag.NOUWU:
        entry = _do_uwu(entry)

    if flags & UwuifyFlag.STUTTER:
        entry = _do_stutter(entry)

    if flags & UwuifyFlag.SMILEY:
        entry = _do_smiley(entry)

    return entry
