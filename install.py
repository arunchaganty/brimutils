#!/usr/bin/env python

import distutils.dir_util
import getopt
import inspect
import os
import stat
import sys

# TODO
#   - Now that this is written, it appears a rewrite in far fewer
#     lines of bash would be preferable.  (One plus of python is that
#     we have sane getopt, unlike in darwin bash.  Another is that it
#     ensures python is installed. ;p)

ALIASES_F = 'aliases.sh'
BIN_DIRS = [
    'bin/',
    'ext/bitly/data_hacks/',
    ]

def print_usage():
    print('install.py ' + \
              '[--prefix=DIRPATH] ' + \
              '[--aliases=FILEPATH] ' + \
              '[--no-aliases] ' + \
              '[--dry-run] [--verbose] [--help]')
    print('')
    print('  prefix -- where binaries will be installed.')
    print('  aliases -- file in which to append bash alias commands.')
    print('  use --no-aliases to avoid installing alias-based utils (--aliases will be ignored).')
    print('')

def this_file():
    return os.path.abspath(inspect.getfile(inspect.currentframe()))

def install(prefix, bash_aliases_f, no_aliases=False, dry_run=False, vebose=False):
    for src in BIN_DIRS:
        print('Installing executables from %s' % src)
        # TODO kinda want cp -n here...
        copied = distutils.dir_util.copy_tree(src, prefix,
                                              verbose=verbose, dry_run=dry_run)
        # chmod +x everything we just copied over.
        for f in copied:
            os.chmod(f, os.stat(f).st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        print('  ' + '\n  '.join(copied))

    if not no_aliases:
        print('Installing aliases (appending to %s from %s)' \
                  % (bash_aliases_f, ALIASES_F))

        if not dry_run:
            with open(ALIASES_F, 'r') as src:
                with open(bash_aliases_f, 'a') as dst:
                    dst.write('\n\n')
                    dst.write('# Added by exoutils install script -- %s\n' \
                                  % this_file())
                    for l in src:
                        if not l.startswith('#'):
                            if verbose:
                                print('  %s' % l.rstrip())
                            dst.write(l)

    print('')
    print('Install complete.  You probably want to add %s to your PATH.' \
              % os.path.abspath(os.path.expanduser(prefix)))


if __name__ == '__main__':
    cmd, args = sys.argv[0], sys.argv[1:]

    try:
        opts, args = getopt.gnu_getopt(args, '', ['prefix=',
                                                  'aliases=',
                                                  'no-aliases',
                                                  'dry-run',
                                                  'verbose',
                                                  'help',
                                                  'usage'])
    except Exception:
        print_usage()
        sys.exit(1)

    opts = dict(opts)

    if '--help' in opts or '--usage' in opts:
        print_usage()
        sys.exit(0)

    prefix = opts.get('--prefix', os.path.expanduser('~/bin'))
    bash_aliases_f = opts.get('--aliases', os.path.expanduser('~/.bash_aliases'))
    no_aliases = '--no-aliases' in opts
    dry_run = '--dry-run' in opts
    verbose = '--verbose' in opts

    prompt = \
        'Will %sinstall into %s and %sappend alias commands to %s -- continue? [y/n] ' \
        % (
        'pretend to ' if dry_run else '',
        prefix,
        'NOT ' if no_aliases else '',
        bash_aliases_f,
        )
    resp = raw_input(prompt)

    if resp in ['y', 'yes']:
        install(prefix, bash_aliases_f, no_aliases, dry_run, verbose)
