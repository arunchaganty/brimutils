#!/usr/bin/env python

def install(prefix):
    pass

if __name__ == '__main__':
    import os
    import getopt
    import sys

    cmd, args = sys.argv[0], sys.argv[1:]

    opts, args = getopt.gnu_getopt(args, '', ['prefix='])
    opts = dict(opts)

    prefix = opts.get('--prefix', os.path.expanduser('~/bin'))

    install(prefix)
