#!/usr/bin/env python

import distutils.dir_util
import getopt
import inspect
import os
import sys

ALIASES_F = 'aliases.sh'

def this_file():
    return os.path.abspath(inspect.getfile(inspect.currentframe()))

def install(prefix, bash_aliases_f, dry_run=False, vebose=False):
    # TODO:
    # - Install bin/
    # - Install each ext/
    # - Install aliases.sh

    print('Installing scripts from bin/')

    copied = distutils.dir_util.copy_tree('bin/', prefix,
                                          verbose=verbose, dry_run=dry_run)
    print('  ' + '\n  '.join(copied))

    print('Installing scripts from ext/bitly/data_hacks')

    copied = distutils.dir_util.copy_tree('ext/bitly/data_hacks/', prefix,
                                          verbose=verbose, dry_run=dry_run)
    print('  ' + '\n  '.join(copied))

    print('Installing aliases (appending to %s from %s):' % (bash_aliases_f, ALIASES_F))

    with open(ALIASES_F, 'r') as src:
        with open(bash_aliases_f, 'a') as dst:
            dst.write('\n\n')
            dst.write('# Added by exoutils install script -- %s\n' % this_file())
            for l in src:
                dst.write(l)

if __name__ == '__main__':
    cmd, args = sys.argv[0], sys.argv[1:]

    opts, args = getopt.gnu_getopt(args, '', ['prefix=',
                                              'bash-aliases=',
                                              'dry-run',
                                              'verbose'])
    opts = dict(opts)

    prefix = opts.get('--prefix', os.path.expanduser('~/bin'))
    bash_alises_f = opts.get('--bash-aliases', os.path.expanduser('~/.bash_aliases'))
    dry_run = '--dry-run' in opts
    verbose = '--verbose' in opts

    prompt = \
        'Will %sinstall into %s and append alias commands to %s -- continue? [y/n]' \
        % ('pretend to ' if dry_run else '', prefix, bash_aliases_f))
    resp = raw_input(prompt)

    if False and resp in ['y', 'yes']:
        install(prefix, bash_aliases_f, dry_run, verbose)
