# -*- coding: utf-8 -*-

import argparse
from sys import stdin, stdout

from uwuify import *

def parse_args():
    parser = argparse.ArgumentParser(prog='uwuify', description='UwUify text')

    parser.add_argument('--input', nargs='?', type=argparse.FileType(), default=stdin,
                        help='Input file; defaults to stdin'
                        )

    parser.add_argument('--output', nargs='?', type=argparse.FileType('w+'), default=stdout,
                        help='Output file; defaults to stdout'
                        )

    parser.add_argument('-m', '--mode', choices=['translate', 'regex'], default='regex',
                        help='Uwuify mode, defaults to using regex'
                        )

    return parser.parse_args()


def main():
    args = parse_args()

    mode = UwuifyMode[args.mode]

    entry = args.input.read()

    output = uwu_text(entry, mode=mode)

    args.output.write(output)


if __name__ == '__main__':
    main()
