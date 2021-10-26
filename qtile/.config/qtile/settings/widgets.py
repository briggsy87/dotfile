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

# Define functions for bar
# def taskwarrior():
# 	return (
# 		subprocess.check_output(["./.config/qtile/task_polybar.sh"])
# 		.decode("utf-8")
# 		.strip()
# 	)
# 

### Mouse_callback functions
# def open_launcher():
# 	qtile.cmd_spawn("./.config/rofi/launchers/colorful/launcher.sh")
# 
# 
# def finish_task():
# 	qtile.cmd_spawn('task "$((`cat /tmp/tw_polybar_id`))" done')
# 
# 
# def kill_window():
# 	qtile.cmd_spawn("xdotool getwindowfocus windowkill")
# 
# 
# def update():
# 	qtile.cmd_spawn(terminal + "-e yay")
# 
# 
# def open_pavu():
# 	qtile.cmd_spawn("pavucontrol")
# 
# 
# def toggle_bluetooth():
# 	qtile.cmd_spawn("./.config/qtile/system-bluetooth-bluetoothctl.sh --toggle")
# 
# 
# def open_bt_menu():
# 	qtile.cmd_spawn("blueberry")
# 
# 
# def open_connman():
# 	qtile.cmd_spawn("connman-gtk")
# 
# 
# def todays_date():
# 	qtile.cmd_spawn("./.config/qtile/calendar.sh")
# 
# 
# def open_powermenu():
# 	qtile.cmd_spawn("./.config/rofi/powermenu/powermenu.sh")


