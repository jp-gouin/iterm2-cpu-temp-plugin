# iterm2-cpu-temp-plugin
Display cpu temperature in the status bar of iTerm2

## Based on [smctemp](https://github.com/narugit/smctemp)

# How to Install

1. Install smctemp
```console
$ git clone https://github.com/narugit/smctemp
$ cd smctemp
$ sudo make install
$ smctemp -c
```
2. Clone this repository
3. Enable Python API in iTerm2. Go to Preferences > General > Magic > Enable Python Api
4. Create Folder AutoLaunch `mkdir ~/Library/Application\ Support/iTerm2/Scripts/AutoLaunch`
5. You’ll need to place the script in ~/Library/Application Support/iTerm2/Scripts/AutoLaunch. 
6. Then manually launch it or restart the app.
7. Then, navigate to Preferences > Profiles > Session. Turn on Status Bar Enabled and select Configure Status Bar. Drag the 🌡x°C component into the bottom section

# Customisation

None yet
