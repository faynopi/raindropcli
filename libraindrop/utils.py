# This file is part of Unofficial raindrop.io cli project.
# Repo: https://github.com/itsnexn/raindropcli
# Licensed under MIT (https://opensource.org/licenses/MIT)

import sys
from rich import print
from re import search


URL_REGEX = r"^https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)$"

def eprint(*args, **kwargs):
    print("[black bold on red][italic] Error [/italic][/black bold on red]", *args, file=sys.stderr, **kwargs)

def checkUrl(link: str):
    if not search(URL_REGEX, link):
        eprint("Please enter valid url!")
        exit(1)


