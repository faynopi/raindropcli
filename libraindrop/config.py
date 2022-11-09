# This file is part of Unofficial raindrop.io cli project.
# Repo: https://github.com/itsnexn/raindropcli
# Licensed under MIT (https://opensource.org/licenses/MIT)

from os import path, environ
from pathlib import Path
from re import search
import toml
from .utils import eprint


XDG_CONFIG_DIR = environ.get("XDG_CONFIG_HOME")
HOMEDIR = Path.home()

def getConfigDir() -> str | None:
    if XDG_CONFIG_DIR:
        p = path.join(XDG_CONFIG_DIR, "raindropcli.conf")
        if path.exists(p):
            return p
    if HOMEDIR:
        p = path.join(HOMEDIR, ".raindropcli.conf")
        if path.exists(p):
            return p
    return None


def parseConfig() -> dict:
    conf_dir = getConfigDir()
    if not conf_dir:
        eprint("config file doesnt exists!")
        eprint("https://github.com/itsnexn/raindropcli#configuration")
        exit(1)

    data = toml.load(conf_dir)

    if not data["token"]:
        eprint("Error: empty token ! Aborting.")
        eprint("https://github.com/itsnexn/raindropcli#configuration")
        exit(1)

    if not search(r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$",
            data["token"]):
        eprint("Error: invalid token! Aborting")
        eprint("https://github.com/itsnexn/raindropcli#configuration")
        exit(1)

    return {
        "token": data["token"]
    }
