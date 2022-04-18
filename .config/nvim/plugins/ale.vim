" ALE config
let g:ale_linters= {
\   'javascript': ['eslint'],
\   'python': ['pyls', 'flake8'],
\   'vim': ['vint'],
\   'cpp': ['clang'],
\   'c': ['clang'],
\ 	'go': ['gobuild'],
\}
let g:ale_fixers = {
\   '*': ['remove_trailing_lines', 'trim_whitespace'],
\   'c': ['clang-format'],
\   'cpp': ['clang-format'],
\   'css': ['prettier'],
\   'javascript': ['prettier'],
\   'typescript': ['prettier'],
\   'html': ['prettier'],
\   'json': ['prettier'],
\   'scss': ['prettier'],
\   'yalm': ['prettier'],
\   'python': ['black', 'reorder-python-imports', 'add_blank_lines_for_python_control_statements'],
\   'go': ['gofmt', 'goimports'],
\}
let g:ale_fix_on_save = 1
let g:ale_completion_enabled = 0
let g:ale_hover_cursor = 1
let g:ale_disable_lsp = 1
let g:ale_python_pylint_auto_pipenv = 1
let g:ale_lint_on_text_changed = 'never'
let g:ale_lint_on_insert_leave = 0
let g:ale_lint_on_enter = 0
let g:ale_python_pyls_auto_pipenv = 1
let g:ale_python_flake8_auto_pipenv = 1
let g:ale_python_black_auto_pipenv = 1

" Echodoc config
let g:echodoc#enable_at_startup = 1