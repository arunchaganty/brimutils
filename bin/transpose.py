#!/usr/bin/env python

def print_usage():
    print('Usage: transpose.py [-d <delim>] [file]')
    print('')
    print('  If no file is given, read stdin.')
    print('')

def transpose(rows):
    return zip(*rows)

if __name__ == '__main__':
    import getopt
    import os
    import sys

    cmd, args = sys.argv[0], sys.argv[1:]

    try:
        opts, args = getopt.gnu_getopt(args, 'd:', [])
    except Exception:
        print_usage()
        sys.exit(1)

    opts = dict(opts)
    delim = opts.get('-d')
    join_delim = ' ' if delim is None else delim

    f = sys.stdin
    if len(args) > 0:
        f = open(args[0], 'r')

    for y in transpose(x.rstrip(os.linesep).split(delim) for x in f):
        print(join_delim.join(y))

    f.close()
