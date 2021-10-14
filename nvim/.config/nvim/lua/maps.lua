---------------------------------------------------------
-- Keymaps configuration file: keymaps of neovim
-- and plugins.
-----------------------------------------------------------

local map = vim.api.nvim_set_keymap
local default_opts = {noremap = true, silent = true}
local cmd = vim.cmd

-- map the leader key
-- map('n', '<Space>', '', {})
vim.g.mapleader = ' '  -- 'vim.g' sets global variables


--map('n', '<leader>n', ':bnext<cr>', options)
--map('n', '<leader>p', ':bprev<cr>', options)

-----------------------------------------------------------
-- Neovim shortcuts:
-----------------------------------------------------------

-- clear search highlighting
map('n', '<leader>c', ':nohl<CR>', default_opts)
map('n', '<leader><esc>', ':nohlsearch<cr>', default_opts)

-- map Esc to kk
map('i', 'kk', '<Esc>', {noremap = true})
map('n', '<C-c>', '<Esc>', {noremap = true})

-- don't use arrow keys
map('', '<up>', '<nop>', {noremap = true})
map('', '<down>', '<nop>', {noremap = true})
map('', '<left>', '<nop>', {noremap = true})
map('', '<right>', '<nop>', {noremap = true})

-- fast saving with <leader> and s
map('n', '<leader>s', ':w<CR>', default_opts)
map('i', '<leader>s', '<C-c>:w<CR>', default_opts)

-- move around splits using Ctrl + {h,j,k,l}
map('n', '<C-h>', '<C-w>h', default_opts)
map('n', '<C-j>', '<C-w>j', default_opts)
map('n', '<C-k>', '<C-w>k', default_opts)
map('n', '<C-l>', '<C-w>l', default_opts)

-- close all windows and exit from neovim
map('n', '<leader>q', ':quitall<CR>', default_opts)

-----------------------------------------------------------
-- Applications & Plugins shortcuts:
-----------------------------------------------------------
-- open terminal
map('n', '<C-t>', ':Term<CR>', {noremap = true})

--Git Commands
map('n', '<leader>ga', ':Git fetch --all<CR>', {noremap = true})
map('n', '<leader>grum', ':Git rebase upstream/master<CR>', {noremap = true})
map('n', '<leader>grom', ':Git rebase origin/master<CR>', {noremap = true})

map('n', '<leader>gh', ':diffget //3<CR>', {noremap = true})
map('n', '<leader>gu', ':diffget //2<CR>', {noremap = true})
map('n', '<leader>gs', ':G<CR>', {noremap = true})
map('n', '<leader>gp', ':Git push<CR>', {noremap = true})
-- nvim-tree
map('n', '<leader>n', ':NERDTreeFocus<CR>', default_opts)       -- open/close
map('n', '<C-n>', ':NERDTree<CR>', default_opts)       -- open/close
map('n', '<C-t>', ':NERDTreeToggle<CR>', default_opts)  -- refresh
map('n', '<C-f>', ':NERDTreeFind<CR>', default_opts) -- search file

-- Sessionizer
map('n', '<C-f>', ':silent !tmux neww tmux-sessionizer<CR>', default_opts)       -- open/close

-- Telescope
map('n', '<leader>ff', '<cmd>Telescope find_files<CR>', default_opts) -- search file
map('n', '<leader>fg', '<cmd>Telescope live_grep<CR>', default_opts) -- search file
map('n', '<leader>fb', '<cmd>Telescope buffers<CR>', default_opts) -- search file
map('n', '<leader>fh', '<cmd>Telescope help_tags<CR>', default_opts) -- search file

-- Set file permissions
map('n', '<leader>x', ':silent !chmod +x %<CR>', default_opts) -- search file

