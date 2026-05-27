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

### System installation (opt-in)

By default the package builds Zsh into `$ZPFX` and does **not** touch the system
shell. To also replace `/bin/zsh`, set `ZSH_INSTALL_SYSTEM=1` when installing.
The original is backed up to `/bin/zsh.bkp`; if that backup already exists,
the system replacement step fails instead of overwriting it:

```shell
ZSH_INSTALL_SYSTEM=1 zi pack for zsh
```

### Default Profile

The ZI command that runs for the default profile is generated from `scripts/build-manifest.py` and mirrored in `package.json`.

In short, the default profile:

- runs `./.preconfig`, then `./configure --prefix="$ZPFX"`
- uses `LDFLAGS="-L/usr/lib -L/usr/local/lib"`
- runs `make install` when `yodl` is available, otherwise falls back to `make install.bin install.fns install.modules`
- installs into `$ZPFX` by default
- copies the built shell to `/bin/zsh` only when `ZSH_INSTALL_SYSTEM=1` is set and `/bin/zsh.bkp` does not already exist

By default it never replaces `/bin/zsh`. System replacement requires:

```shell
ZSH_INSTALL_SYSTEM=1 zi pack for zsh
```

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
