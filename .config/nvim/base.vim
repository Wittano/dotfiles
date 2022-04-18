syntax on
syntax enable

set background=dark
set autoindent
set smarttab
set tabstop=4
set shiftwidth=4
set smartcase
set nu rnu
set clipboard+=unnamedplus
filetype on
filetype plugin indent on
set encoding=UTF-8
set cmdheight=2
set nobackup
set nowritebackup
set shortmess+=c
set signcolumn=yes

" Auto start command
autocmd FileType python set sw=4
autocmd FileType python set ts=4
autocmd FileType python set sts=4
autocmd FileType apache setlocal commentstring=#\ %s
autocmd FileType html set omnifunc=htmlcomplete#CompleteTags

set termguicolors     " enable true colors support
" Theme
colorscheme sweet_dark