primary_widgets = [
    *workspaces(),

    separator(),

    powerline('color5', 'dark'),

    icon(bg="color5", text=' '), # Icon: nf-fa-download
    
    widget.CheckUpdates(
        background=colors['color5'],
        colour_have_updates=colors['light'],
        colour_no_updates=colors['light'],
        no_update_string='0',
        display_format='{updates}',
        update_interval=1800,
        custom_command='checkupdates',
    ),

    powerline('color4', 'color5'),

    icon(bg="color4", text=' '),  # Icon: nf-fa-feed
    
    widget.Net(**base(bg='color4'), interface='wlp58s0'),

    powerline('color3', 'color4'),

    widget.CurrentLayoutIcon(**base(bg='color3'), scale=0.65),

    widget.CurrentLayout(**base(bg='color3'), padding=5),    

    powerline('color2', 'color3'),

    icon(bg="color2", fontsize=25, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('color1', 'color2'),
 
    widget.Battery(**base(bg='color1'), format='{char} {percent:2.0%} {hour:d}:{min:02d}'),

    powerline('dark', 'color1'),

    widget.Systray(background=colors['dark'], padding=5),
]

colors2 = [
	["#2e3440", "#2e3440"],  # 0 background
	["#d8dee9", "#d8dee9"],  # 1 foreground
	["#3b4252", "#3b4252"],  # 2 background lighter
	["#bf616a", "#bf616a"],  # 3 red
	["#a3be8c", "#a3be8c"],  # 4 green
	["#ebcb8b", "#ebcb8b"],  # 5 yellow
	["#81a1c1", "#81a1c1"],  # 6 blue
	["#b48ead", "#b48ead"],  # 7 magenta
	["#88c0d0", "#88c0d0"],  # 8 cyan
	["#e5e9f0", "#e5e9f0"],  # 9 white
	["#4c566a", "#4c566a"],  # 10 grey
	["#d08770", "#d08770"],  # 11 orange
	["#8fbcbb", "#8fbcbb"],  # 12 super cyan
	["#5e81ac", "#5e81ac"],  # 13 super blue
	["#242831", "#242831"],  # 14 super dark background
]

group_box_settings = {
	"padding": 5,
	"borderwidth": 4,
	"active": colors[9],
	"inactive": colors[10],
	"disable_drag": True,
	"rounded": True,
	"highlight_color": colors[2],
	"block_highlight_text_color": colors[6],
	"highlight_method": "block",
	"this_current_screen_border": colors[14],
	"this_screen_border": colors[7],
	"other_current_screen_border": colors[14],
	"other_screen_border": colors[14],
	"foreground": colors[1],
	"background": colors[14],
	"urgent_border": colors[3],
}
# genome_widgets = [
# 	widget.TextBox(
# 		text="",
# 		foreground=colors2[13],
# 		background=colors2[0],
# 		font="Font Awesome 5 Free Solid",
# 		fontsize=28,
# 		padding=20,
# #		#mouse_callbacks={"Button1": open_launcher},
# 	),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.GroupBox(
# 				font="Font Awesome 5 Brands",
# 				visible_groups=[""],
# 				**group_box_settings,
# 			),
# 			widget.GroupBox(
# 				font="Font Awesome 5 Free Solid",
# 				visible_groups=["", "", "", "", ""],
# 				**group_box_settings,
# 			),
# 			widget.GroupBox(
# 				font="Font Awesome 5 Brands",
# 				visible_groups=[""],
# 				**group_box_settings,
# 			),
# 			widget.GroupBox(
# 				font="Font Awesome 5 Free Solid",
# 				visible_groups=["", "", ""],
# 				**group_box_settings,
# 			),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.Sep(
# 				linewidth=0,
# 				foreground=colors2[2],
# 				background=colors2[0],
# 				padding=10,
# 				size_percent=40,
# 			),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.CurrentLayoutIcon(
# 				custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
# 				foreground=colors2[2],
# 				background=colors2[14],
# 				padding=-10,
# 				scale=0.40,
# 			),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.Sep(
# 				linewidth=0,
# 				foreground=colors2[2],
# 				padding=10,
# 				size_percent=50,
# 			),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.GenPollText(
# 				func=taskwarrior,
# 				update_interval=5,
# 				foreground=colors2[11],
# 				background=colors2[14],
# 				#mouse_callbacks={"Button1": finish_task},
# 			),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.Spacer(),
# 			widget.TextBox(
# 			    text=" ",
# 			    foreground=colors2[12],
# 			    background=colors2[0],
# 			    # fontsize=38,
# 			    font="Font Awesome 5 Free Solid",
# 			),
# 			widget.WindowName(
# 			    background=colors2[0],
# 			    foreground=colors2[12],
# 			    width=bar.CALCULATED,
# 			    empty_group_string="Desktop",
# 			    max_chars=130,
# 			    #mouse_callbacks={"Button2": kill_window},
# 			),
# 			widget.Spacer(),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.Systray(icon_size=26, background=colors2[14], padding=10),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.Sep(
# 				linewidth=0,
# 				foreground=colors2[2],
# 				padding=10,
# 				size_percent=50,
# 			),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.TextBox(
# 				text=" ",
# 				foreground=colors2[8],
# 				background=colors2[14],
# 				font="Font Awesome 5 Free Solid",
# 				# fontsize=38,
# 			),
# 			widget.PulseVolume(
# 				foreground=colors2[8],
# 				background=colors2[14],
# 				limit_max_volume="True",
# 				#mouse_callbacks={"Button3": open_pavu},
# 			),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.Sep(
# 				linewidth=0,
# 				foreground=colors2[2],
# 				padding=10,
# 				size_percent=50,
# 			),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.TextBox(
# 				text=" ",
# 				font="Font Awesome 5 Free Solid",
# 				foreground=colors2[7],  # fontsize=38
# 				background=colors2[14],
# 			),
# 			widget.Wlan(
# 				interface="wlp58s0",
# 				format="{essid}",
# 				foreground=colors2[7],
# 				background=colors2[14],
# 				padding=5,
# 				mouse_callbacks={"Button1": open_connman},
# 			),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.Sep(
# 				linewidth=0,
# 				foreground=colors2[2],
# 				padding=10,
# 				size_percent=50,
# 			),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.TextBox(
# 				text=" ",
# 				font="Font Awesome 5 Free Solid",
# 				foreground=colors2[5],  # fontsize=38
# 				background=colors2[14],
# 			),
# 			widget.Clock(
# 				format="%a, %b %d",
# 				background=colors2[14],
# 				foreground=colors2[5],
# 			),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.Sep(
# 				linewidth=0,
# 				foreground=colors2[2],
# 				padding=10,
# 				size_percent=50,
# 			),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.TextBox(
# 				text=" ",
# 				font="Font Awesome 5 Free Solid",
# 				foreground=colors2[4],  # fontsize=38
# 				background=colors2[14],
# 			),
# 			widget.Clock(
# 				format="%I:%M %p",
# 				foreground=colors2[4],
# 				background=colors2[14],
# 				#    mouse_callbacks={"Button1": todays_date},
# 			),
# 			widget.TextBox(
# 				text="",
# 				foreground=colors2[14],
# 				background=colors2[0],
# 				fontsize=28,
# 				padding=0,
# 			),
# 			widget.TextBox(
# 				text="⏻",
# 				foreground=colors2[13],
# 				font="Font Awesome 5 Free Solid",
# 				fontsize=34,
# 				padding=20,
# 				#mouse_callbacks={"Button1": open_powermenu},
# 			),
# 	]
secondary_widgets = [
    *workspaces(),

    separator(),

    powerline('color1', 'dark'),

    widget.CurrentLayoutIcon(**base(bg='color1'), scale=0.65),

    widget.CurrentLayout(**base(bg='color1'), padding=5),

    powerline('color2', 'color1'),

    widget.Clock(**base(bg='color2'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'color2'),
]

widget_defaults = {
    'font': 'Mononoki Nerd Font',
    'fontsize': 12,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
