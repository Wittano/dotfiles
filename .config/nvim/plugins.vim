call plug#begin('~/.local/share/nvim/plugged')

  " Auto Complete
  Plug 'fatih/vim-go', { 'do': ':GoUpdateBinaries' } " GoLang
  Plug 'https://github.com/jansenm/vim-cmake.git' " Cmake

  " coc.nvim
  Plug 'neoclide/coc.nvim', {'branch': 'release'}
  Plug 'clangd/coc-clangd'
  Plug 'voldikss/coc-cmake'
  Plug 'josa42/coc-docker'
  Plug 'josa42/coc-sh'
  Plug 'neoclide/coc-html'
  Plug 'neoclide/coc-json'
  Plug 'neoclide/coc-tsserver'
  Plug 'neoclide/coc-yaml'
  Plug 'neoclide/coc-prettier'

  "Theme
  Plug 'vim-airline/vim-airline-themes'
  Plug 'jschmold/sweet-dark.vim'

  "Formater
  Plug 'bronson/vim-trailing-whitespace' "Remove unnecesarry spaces and whitespace
  Plug 'airblade/vim-gitgutter' "Show changes in repo

  "Syntax
  Plug 'https://github.com/PotatoesMaster/i3-vim-syntax.git' "Vim i3 syntax
  Plug 'https://github.com/octol/vim-cpp-enhanced-highlight.git' "Cpp syntax
  Plug 'https://github.com/pboettch/vim-cmake-syntax.git' " CMake syntax
  Plug 'sheerun/vim-polyglot' " Syntax for so much language
  Plug 'dense-analysis/ale' " ALE
  Plug 'autozimu/LanguageClient-neovim', {
    \ 'branch': 'next',
    \ 'do': 'bash install.sh',
    \ }
  Plug 'LnL7/vim-nix' " Vim-nix

  "Lightline
  Plug 'itchyny/lightline.vim' "Light line
  Plug 'https://github.com/itchyny/vim-gitbranch.git' "Show currently git branch on Light line

  "Facilitate
  Plug 'https://github.com/jlanzarotta/bufexplorer.git'
  Plug 'jiangmiao/auto-pairs' " Added missing bracket
  Plug 'https://github.com/tpope/vim-fugitive.git'
  Plug 'https://github.com/tpope/vim-commentary.git' "Auto commentary
  Plug 'https://github.com/tpope/vim-surround.git' "Click link and you know what is it
  Plug 'https://github.com/tpope/vim-repeat.git' "Repeat last action if you click '.'
  Plug 'reedes/vim-pencil' "Facilitate read text
  Plug 'terryma/vim-multiple-cursors' " Modified code in few lines at same time
  Plug 'https://github.com/Shougo/echodoc.vim.git' " Show parms in function

call plug#end()
