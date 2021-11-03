# zsh-users/zsh as a Zsh package

##### Homepage link: [zsh-users/zsh](https://github.com/zsh-users/zsh)

| **Package source:** | Source Tarball | Binary | Git | Node | Gem |
|:-------------------:|:--------------:|:------:|:---:|:----:|:---:|
| **Status:**         |        -       |   -    | + <br> (default) | - | - |

[Zinit](https://github.com/zdharma/zinit) can use `package.json` to
automatically:

- get the plugin's Git repository OR release-package URL,
- get the list of the recommended ices for the plugin,
    - there can be multiple lists of ices,
    - the ice lists are stored in *profiles*; there's at least one profile, *default*,
    - the ices can be selectively overriden.

Example invocations that'll install
[zsh-users/zsh](https://github.com/zsh-users/zsh) either from the release archive
or from Git repository:

```zsh
# Install the newest zsh
zinit pack for zsh

# Install the selected zsh version
zinit pack"5.7.1" for zsh
zinit pack"5.6.2" for zsh
zinit pack"5.5.1" for zsh
zinit pack"5.4.2" for zsh
zinit pack"5.3.1" for zsh
zinit pack"5.2.4" for zsh
zinit pack"5.1.1" for zsh
zinit pack"5.8" for zsh
```

## Default Profile

Builds and installs the newest Zsh (HEAD of the Git repository).

The Zinit command that'll be run will be equivalent to:

```zsh
zinit ice as"null" lucid atclone'./.preconfig; print -P %F{208}Building \
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

<!-- vim:set ft=markdown tw=80 fo+=an1 autoindent: -->
