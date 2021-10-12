let mapleader = " "

call plug#begin('~/.vim/plugged')

"Dracula color scheme plugin- set in colors.vim
Plug 'dracula/vim', { 'as': 'dracula' }

"Git plugins
Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-rhubarb'
Plug 'junegunn/gv.vim'

"Language server plugin
Plug 'neovim/nvim-lspconfig'

"Black code python formatter
Plug 'ambv/black'

"Man page viewer
Plug 'vim-utils/vim-man'

Plug 'mbbill/undotree'

call plug#end()

nnoremap <silent> <C-f> :silent !tmux neww tmux-sessionizer<CR>
nnoremap <Leader><CR> :so ~/.config/nvim/init.vim<CR>
nnoremap <Leader>+ :vertical resize +5<CR>
nnoremap <Leader>- :vertical resize -5<CR>
nnoremap <Leader>rp :resize 100<CR>

nnoremap <leader>x :silent !chmod +x %<CR>

inoremap <C-c> <esc>
