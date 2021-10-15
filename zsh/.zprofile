export XDG_CONFIG_HOME=$HOME/.config
VIM="nvim"

export GOPATH=$HOME/go
export GIT_EDITOR=$VIM

catr() {
    tail -n "+$1" $3 | head -n "$(($2 - $1 + 1))"
}

validateYaml() {
    python -c 'import yaml,sys;yaml.safe_load(sys.stdin)' < $1
}

git config --global user.name "Kyle Briggs"

goWork() {
    git config --global user.email "briggsy87@gmail.com"
}

goPersonal() {
    git config --global user.email "kyle.briggs@specopssoft.com"
}


cat1Line() {
    cat $1 | tr -d "\n"
}

# Where should I put you?
bindkey -s ^f "tmux-sessionizer\n"
