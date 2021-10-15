require('settings')    -- lua/settings.lua
require('maps')        -- lua/maps.lua
--require('statusline')  -- lua/statusline.lua

local Plug = vim.fn['plug#']

vim.call('plug#begin', '~/.config/nvim/plugged')

--Dracula color scheme plugin- set in colors.vim
Plug('dracula/vim', { as = 'dracula' })

--Git plugins
Plug 'tpope/vim-fugitive'
Plug 'tpope/vim-rhubarb'
Plug 'junegunn/gv.vim'

--Language server plugin
Plug 'neovim/nvim-lspconfig'

--Black code python formatter
Plug 'ambv/black'

--Man page viewer
Plug 'vim-utils/vim-man'

Plug 'mbbill/undotree'

--Telescope
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'

--NerdTree
Plug 'preservim/nerdtree'

vim.call('plug#end')

vim.cmd  [[let g:dracula_colorterm = 0]]
vim.cmd  [[colorscheme dracula]]

require("briggsadier.telescope")
--require('telescope').setup{ defaults = { vimgrep_arguments = { 'rg', '--hidden', '--color=never', '--no-heading', '--with-filename', '--line-number', '--column', '--smart-case' }}}
