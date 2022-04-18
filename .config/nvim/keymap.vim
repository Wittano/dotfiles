map tt :NERDTreeToggle<CR>
map tc :NERDTreeClose<CR>
map tf :NERDTreeFocus<CR>
map <F2> :CocCommand document.renameCurrentWord<CR>

nmap <silent> <A-k> :wincmd k<CR>
nmap <silent> <A-j> :wincmd j<CR>
nmap <silent> <A-h> :wincmd h<CR>
nmap <silent> <A-l> :wincmd l<CR>

"Tab managment
map <C-o> :tabnew<CR>
map <C-c> :tabclose<CR>
map <C-l> :tabn<CR>
map <C-h> :tabp<CR>

" Go keymaps
autocmd FileType go map <F2> :GoRename<CR>
autocmd FileType go map <F5> :GoRun<CR>