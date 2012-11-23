#!/usr/bin/env python

def transpose(rows):
    return zip(*rows)

if __name__ == '__main__':
    import sys

    cmd, args = sys.argv[0], sys.argv[1:]

    f = sys.stdin
    if len(args) > 0:
        f = open(args[0], 'r')

    for y in transpose(x.split() for x in f):
        print(' '.join(y))

    f.close()
