from libqtile import widget
from settings.theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='light', bg='dark'): 
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=1, padding=5)


def icon(fg='light', bg='dark', fontsize=12, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=60,
        padding=-11
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='Mononoki Nerd Font',
            fontsize=24,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=20, padding=5),
        separator(),
    ]


# primary_widgets = [
#     *workspaces(),
# 
#     separator(),
# 
#     powerline('color5', 'dark'),
# 
#     icon(bg="color5", text=' '), # Icon: nf-fa-download
#     
#     widget.CheckUpdates(
#         background=colors['color5'],
#         colour_have_updates=colors['light'],
#         colour_no_updates=colors['light'],
#         no_update_string='0',
#         display_format='{updates}',
#         update_interval=1800,
#         custom_command='checkupdates',
#     ),
# 
#     powerline('color4', 'color5'),
# 
#     icon(bg="color4", text=' '),  # Icon: nf-fa-feed
#     
#     widget.Net(**base(bg='color4'), interface='wlp58s0'),
# 
#     powerline('color3', 'color4'),
# 
#     widget.CurrentLayoutIcon(**base(bg='color3'), scale=0.65),
# 
#     widget.CurrentLayout(**base(bg='color3'), padding=5),    
# 
#     powerline('color2', 'color3'),
# 
#     icon(bg="color2", fontsize=25, text=' '), # Icon: nf-mdi-calendar_clock
# 
#     widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
# 
#     powerline('color1', 'color2'),
#  
#     widget.Battery(**base(bg='color1'), format='{char} {percent:2.0%} {hour:d}:{min:02d}'),
# 
#     powerline('dark', 'color1'),
# 
#     widget.Systray(background=colors['dark'], padding=5),
# ]
# 
# secondary_widgets = [
#     *workspaces(),
# 
#     separator(),
# 
#     powerline('color1', 'dark'),
# 
#     widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),
# 
#     widget.CurrentLayout(**base(bg='color1'), padding=5),
# 
#     powerline('color2', 'color1'),
# 
#     widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),
# 
#     powerline('dark', 'color2'),
# ]
# 
# widget_defaults = {
#     'font': 'Mononoki Nerd Font',
#     'fontsize': 12,
#     'padding': 1,
# }
# extension_defaults = widget_defaults.copy()

primary_widgets = [
                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors['color3'],
                ),

                widget.TextBox(
                    text='  ',
                    font="Ubuntu Nerd Font",
                    fontsize='18',
                    background=colors['color3'],
                    foreground=colors['active'],
                    #mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("xmenu.sh")},
                    ),
                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color3'],
                    foreground=colors['black'],
                ),

                #widget.TextBox(
                #    text='|',
                #    padding=0,
                #    foreground=colors[5],
                #),

                widget.GroupBox(
                    font="Ubuntu Nerd Font",
                    fontsize=16,
                    margin_y=3,
                    margin_x=6,
                    padding_y=7,
                    padding_x=6,
                    borderwidth=1,
                    active=colors['color2'],
                    inactive=colors['color3'],
                    foreground=colors['color3'],
                    rounded=True,
                    highlight_color=colors['color3'],
                    highlight_method="border",
                    this_current_screen_border=colors['color1'],
                    block_highlight_text_color=colors['color3'],
                    other_current_screen_border=colors['color2'],
                    other_screen_border=colors['color2'],
                ),

                #widget.TextBox(
                #    text='|',
                #    padding=0,
                #    foreground=colors[5],
                #),

                widget.Prompt(
                    background=colors['color3'],
                    foreground=colors['color1'],
                    font="Ubuntu Nerd Font",
                    fontsize=18,
                ),

                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['black'],
                    foreground=colors['color2'],
                ),

                widget.WindowName(
                    background=colors['color2'],
                        ),

                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color2'],
                    foreground=colors['black'],
                ),


                widget.Spacer(),

               widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['black'],
                    foreground=colors['color5'],
                ),

                widget.CurrentLayoutIcon(
                    #custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    scale=0.45,
                    padding=0,
                    background=colors['color5'],
                    font="Ubuntu Nerd Font",
                    fontsize='14',
                ),
                widget.Net(
                    background=colors['color5'],
                    format='{down} ↓↑ {up}'
                ),
                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color5'],
                    foreground=colors['color2'],
                ),
                widget.TextBox(
                         text=" ",
                         font="Ubuntu Nerd Font",
                         fontsize=16,
                         foreground=colors['active'],
                         background=colors['color2'],
                         padding=0,
                         mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("alacritty -e htop")},
                     ),
                widget.CPU(
                        format = '{load_percent}%',
                        background=colors['color2'],
                        foreground=colors['active'],
                        ),
                widget.CPUGraph(
                        background=colors['color2'],
                        foreground=colors['active'],
                        fill_color=colors['color3'],
                        graph_color=colors['color3'],
                        type='box',
                        ),
                 widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color2'],
                    foreground=colors['color3'],
                ),

                widget.DF(
	            fmt = ' {}',
                    font="Ubuntu Nerd Font",
                    fontsize = 14,
	            partition = '/home',
	            format = '{uf}{m} ({r:.0f}%)',
	            visible_on_warn = False,
	            background = colors['color3'],
	            padding = 5,
	            #mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("alacritty -e storage.sh")},
				),

                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color3'],
                    foreground=colors['color2'],
                ),

                widget.Systray(
                    background=colors['color2'],
                    icons_size=18,
                    padding=4,
                ),

                widget.Sep(
                    padding=8,
                    linewidth=0,
                    background=colors['color2'],
                ),

                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color2'],
                    foreground=colors['color3'],
                ),

                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors['color3'],
                ),

                widget.TextBox(
                    text=" ",
                    font="Ubuntu Nerd Font",
                    fontsize=16,
                    foreground=colors['active'],
                    background=colors['color3'],
                    padding=0,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("alacritty -e htop")},
                ),

                widget.Memory(
                    background=colors['color3'],
                    foreground=colors['active'],
                    font="Inconsolata for powerline",
                    fontsize=14,
                    format='{MemUsed: .0f} MB',
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("alacritty -e htop")},
                ),
                widget.MemoryGraph(
                    foreground=colors['active'],
                    background=colors['color3'],
                    fill_color=colors['color2'],
                    graph_color=colors['color2'],
                ),
                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color3'],
                    foreground=colors['color2'],
                ),

                widget.TextBox(
                    text="蓼",
                    background=colors['color2'],
                    foreground=colors['active'],
                    fontsize=16,
                ),

                widget.Volume(
                    background=colors['color2'],
                    foreground=colors['active'],
                    font="Inconsolata for powerline",
                    fontsize=14,
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("alacritty -e pulsemixer")},
                ),

                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color2'],
                    foreground=colors['color3'],
                ),

                widget.TextBox(
                    text=' ',
                    font="Ubuntu Nerd Font",
                    fontsize='15',
                    padding=0,
                    background=colors['color3'],
                    foreground=colors['active'],
                ),

                widget.Clock(
                    font="Inconsolata for powerline",
                    foreground=colors['active'],
                    background=colors['color3'],
                    fontsize=14,
                    format='%a, %m/%d',
                    ),

                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors['color3'],
                ),

                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color3'],
                    foreground=colors['color2'],
                ),

                widget.TextBox(
                    text=' ',
                    font="Inconsolata for powerline",
                    fontsize='18',
                    padding=0,
                    background=colors['color2'],
                    foreground=colors['active'],
                ),

                widget.Clock(
                    font="Inconsolata for powerline",
                    foreground=colors['active'],
                    background=colors['color2'],
                    fontsize=14,
                    format='%H:%M'
                ),

                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color2'],
                    foreground=colors['color3'],
                ),

                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors['color3'],
                ),
            ]
