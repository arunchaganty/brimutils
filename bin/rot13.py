#!/usr/bin/env python

def rot13_char(x):
    if ord('A') <= ord(x) <= ord('Z'):
        return chr(((ord(x) - ord('A') + 13) % 26) + ord('A'))
    if ord('a') <= ord(x) <= ord('z'):
        return chr(((ord(x) - ord('a') + 13) % 26) + ord('a'))
    return x

def rot13(strs):
    return ' '.join(
        ''.join(rot13_char(x) for x in s)
        for s in strs
        )

if __name__ == '__main__':
    import sys

    if len(sys.argv) <= 1:
        print('Usage: rot13.py string [string [...]]')
        sys.exit(1)

    print(rot13(sys.argv[1:]))
