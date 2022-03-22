#!/usr/bin/env bash

echo "Installing Nixos configuration"
nix-env -iA nixos.git nixos.vim

if [ ! -d '/vagrant/nix-dotfiles' ]; then 
    nix-shell -p git --run 'git clone "https://github.com/Wittano/nix-dotfiles.git" /vagrant/nix-dotfiles'
fi