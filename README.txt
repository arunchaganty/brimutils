brimutils
Created and curated by Roy Frostig
Last updated 11/23/12

brimutils is a collection of fringe utilities to complement GNU
coreutils.

File structure:

  bin/
    Various pre-built utility binaries and scripts, usually written by
    me.

  ext/
    Other projects that produce utility binaries and scripts, usually
    written by others (often incporporated as git submodules).

  aliases.sh
    Utils in disguise as bash aliases.

  Makefile
    Automatic build and install.  Considers the following environment
    variables.

    PREFIX
      Binary install destination.

    ALIASES
      File where bash aliases will go.

    CAREFUL
      If set, do not install binaries if doing so will override a file
      in destination.

    NO_ALIASES
      If set, ${ALIASES} is ignored and no alias commands are
      installed.

  README.txt
    You are here.

============================================================
(C) Copyright 2012, Roy Frostig

http://ai.stanford.edu/~rfrostig

Permission is granted for anyone to copy, use, or modify these
programs and accompanying documents for purposes of research or
education, provided this copyright notice is retained, and note is
made of any changes that have been made.

These programs and documents are distributed without any warranty,
express or implied.  As the programs were written for research
purposes only, they have not been tested to the degree that would be
advisable in any important application.  All use of these programs is
entirely at the user's own risk.
