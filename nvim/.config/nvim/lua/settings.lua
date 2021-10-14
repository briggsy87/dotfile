local o = vim.o
local wo = vim.wo
local bo = vim.bo

-- global options
o.guicursor = ''
o.swapfile = false
o.dir = '/tmp'
o.smartcase = true
o.laststatus = 2
o.hlsearch = true
o.incsearch = true
o.ignorecase = true
o.scrolloff = 12
o.hidden = true
o.errorbells = false
o.backup = false
o.undodir = "~/.vim/undodir"
o.termguicolors = true
o.undofile = true
o.scrolloff = 8
o.cmdheight = 1
o.updatetime = 50


-- window-local options
wo.number = true
wo.wrap = false
wo.colorcolumn = '80'
wo.relativenumber = true
wo.signcolumn = 'yes'

-- buffer-local options
bo.expandtab = true
bo.smartindent = true
bo.tabstop = 4
bo.softtabstop = 4
bo.shiftwidth = 4
