# Personal Scoop Bucket #

This repo contains [scoop](https://scoop.sh/) manifests that I made or updated that have yet to be merged in the default `main` or `extras` scoop buckets.

## Applications ##
- [mpv-git](https://mpv.io/) Almost the same as `extras/mpv-git` but without the persist local config (personal preference, because reasons) and use the Github Releases instead of Sourceforge. Daily builds by (~~some guy~~) [shinchiro](https://github.com/shinchiro/mpv-winbuild-cmake). Endorsed by MPV.io (?)

## Available in `main` or `extras` official buckets
- [KiCAD](https://kicad.org/) Open-Source PCB Design software.
  - Version 7.0.0 onwards available after Issue [#10537](https://github.com/ScoopInstaller/Extras/issues/10573).
- [SoundSwitch](https://github.com/Belphemur/SoundSwitch) Windows Audio output source manager
  - Issue and PR to `extras` tracked in Issue [#10623](https://github.com/ScoopInstaller/Extras/issues/10623). Merged and working
- [Windows Terminal Preview](https://github.com/microsoft/terminal/)
  - Now available on the `versions` bucket. But, installer does not work well with Scoop, Windows store version generally recommended.
- [AltSnap](https://github.com/RamonUnch/AltSnap)
  - Altsnap was merged to the [`extras`](https://github.com/ScoopInstaller/Extras) bucket and is kept up to date.

Don't know what scoop is? Check out
[Scoop](https://scoop.sh/) installation.

### Using the bucket
```shell
scoop bucket add jack-mil https://github.com/jack-mil/scoop-bucket.git
scoop install kicad
```
