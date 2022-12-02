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

import click

from uwuify import SMILEY, YU, uwu, STUTTER


def allow_pipe(ctx, param, value):
    if not value and not click.get_text_stream("stdin").isatty():
        pipped = click.get_text_stream("stdin").read().strip()
        return pipped.split(" ")  # Compatibility with -1 garbage
    else:
        return value


@click.command(help="Command line uwuification.")
@click.option("--smiley", is_flag=True, help="Add smileys on puntuation.")
@click.option("--yu", is_flag=True, help="Replace u with yu")
@click.option(
    "--stutter",
    help="Add stutter for every 4-th word.",
    is_flag=True,
    type=int
)
@click.argument("text", nargs=-1, callback=allow_pipe)
def main(smiley, yu, text, stutter):
    text = " ".join(text)
    flags = 0

    if smiley:
        flags |= SMILEY

    if yu:
        flags |= YU

    if stutter:
        flags |= STUTTER

    uwuified = uwu(text, flags=flags)
    click.echo(uwuified)
