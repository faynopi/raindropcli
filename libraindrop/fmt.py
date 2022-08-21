# This file is part of Unofficial raindrop.io cli project.
# Repo: https://github.com/itsnexn/raindropcli
# Licensed under MIT (https://opensource.org/licenses/MIT)

from rich.table import Table
from rich.console import Console
from .api import getAllCollections, getCollectionWithId

def P_ColLsRaw(secret: str, sep: str):
    col = getAllCollections(secret)
    print(sep.join(["title", "creator", "count", "id"]))
    for i in col:
        if i and ("title", "creatorRef", "count", "_id" in i):
            print(sep.join([i["title"], i["creatorRef"]["name"], str(i["count"]), str(i["_id"])]))


def P_ColLsPretty(secret: str):
    col = getAllCollections(secret)
    t = Table()
    t.add_column("Name")
    t.add_column("Count")
    t.add_column("Id")

    for i in col:
        if i and ("title", "count", "_id" in i):
            t.add_row(i["title"], str(i["count"]), str(i["_id"]))

    c = Console()
    c.print(t)

def P_ColShowRaw(secret: str, sep: str, id: int):
    col = getCollectionWithId(secret, id)
    for i in col:
        if i and ("title", "type", "important", "_id", "tags", "link" in i):
            print(sep.join([i["type"], i["title"], (" +" if i["important"] else " -"),
                    "#".join(i["tags"]),
                    i["link"],
                    str(i["_id"])]))

def P_ColShowPretty(secret: str, id: int):
    col = getCollectionWithId(secret, id)
    t = Table(title=str(id))
    t.add_column("Type")
    t.add_column("Name")
    t.add_column("Fav")
    t.add_column("Tags")
    t.add_column("URL")
    t.add_column("Id")
    for i in col:
        if i and ("title", "type", "important", "_id", "tags", "link" in i):
            t.add_row(i["type"], i["title"], (" +" if i["important"] else " -"),
                    ",".join(i["tags"]),
                    i["link"],
                    str(i["_id"]))
    c = Console()
    c.print(t)
