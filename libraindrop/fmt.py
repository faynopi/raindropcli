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
        if i and ({"title", "creatorRef", "count", "_id"} <= i.keys()):
            print(sep.join([i.get("title"), i.get("creatorRef")["name"],
                str(i.get("count")), str(i.get("_id"))]))


def P_ColLsPretty(secret: str):
    col = getAllCollections(secret)
    t = Table()
    t.add_column("Name")
    t.add_column("Count")
    t.add_column("Id")

    for i in col:
        if i and ({"title", "count", "_id"} <= i.keys()):
            t.add_row(i.get("title"), str(i.get("count")), str(i.get("_id")))

    c = Console()
    c.print(t)

def P_ColShowRaw(secret: str, sep: str, id: int):
    col = getCollectionWithId(secret, id)
    print(sep.join(["type", "title", "fav", "tags", "link", "id"]))
    for i in col:
        if i and {"title", "type", "_id", "tags", "link"} <= i.keys():
            print(sep.join([i.get("type"), i.get("title"),
                ("true" if i.get("important") else "false"),
                    "#".join(i.get("tags")),
                    i.get("link"),
                    str(i.get("_id"))]))

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
        if i and {"title", "type", "_id", "tags", "link"} <= i.keys():
            t.add_row(i.get("type"), i.get("title"), (" +" if i.get("important") else " -"),
                    ",".join(i.get("tags") if i.get("tags") else []),
                    i.get("link"), str(i.get("_id")))
    c = Console()
    c.print(t)
