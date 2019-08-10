# iterm2-container-counter
iTerm2 component for status bar which shows number of docker containers.  

![](imgs/statusbar.png)  

🐳 -> Running Container  
⚫ -> Stopped Container  

## Prerequisites

- iTerm2 (>=3.3) 
- Docker Desktop for Mac

## Install

### Clone this Repository

```
$ git clone git@github.com:koh-sh/iterm2-container-counter.git
```

### Create Directory for Auto Launch

```
$ mkdir -p ~/Library/ApplicationSupport/iTerm2/Scripts/AutoLaunch
```

### Manually create new python script

Scripts -> Manage -> New Python Script -> Full Environment -> Long-Running Daemon  
Save as "container-counter" under ` ~/Library/ApplicationSupport/iTerm2/Scripts/AutoLaunch`  

\* Enable Python API and install iTerm2's Python Runtime if requested.  

### Replace example script.  

```
$ rm ~/Library/ApplicationSupport/iTerm2/Scripts/AutoLaunch/container-counter/container-counter/container-counter.py
$ ln -s /path/to/iterm2-container-counter/container-counter.py ~/Library/ApplicationSupport/iTerm2/Scripts/AutoLaunch/container-counter/container-counter/container-counter.py
```

### Install dependency

Scripts -> Manage -> Manage Dependencies...  
Choose `AutoLaunch/container-counter` and press `Add`  
Type `docker` then install.

### Relaunch iTerm2

Quit iTerm2 and relaunch.  
If anything went wrong, see error messages.  

## Set to Status Bar

Preference -> Profiles -> Session -> Configure Status Bar  
Drag `[Container Counter]` to Active Components
