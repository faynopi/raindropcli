# This file is part of Unofficial raindrop.io cli project.
# Repo: https://github.com/itsnexn/raindropcli
# Licensed under MIT (https://opensource.org/licenses/MIT)

from os import path, environ
from pathlib import Path
from re import search
import toml


XDG_CONFIG_DIR = environ.get("XDG_CONFIG_DIR")
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
        print("config file doesnt exists!")
        print("https://github.com/itsnexn/raindropcli#installation")
        exit(1)

    data = toml.load(conf_dir)

    if not data["token"]:
        print("Error: empty token ! Aborting.")
        print("https://github.com/itsnexn/raindropcli#installation")
        exit(1)

    if not search(r"^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$",
            data["token"]):
        print("Error: invalid token! Aborting")
        print("https://github.com/itsnexn/raindropcli#installation")

    return {
        "token": data["token"]
    }
