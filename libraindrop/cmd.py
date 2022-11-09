# This file is part of Unofficial raindrop.io cli project.
# Repo: https://github.com/itsnexn/raindropcli
# Licensed under MIT (https://opensource.org/licenses/MIT)

import argparse
from .fmt import P_ColLsRaw, P_ColLsPretty, P_ColShowRaw, P_ColShowPretty
from .api import createRaindrop
from .config import parseConfig


ver = """
Author : Itsnexn
Github : https://github.com/itsnexn/raindropcli
Version: 1.0.0
License: MIT (https://opensource.org/licenses/MIT)
"""


def __addRawArgs__(p: argparse.ArgumentParser):
    p.add_argument("-r", "--raw", help="Print list in grepable format.",
                   action="store_true")
    p.add_argument("-s", "--sep", default=",", type=str,
                   help="Raw format separator. (default = ','."
                        "If the raw flag is not set, this value is ignored.)")


def Exec():
    config = parseConfig()

    parser = argparse.ArgumentParser(description="Unofficial raindrop.io cli.")
    mparser = parser.add_subparsers(dest="mode", help="Modes")

    col_showp = mparser.add_parser("show", help="show the collection with id.")
    col_showp.add_argument("collection_id", help="id of Collection to show",
                           type=int)
    __addRawArgs__(col_showp)

    collsp = mparser.add_parser("list", help="List all the collections")
    __addRawArgs__(collsp)

    createp = mparser.add_parser("create", help="List all the collections")
    createp.add_argument("-t", "--title", help="Raindrop title.",
                         required=True, type=str)
    createp.add_argument("-l", "--link", help="Raindrop link.",
                         required=True, type=str)
    createp.add_argument("-T", "--tags",
                         help="Raindrop tags. (comma separated)", type=str)
    createp.add_argument("-c", "--collection_id", metavar="id",
                         help="collection_id", type=int)
    createp.add_argument("-f", "--favorite", help="Mark as favorite?",
                         action="store_true")

    parser.add_argument("-v", "--version", action="store_true")

    args = vars(parser.parse_args())

    token = config["token"]

    if args["version"]:
        print(ver)
        exit(0)
    elif args["mode"]:
        if args["mode"] == "list":
            if args["raw"]:
                P_ColLsRaw(token, args["sep"])
            else:
                P_ColLsPretty(config["token"])
        elif args["mode"] == "show":
            if args["raw"]:
                P_ColShowRaw(token, args["sep"], args["collection_id"])
            else:
                P_ColShowPretty(config["token"], args["collection_id"])
        elif args["mode"] == "create":
            createRaindrop(token, args["title"], args["link"],
                           args["collection_id"], args["tags"],
                           args["favorite"])
        else:
            parser.print_help()
            exit(1)
    else:
        parser.print_help()
        exit(1)
    exit(0)
