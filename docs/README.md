<div align="center"><table style="width:100%;height:auto">
<tr><td align="center">
<a title="ZI" target="_self" href="https://github.com/z-shell/zi/">
<h2><img align="center" style="width:60px;height:auto" src="https://github.com/z-shell/zi/raw/main/docs/images/logo.svg" alt="ZI Logo" /></a>
❮ ZI ❯ Package - Zsh </h2><h3> Builds and installs the newest Zsh (HEAD of the Git repository).</h3>
</td></tr>
<tr><td align="center"><h3>
  
| **Package source:** | Source Tarball | Binary |             Git              | Node | Gem |
| :-----------------: | :------------: | :----: | :--------------------------: | :--: | :-: |
|     **Status:**     |      :x:       |  :x:   | :heavy_check_mark: (default) | :x:  | :x: |

</h3>

</h3>
  <img style="width:90%;height:auto" 
       src="https://user-images.githubusercontent.com/59910950/161060980-8bc70578-e086-4a51-8cd4-ed3d7289f216.gif" alt="Preview" />
</td></tr></table></div>
  
## Available `pack''` invocations

```shell
# Install the newest zsh
zi pack for zsh

# Install the selected zsh version
zi pack"5.8.1" for zsh
zi pack"5.8" for zsh
zi pack"5.7.1" for zsh
zi pack"5.6.2" for zsh
zi pack"5.5.1" for zsh
zi pack"5.4.2" for zsh
zi pack"5.3.1" for zsh
zi pack"5.2.4" for zsh
zi pack"5.1.1" for zsh
```

### Default Profile

The ZI command that'll be run will be equivalent to:

```shell
zi ice as"null" lucid atclone'./.preconfig; print -P %F{208}Building \
        Zsh...%f; CPPFLAGS="-I/usr/include -I/usr/local/include" CFLAGS="-g \
        -O2 -Wall" LDFLAGS="-L/usr/libs -L/usr/local/libs" ./configure \
        --prefix="$ZPFX" >/dev/null && make install.bin install.fns \
        install.modules >/dev/null && sudo rm -f /bin/zsh && sudo cp -vf \
        Src/zsh /bin/zsh && print -P %F{208}The build succeeded.%f || print \
        -P %F{160}The build failed.%f'
    atpull"%atclone" nocompile countdown git for \
        zsh-users/zsh
```

It copies the zsh binary onto `/bin/zsh`.

### ZI Completions Control

Package: [system-completions](https://github.com/z-shell/system-completions)
> Moves the stock Zsh completions under the control of ZI (optional)

```shell
zi pack for system-completions

# Utilize Turbo
zi wait pack for system-completions

# Utilize Turbo and initialize the completion system
zi wait pack atload=+"zicompinit; zicdreplay" for system-completions
```

> Selectively enable and disable the completions with `cenable` and `cdisable`.

---

> This repository compatible with [ZI](https://github.com/z-shell/zi)

The [zsh-users/zsh](https://github.com/zsh-users/zsh) zsh package that can use the NPM package registry to automatically:

- get the plugin's Git repository OR release-package URL,
- get the list of the recommended ices for the plugin,
  - there can be multiple lists of ices,
  - the ice lists are stored in _profiles_; there's at least one profile, _default_,
  - the ices can be selectively overridden.