secondary_widgets = [
                widget.GroupBox(
                    font="Ubuntu Nerd Font",
                    fontsize=16,
                    margin_y=3,
                    margin_x=6,
                    padding_y=7,
                    padding_x=6,
                    borderwidth=1,
                    active=colors['color3'],
                    inactive=colors['color2'],
                    rounded=True,
                    highlight_color=colors['active'],
                    highlight_method="block",
                    this_current_screen_border=colors['color2'],
                    block_highlight_text_color=colors['color5'],
                ),

                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['black'],
                    foreground=colors['color2'],
                ),

                widget.WindowName(
                    background=colors['color2'],
                        ),

                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color2'],
                    foreground=colors['black'],
                ),


                widget.Spacer(),

               widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['black'],
                    foreground=colors['color5'],
                ),

                widget.TextBox(
                    text="蓼",
                    background=colors['color2'],
                    foreground=colors['active'],
                    fontsize=16,
                ),

                widget.Volume(
                    background=colors['color2'],
                    foreground=colors['active'],
                    font="Inconsolata for powerline",
                    fontsize=14,
                    mouse_callbacks={'Button3': lambda: qtile.cmd_spawn("alacritty -e pulsemixer")},
                ),

                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color2'],
                    foreground=colors['color3'],
                ),

                widget.TextBox(
                    text=' ',
                    font="Ubuntu Nerd Font",
                    fontsize='15',
                    padding=0,
                    background=colors['color3'],
                    foreground=colors['active'],
                ),

                widget.Clock(
                    font="Inconsolata for powerline",
                    foreground=colors['active'],
                    background=colors['color3'],
                    fontsize=14,
                    format='%a, %m/%d',
                    ),

                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors['color3'],
                ),

                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color3'],
                    foreground=colors['color2'],
                ),

                widget.TextBox(
                    text=' ',
                    font="Inconsolata for powerline",
                    fontsize='18',
                    padding=0,
                    background=colors['color2'],
                    foreground=colors['active'],
                ),

                widget.Clock(
                    font="Inconsolata for powerline",
                    foreground=colors['active'],
                    background=colors['color2'],
                    fontsize=14,
                    format='%H:%M'
                ),

                widget.TextBox(
                    text='\ue0be',
                    font="Inconsolata for powerline",
                    fontsize='33',
                    padding=0,
                    background=colors['color2'],
                    foreground=colors['color3'],
                ),

                widget.Sep(
                    padding=6,
                    linewidth=0,
                    background=colors['color3'],
                ),
            ]
