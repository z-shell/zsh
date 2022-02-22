<h2 align="center">
  <a href="https://github.com/z-shell/zi">
    <img src="https://github.com/z-shell/zi/raw/main/docs/images/logo.svg" alt="Logo" width="80" height="80" />
  </a>
❮ ZI ❯ Package - Zsh
</h2>

<h3 align="center">

| **Package source:** | Source Tarball | Binary |             Git              | Node | Gem |
| :-----------------: | :------------: | :----: | :--------------------------: | :--: | :-: |
|     **Status:**     |      :x:       |  :x:   | :heavy_check_mark: (default) | :x:  | :x: |

</h3>

- [Available `pack''` invocations](#available-pack-invocations)
- [Default Profile](#default-profile)

> This repository compatible with [ZI](https://github.com/z-shell/zi)

The [zsh-users/zsh](https://github.com/zsh-users/zsh) zsh package that can use the NPM package registry to automatically:

- get the plugin's Git repository OR release-package URL,
- get the list of the recommended ices for the plugin,
  - there can be multiple lists of ices,
  - the ice lists are stored in _profiles_; there's at least one profile, _default_,
  - the ices can be selectively overridden.

### Available `pack''` invocations

[zsh-users/zsh](https://github.com/zsh-users/zsh) either from the release archive or from Git repository:

```zsh
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

Builds and installs the newest Zsh (HEAD of the Git repository).

The ZI command that'll be run will be equivalent to:

```zsh
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
