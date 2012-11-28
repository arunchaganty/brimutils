#!/usr/bin/env python

import getopt
import os
import sys

def print_usage():
    print('Usage: reshape.py [-c <num columns>] [-d <delimeter>] [-f <fill value>]')
    print('')

def reshape(rows, numcols=1, delim=None, fill=None):
    join_delim = ' ' if delim is None else delim
    buf = []
    for row in rows:
        elems = row.rstrip(os.linesep).split(delim)
        buf.extend(elems)
        while len(buf) >= numcols:
            print(join_delim.join(buf[:numcols]))
            buf = buf[numcols:]
    if len(buf) > 0:
        if fill is not None:
            buf.extend([fill] * (numcols - len(buf)))
        print(join_delim.join(buf))

if __name__ == '__main__':

    args = sys.argv[1:]
    try:
        opts, args = getopt.gnu_getopt(args, 'c:d:f:')
    except Exception:
        print_usage()
        sys.exit(1)

    opts = dict(opts)

    numcols = int(opts.get('-c', 1))
    delim = opts.get('-d')
    fill = opts.get('-f')

    f = sys.stdin
    if len(args) > 0:
        fin = args[0]
        if fin != '-':
            f = open(fin, 'r')

    reshape(f, numcols, delim, fill)

    f.close()
