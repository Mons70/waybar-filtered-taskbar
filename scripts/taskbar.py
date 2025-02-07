#!/home/mons/.config/waybar/scripts/waybar_venv/bin/python

import i3ipc
import sys

def get_outputs(conn):
    ws_outputs = {}
    

def get_ws_windows(conn):
    window_dict = {}
    for workspace in conn.get_tree().workspaces():
        window_dict[workspace.name] = []
        for window in workspace.leaves():
            focused = False
            if window.app_id == None:
                window_dict[workspace.name].append([window.window_class, window.focused])
            else:
                window_dict[workspace.name].append([window.app_id, window.focused])
    return window_dict

def get_workspace(conn, output):
    outputs = conn.get_outputs()
    for op in outputs:
        if op.name == output:
            return op.current_workspace
    return None

def get_icons(windows):
    icons = {
        "firefox": "",
        "com.mitchellh.ghostty": "",
        "spotify": "",
        "code": "󰨞" 
    }

    iconized_windows = []
    for window in windows:
        if window[1]:
            iconized_windows.append(f"<span color='#3987a8'>{icons[str.lower(window[0])]}</span>")
        else:
            iconized_windows.append(icons[str.lower(window[0])])
    return iconized_windows

def waybar_json_string(windows):
    string = ' '.join(str(x) for x in windows)
    return f'{{"text": "{string}"}}'



def main(output):
    conn = i3ipc.Connection()
    while True:
        window_dict = get_ws_windows(conn)
        current_ws = get_workspace(conn, output)
        current_windows = get_icons(window_dict[current_ws])
        print(waybar_json_string(current_windows))

# Detect monitor name dynamically from Waybar argument
if len(sys.argv) > 1:
    monitor_name = sys.argv[1]  # Get monitor name from Waybar config
else:
    print({"text": "Monitor not specified"})
    sys.exit(1)     
    
main(monitor_name)