# Qtile config
My comfy qtile config that supports both vimkeys and arrow keys to manipulate windows.
Made with pure qtile widgets, layouts etc. without qtile-extras.

## Requirements
- MPD - without python mpd library it won't load and fallback to default config
- Rofi - launcher
- Flameshot - screenshot utility
- Kitty - my terminal of choice
- libnotify - some functions send push notifications using notify-send

# Install
After installing required and optional dependencies it just a matter of cloning the repo

``` shell
git clone https://github.com/Moskas/qtile-config ~/.config/qtile
```

> [!IMPORTANT]
> Keep in mind that current config was made purely for me, so if you want to use it check the code and modify it better suit your needs.

# My additions
Due to the fact that I'm using both laptop and desktop with the same config I had to add automatic laptop aka check if device has battery if not. 
I have created two bar configurations, one simple and second simple with minimal use of colors.
I have created a couple of colorscheme configs:
- gruvbox-dark
- gruvbox-light
- solarized-dark
- decay-dark
- kanagawa
