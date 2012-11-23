#!/usr/bin/env python

import operator


def cmd_max(lines):
    maxs, _ = fold_columns(lines, max, -float('inf'))
    print(' '.join(str(x) for x in maxs))

def cmd_min(lines):
    mins, _ = fold_columns(lines, min, float('inf'))
    print(' '.join(str(x) for x in mins))

def cmd_sum(lines):
    sums, _ = fold_columns(lines, operator.add, 0.0)
    print(' '.join(str(x) for x in sums))

def cmd_mean(lines):
    sums, counts = fold_columns(lines, operator.add, 0.0)
    print(' '.join(str(x / n) for x, n in zip(sums, counts)))

def fold_columns(lines, op, init):
    folds = {}
    counts = {}
    for l in sys.stdin:
        for i, x in enumerate(l.split()):
            folds[i] = op(folds.get(i, init), float(x))
            counts[i] = counts.get(i, 0) + 1

    folds = [x for _, x in sorted(folds.items())]
    counts = [x for _, x in sorted(counts.items())]
    return folds, counts

if __name__ == '__main__':
    def print_usage():
        print('Usage: colstat.py <%s>' % '|'.join(CMDS.keys()))

    import sys

    CMDS = {
        'max': cmd_max,
        'min': cmd_min,
        'sum': cmd_sum,
        'mean': cmd_mean,
        }

    args = sys.argv[1:]

    if len(args) < 1:
        print_usage()
        sys.exit(-1)

    cmd = args[0]

    if cmd not in CMDS:
        print_usage()
        sys.exit(-1)

    CMDS[cmd](sys.stdin)
