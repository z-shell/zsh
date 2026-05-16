# ❮ Zi ❯ Package - Zsh

Build and install the newest or a selected Zsh version with
[Zi](https://github.com/z-shell/zi).

| Package source | Source tarball | Binary | Git | Node | Gem |
| -------------- | -------------- | ------ | --- | ---- | --- |
| Status         | ❌             | ❌     | ✔️  | ❌   | ❌  |

## Install

Install the newest supported Zsh revision:

```zsh
zi pack for zsh
```

Install a selected version:

```zsh
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

## Default profile behavior

The default profile defined in `package.json`:

1. runs `./.preconfig`,
2. configures Zsh under `$ZPFX` with the package's current `CPPFLAGS`,
   `CFLAGS`, and `LDFLAGS`,
3. runs `make install` when `yodl` is available, or falls back to
   `make install.bin install.fns install.modules`,
4. if `sudo` is available and `/bin/zsh` already exists, backs it up to
   `/bin/zsh.bkp` and copies the newly built `Src/zsh` to `/bin/zsh`.

Versioned profiles first check out their matching upstream tag, then run the
same build flow.

## Zsh completions

Use the [`system-completions`](https://github.com/z-shell/system-completions)
package to move stock Zsh completions under Zi control:

```zsh
zi pack for system-completions

# Utilize Turbo
zi wait pack for system-completions

# Utilize Turbo and initialize the completion system
zi wait pack atload=+"zicompinit; zicdreplay" for system-completions
```

Selectively enable and disable completions with `cenable` and `cdisable`.

## About this package

This repository is compatible with [Zi](https://github.com/z-shell/zi).

The package targets the upstream
[`zsh-users/zsh`](https://github.com/zsh-users/zsh) repository and uses
[`zsh-string-lib`](https://github.com/z-shell/zsh-string-lib) to expose:

- the upstream Git source,
- the recommended Zi ice modifiers,
- named profiles for the supported historical versions,
- selective overrides for those profile settings.
