set -gx EDITOR vim

# Set PATH
set -U fish_user_paths $HOME/.local/bin $fish_user_paths

# aliases
alias pra="sudo pacman -Rsn (pacman -Qdtq)"
alias yta="youtube-dl -x --audio-format mp3 -o '%(title)s.%(ext)s' --prefer-ffmpeg"

if status is-interactive
    # Commands to run in interactive sessions can go here
end
