<table align="center"><tr><td>
<h1 align="center">
  <p><a target="_self" href="https://github.com/z-shell/zi/">
    <img align="center" src="https://github.com/z-shell/zi/raw/main/docs/images/logo.svg" alt="ZI Logo" width="60px" height="60px" /></a>
    ❮ ZI ❯ Package - Zsh </p></h1>
<h2 align="center">
  <p> Builds and installs the newest/selected zsh version </p>    
</h2>
<h3 align="center">
<table>
    <tr>
        <td><b>Package source:</b></td>
        <td>Source Tarball</td>
        <td>Binary</td>
        <td>Git</td>
        <td>Node</td>
        <td>Gem</td>
    </tr>
    <tr>
        <td><b>Status:</b></td>
        <td>❌</td>
        <td>❌</td>
        <td>✔️ (default)</td>
        <td>❌</td>
        <td>❌</td>
    </tr>
</table></h3>
  <p><img align="center" src="https://user-images.githubusercontent.com/59910950/172880190-adea01ea-d389-4644-8dff-ef6f6185f203.png" width="100%" height="auto" alt="zi package zsh" /></p></td></tr></table><hr />

## Available `pack''` invocations

```shell
# Install the newest zsh
zi pack for zsh

# Install the selected zsh version
zi pack"5.9" for zsh
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
  -O2 -Wall" LDFLAGS="-L/usr/libs -L/usr/local/libs" \
  ./configure --prefix="$ZPFX" --enable-shared >/dev/null && make install.bin install.fns \
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

The [zsh-users/zsh](https://github.com/zsh-users/zsh) zsh package that uses the [zsh-string-lib](https://github.com/z-shell/zsh-string-lib) to automatically:

- get the plugin's Git repository OR release-package URL,
- get the list of the recommended ices for the plugin,
  - there can be multiple lists of ices,
  - the ice lists are stored in _profiles_; there's at least one profile, _default_,
  - the ices can be selectively overridden.
