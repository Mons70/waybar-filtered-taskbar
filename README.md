# waybar-filtered-taskbar
Alternative to wlr/taskbar showing only the windows open in their respective workspaces


## Dependencies
The only dependency is i3ipc-python:
```
pip install i3ipc
```

## Installation

### Clone repo
Git clone this repo into your ```~/.config/waybar/```
This repo includes a pretty plain waybar config and style. If you're just interested in the module, you'll only need the scripts in ```/scripts/``` .
So ```~/.config/waybar/``` should only contain ```/scripts/taskbar.*``` & ```defconf``` where defconf is your config containing all the other modules you want to use in you waybar.
There are some limitations to this if you don't want do change any source code, currently the module is configured for being placed in ```center-modules``` and alone. 

So you should remove the ```"center-modules": ["module1", ..., "module2"]``` from you ```defconf```. However if you want the module placed to the left or right side of the bar, you'll just have to change ```"center-modules"``` in ```/scripts/taskbar.sh``` to either left or right (Then you should probably remove left or right modules from your ```defconf```). If you want to have other modules in the same container as the taskbar, you'll have to edit the ```/scripts/taskbar.sh``` again, and add the modules to the modules array there.

### Back up/Move your waybar config
your ```~/.config/waybar/config``` needs to be moved to ```~/.config/waybar/defconf```, as the module will overwrite the normal config file and look for your specifi config in ```defconf```. To understand why see [Implementation]

### Make scripts executable
Make the scripts in /scripts/ executable by doing
```
chmod +x ~/.config/waybar/scripts/taskbar.py
chmod +x ~/.config/waybar/scripts/taskbar.sh
```
You probably need to edit the first line in taskbar.py to point to your own python environment with i3ipc-python installed.

### Update .bashrc/.zshrc
you need to include this in your .bashrc/.zshrc for the module to configure itself properly
```
exec_always{
  ~/.config/waybar/scripts/taskbar.sh
}


Then you should be ready to go!!

## TODO
- Finish README.md
- Add more unicode app icons for default use
- Add trigger for auto reload/reconfiguration if a new output is added/removed
- Implement svg parsing from icon library/directory (if possible)
