#!/usr/bin/env python

if __name__ == '__main__':
    import sys
    cmd, args = sys.argv[0], sys.argv[1:]

    if len(args) < 1:
        print('Usage:')
        print('  %s <end>' % cmd)
        print('  %s <start> <end> [step]' % cmd)
        sys.exit(1)

    args = [int(x) for x in args]

    print(' '.join(str(x) for x in xrange(*args)))
