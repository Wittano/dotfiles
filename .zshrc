# export PATH=$HOME/bin:/usr/local/bin:$PATH

export ZSH="$HOME/.oh-my-zsh"

ZSH_THEME="af-magic"

export UPDATE_ZSH_DAYS=7

COMPLETION_WAITING_DOTS="true"

plugins=(git
  branch
  colorize
  colored-man-pages
  docker
  docker-compose
  python
  tmux
  vi-mode
)

source $ZSH/oh-my-zsh.sh

if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='nvim'
else
  export EDITOR='vim'
fi

EDITOR=vim
PATH=$PATH:$HOME/.local/bin:$HOME/.cargo/bin
VISUAL=$EDITOR
SERVER_IP="192.168.1.160"

# Aliases

# Debian/Ubuntu base
if [ -n "$(command -v apt)" ]; then
  alias ai="sudo apt install --no-install-recommends --auto-remove --show-progress"
  alias au="sudo apt update && sudo apt upgrade"
  alias ar="sudo apt remove"
  alias ara="sudo apt autoremove"
  alias ap="sudo apt purge"
  alias as="apt search"
fi

# Void linux
if [ -n "$(command -v xbps-install)" ]; then
  alias xq='xbps-query -R'
  alias xi='sudo xbps-install -S'
  alias xiu='sudo xbps-install -Su'
  alias xr='sudo xbps-remove'
  alias xro='sudo xbps-remove -Oo'
fi

# Config shotcuts
alias bc="$EDITOR ~/.config/bspwm/bspwmrc"
alias kc="$EDITOR ~/.config/sxhkd/sxhkdrc"
alias zc="$EDITOR ~/.zshrc"
alias oc="$EDITOR ~/.oh-my-zsh"
alias vc="$EDITOR ~/.config/nvim/init.vim"

# YADM alias
alias yaa="yadm add"
alias yac="yadm commit"
alias yas="yadm status"
alias yapush="yadm push origin main"
alias yapull="yadm pull origin main"
alias yad="yadm diff"

# Programming
alias py='python3'
alias npm='pnpm'
if [ -z "$(command -v nvim)" ]; then
  alias vi="vim"
else
  alias vi="nvim"
fi

# Server
alias sl="ssh wittano@${SERVER_IP}"
alias re='sudo sshfs -o allow_other wittanosftp@192.168.10.160:/ /mnt/remote'

# Virtuals
alias vu="ssh wittano@192.168.122.100"
alias vd="ssh wittano@192.168.122.129"
alias vn="ssh wittano@192.168.122.83"

# Utils
alias cl="sudo poweroff"
alias xc='xprop | grep _OB_APP_CLASS'
alias yta='youtube-dl -x --audio-format mp3 -o "%(title)s.%(ext)s" --prefer-ffmpeg'
alias red='redshift -l 51.2181945:22.5546776'
alias cld='bash $HOME/project/bash/cleanDocker.sh'
alias ra='ranger'
alias vm='bash $HOME/projects/config/system/scripts/select-vagrant-vm.sh'
