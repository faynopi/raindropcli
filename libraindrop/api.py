# This file is part of Unofficial raindrop.io cli project.
# Repo: https://github.com/itsnexn/raindropcli
# Licensed under MIT (https://opensource.org/licenses/MIT)

import requests
from .utils import eprint, checkUrl
from rich import print


def getAllCollections(token: str) -> dict:
    """Get all the collections in raindrop.io

    @params:
        *token: str
            the user api token.
    """
    headers = {
        "Authorization": f"Bearer {token}"
    }
    r = requests.get("https://api.raindrop.io/rest/v1/collections",
                     headers=headers)

    try:
        if j := r.json():
            if j["result"]:
                return j["items"]
    except Exception as e:
        eprint(f"while sending request. {e}")
        exit(0)

    return {}


def getCollectionWithId(token: str, id: int) -> dict:
    """Get all the raindrops in the given collection

    @params:
        *token: str
            the user api token.
        *id: int
            collection id.
    """
    headers = {
        "Authorization": f"Bearer {token}"
    }
    r = requests.get(f"https://api.raindrop.io/rest/v1/raindrops/{id}",
                     headers=headers)
    try:
        if j := r.json():
            if j["result"]:
                return j["items"]
    except Exception as e:
        eprint(f"while sending request. {e}")
        exit(0)

    return {}


def createRaindrop(token: str, title: str, link: str,
                   collection_id: int | None, tags: str | None,
                   fav: bool) -> dict:
    """Create new raindrop

    @params:
        *token: str
            the user api token.
        *title: str|
            raindrop title.
        *link:  str
            raindrop link.
        collection_id: int | None
            id of collection you want to add this raindrop.
        tags: str | None
            list of comma separated tags.
        fav: bool
            add to favorite?
    """

    checkUrl(link)

    headers = {
        "Authorization": f"Bearer {token}"
    }
    data = {
        "title": title,
        "link": link,
        "tags": ([i.strip() for i in tags.split(",")] if tags else []),
        "important": fav,
    }

    if type(collection_id) is int:
        # Check if its valid!
        cols = getAllCollections(token)
        print([i["_id"] for i in cols])
        if collection_id in [i["_id"] for i in cols]:
            data["collection"] = {"$id": collection_id}
        else:
            eprint("{collection_id} is not a valid id."
                   "skipping the collection_id part.")

    r = requests.post("https://api.raindrop.io/rest/v1/raindrop",
                      headers=headers, json=data)
    try:
        if j := r.json():
            if j["result"]:
                print("[green bold]Successfully Created.[/green bold]")
            else:
                raise Exception(j)
    except Exception as e:
        eprint(f"while sending request. {e}")

    return {}
