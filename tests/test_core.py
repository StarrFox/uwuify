from uwuify import core


# TODO: expand tests

def test_do_uwu():
    assert core._do_uwu("hello") == "hewwo"


def test_do_yu():
    assert core._do_yu("you") == "yoyu"


def test_do_smiley():
    import random

    # this is so we always have the same random conditions
    random.seed(0)

    assert core._do_smiley("abc!") == "abc! (U ᵕ U❁)"


def test_do_stutter():
    assert (
        core._do_stutter("hello hello hello hello", 1)
        == "h-hello h-hello h-hello h-hello"
    )


def test_uwu():
    import random
    random.seed(0)

    flags = core.UwuifyFlag.STUTTER
    flags |= core.UwuifyFlag.YU
    flags |= core.UwuifyFlag.SMILEY

    assert(core.uwu("hello! how are you?", flags=flags) == "h-hewwo! (U ᵕ U❁) how awe yoyu? (◦ᵕ ˘ ᵕ◦)")
