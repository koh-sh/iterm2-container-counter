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

### Run install script

```
./install.sh
```

install.sh creates symbolic link for the script.

### Relaunch iTerm2

Quit iTerm2 and relaunch.  
If anything went wrong, see error messages.  

## Set to Status Bar

Preference -> Profiles -> Session -> Configure Status Bar  
Drag `[Container Counter]` to Active Components
