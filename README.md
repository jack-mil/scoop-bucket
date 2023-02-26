# Personal Scoop Bucket #

This repo contains [scoop](https://scoop.sh/) manifests that I made or updated that have yet to be merged in the default `main` or `extras` scoop buckets.

## Applications ##
- [KiCAD](https://kicad.org/) Open-Source PCB Design software.
  - Version 7.0.0 broke the old manifest on the `extras` bucket. Changes being tracked in Issue [#10537](https://github.com/ScoopInstaller/Extras/issues/10573). Available here in the mean time.
- [SoundSwitch](https://github.com/Belphemur/SoundSwitch) Windows Audio output source manager
  - Current Manifest in the `extras` bucket does not automatically update properly.
  - Issue and PR to `extras` tracked in Issue [#10623](https://github.com/ScoopInstaller/Extras/issues/10623). Available here in the mean time.
## Deprecated
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
