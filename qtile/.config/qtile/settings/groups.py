# Qtile workspaces

from libqtile.config import Key, Group, Match
from libqtile.command import lazy
from settings.keys import mod, keys
from libqtile import hook

# When application launched automatically focus it's group
@hook.subscribe.client_new
def modify_window(client):
    for group in groups:  # follow on auto-move
        match = next((m for m in group.matches if m.compare(client)), None)
        if match:
            targetgroup = client.qtile.groups_map[group.name]  # there can be multiple instances of a group
            targetgroup.cmd_toscreen(toggle=False)
            break

# Hook to fallback to the first group with windows when last window of group is killed
@hook.subscribe.client_killed
def fallback(window):
    if window.group.windows != [window]:
        return
    idx = qtile.groups.index(window.group)
    for group in qtile.groups[idx - 1::-1]:
        if group.windows:
            qtile.current_screen.toggle_group(group)
            return
    qtile.current_screen.toggle_group(qtile.groups[0])

# Groups with matches

workspaces = [
    {"name": " ₁", "key": "1", "matches": [Match(wm_class='firefox')], "layout": "monadtall"},
    {"name": " ₂", "key": "2", "matches": [Match(wm_class='alacritty'), Match(wm_class='ranger')], "layout": "monadtall"},
    {"name": " ₃", "key": "3", "matches": [Match(wm_class='vim'), Match(wm_class='code-oss')], "layout": "monadtall"},
    {"name": " ₄", "key": "4", "matches": [Match(wm_class='Microsoft Teams - Preview')], "layout": "monadtall"},
    {"name": " ₅", "key": "5", "matches": [Match(wm_class='gimp-2.10')], "layout": "monadtall"},
    {"name": "阮₆", "key": "6", "matches": [Match(wm_class='spotify')], "layout": "monadtall"},
    {"name": " ₇", "key": "7", "matches": [Match(wm_class='org.remmina.remmina')], "layout": "monadtall"},
    {"name": " ₈", "key": "8", "matches": [Match(wm_class='lens')], "layout": "monadtall"},
    {"name": " ₉", "key": "9", "matches": [Match(wm_class='neomutt')], "layout": "monadtall"},
]

groups = []
for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    layouts = workspace["layout"] if "layout" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout=layouts))
    keys.append(Key([mod], workspace["key"], lazy.group[workspace["name"]].toscreen()))
    keys.append(Key([mod, "shift"], workspace["key"], lazy.window.togroup(workspace["name"])))
