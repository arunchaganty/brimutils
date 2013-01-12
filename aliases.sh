alias trim='sed "s/^[[:space:]]*\(.*\)[[:space:]]*$/\1/"'
alias ltrim='sed "s/^[[:space:]]*\(.*\)$/\1/"'
alias rtrim='sed "s/^\(.*\)[[:space:]]*$/\1/"'

alias ls='ls -G' # Make ls output colorful.
alias ll='ls -lF'
alias la='ls -aF'
alias lsh='ls -lshF'
alias lsha='ls -lshaF'
alias lsah='lsha'

# git
alias g='git'
alias gitd='git diff'
alias gits='git status | less'

# taskwarrior
alias t='task'
