#!/usr/bin/env python3
"""Generate package.json (the Zi package manifest) from a single recipe template.

Why this exists: the manifest defines one Zi install profile per Zsh version, and
every profile's `atclone` build recipe is identical except for the `git checkout`
line. Hand-maintaining 11 ~600-char copies caused drift (e.g. an inconsistent
`-f /bin/zsh` guard). This script is the single source of truth: edit BUILD /
VERSIONS / METADATA here, run `python3 scripts/build-manifest.py`, and commit the
regenerated package.json.

Notes on the recipe:
- Builds into $ZPFX (the Zi prefix) via `./configure --prefix="$ZPFX"`.
- Replacing the *system* /bin/zsh is opt-in: it only happens when the installer
  sets `ZSH_INSTALL_SYSTEM` (e.g. `ZSH_INSTALL_SYSTEM=1 zi ...`). By default the
  package never touches /bin/zsh.
"""
import json
import pathlib

METADATA = {
    "name": "zsh",
    "description": "Zsh – the programmer's shell",
    "homepage": "https://github.com/zsh-users/zsh",
    "bugs": {"url": "https://github.com/zsh-users/zsh/issues"},
    "keywords": ["zpackage", "zshell", "zsh"],
}

PLUGIN_INFO = {"user": "zsh-users", "plugin": "zsh"}

# Selectable version profiles, in addition to the unpinned "default".
VERSIONS = ["5.1.1", "5.2.4", "5.3.1", "5.4.2", "5.5.1", "5.6.2",
            "5.7.1", "5.8", "5.8.1", "5.9"]

# Single source of truth for the build recipe. `{checkout}` is replaced per
# profile (empty for "default").
BUILD = (
    "{checkout}"
    "./.preconfig; m {{nl}}{{hi}}Building Zsh{{…}}; "
    "CPPFLAGS='-I/usr/include -I/usr/local/include' CFLAGS='-g -O2 -Wall' "
    "LDFLAGS='-L/usr/lib -L/usr/local/lib' "
    "./configure --prefix=\"$ZPFX\" >> /dev/null 2>&1 && "
    "{{ type yodl >> /dev/null 2>&1 || {{ m -u2 {{warn}}WARNING{{ehi}}:{{rst}}{{warn}} "
    "No {{cmd}}yodl{{warn}}, manual pages will not be built.; ((0)); }} && "
    "{{ make install; ((1)); }} || make install.bin install.fns install.modules }} "
    ">> /dev/null 2>&1 && "
    "{{ [[ -n \"$ZSH_INSTALL_SYSTEM\" ]] && type sudo >> /dev/null 2>&1 && "
    "[[ -e /bin/zsh ]] && sudo mv /bin/zsh /bin/zsh.bkp && sudo cp -vf Src/zsh /bin/zsh; "
    "((1)); }} && m {{ok}}The build succeeded. || m {{failure}}The build failed."
)


def ice(checkout: str) -> dict:
    return {
        "requires": "cc;make;cp;rm",
        "git": "",
        "lucid": "",
        "as": "null",
        "atclone": BUILD.format(checkout=checkout),
        "atpull": "%atclone",
        "nocompile": "",
        "nocompletions": "",
        "countdown": "",
    }


def main() -> None:
    ices = {"default": ice("")}
    for v in VERSIONS:
        ices[v] = ice(f"git checkout --quiet zsh-{v}; ")

    manifest = dict(METADATA)
    manifest["zsh-data"] = {"plugin-info": PLUGIN_INFO, "zi-ices": ices}

    out = pathlib.Path(__file__).resolve().parent.parent / "package.json"
    out.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"Wrote {out} with {len(ices)} profiles (default + {len(VERSIONS)} versions).")


if __name__ == "__main__":
    main()
