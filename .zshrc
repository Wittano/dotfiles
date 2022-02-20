# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/home/wittano/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
# ZSH_THEME="robbyrussell"
# ZSH_THEME="avit"
ZSH_THEME="af-magic"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
	@@ -25,14 +23,13 @@ ZSH_THEME="af-magic"
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
export UPDATE_ZSH_DAYS=7

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"
	@@ -47,7 +44,10 @@ export UPDATE_ZSH_DAYS=7
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
	@@ -70,16 +70,7 @@ COMPLETION_WAITING_DOTS="true"
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
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

	@@ -91,11 +82,11 @@ source $ZSH/oh-my-zsh.sh
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
if [[ -n $SSH_CONNECTION ]]; then
  export EDITOR='nvim'
else
  export EDITOR='vim'
fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"
	@@ -104,69 +95,7 @@ fi
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.

EDITOR=nvim
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
