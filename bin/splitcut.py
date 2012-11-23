#!/usr/bin/env python

def splitcut(l, fields=None, delim=None):
    l = l.rstrip()
    l = l.split(delim)
    if fields is None:
        cuts = l
    else:
        cuts = [l[i] for i in fields if 0 <= i < len(l)]
    if delim is None:
        return ' '.join(cuts)
    else:
        return delim.join(cuts)

def parse_f(fields):
    '''Input is a string argument to -f, such as '1,2,5-7,8-12,15'.'''
    fs = set()
    for intval in fields.split(','):
        ends = [int(x) for x in intval.split('-')]
        if len(ends) == 2:
            lo, hi = ends
        elif len(ends) == 1:
            lo = hi = ends[0]
        else:
            raise ValueError('Invalid -f argument: %s' % intval)
        fs = fs.union(set(range(lo-1, hi)))
    return fs

if __name__ == '__main__':
    import getopt
    import sys
 
    args = sys.argv[1:]
    optvals, args = getopt.gnu_getopt(args, 'f:d:')
    optvals = dict(optvals)

    fields = optvals.get('-f')
    delim = optvals.get('-d')

    if fields is not None:
        fields = parse_f(fields)

    f = sys.stdin
    if len(args) > 0:
        fin = args[0]
        if fin != '-':
            f = open(fin, 'r')

    for l in f:
        print(splitcut(l, fields, delim))

    f.close()
