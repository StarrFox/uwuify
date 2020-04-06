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

import click

from uwuify import *

@click.command(help='Command line uwuification.')
@click.argument('input', type=click.File())
@click.argument('output', type=click.File('w'))
@click.option('--mode',
              type=click.Choice(('translate', 'regex'), case_sensitive=False),
              default='regex',
              help='Mode to use for the uwuification process.'
              )
def main(input, output, mode):
    mode = UwuifyMode[mode]

    entry = input.read()

    uwuified = uwu_text(entry, mode=mode)

    output.write(uwuified)


if __name__ == '__main__':
    main()
