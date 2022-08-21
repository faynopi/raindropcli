# Raindropcli
_Unofficial raindrop.io command-line interface_

![](https://img.shields.io/github/issues/itsnexn/raindropcli?style=flat-square)
![](https://img.shields.io/github/license/itsnexn/raindropcli?style=flat-square)
![](https://img.shields.io/github/last-commit/itsnexn/raindropcli?style=flat-square)

```
usage: raindropcli.py [-h] [-v] {show,list,create} ...

Unofficial raindrop.io cli.

positional arguments:
  {show,list,create}  Modes
    show              show the collection with id.
      -r, --raw          Print list in grepable format.
      -s SEP, --sep SEP  Raw format separator. (default = ','. If the raw flag is not set, this value is ignored.)

    list              List all the collections
      -r, --raw          Print list in grepable format.
      -s SEP, --sep SEP  Raw format separator. (default = ','. If the raw flag is not set, this value is ignored.)

    create            List all the collections
      -t TITLE, --title TITLE
                            Raindrop title.
      -l LINK, --link LINK  Raindrop link.
      -T TAGS, --tags TAGS  Raindrop tags. (comma separated)
      -c id, --collection_id id
                            collection_id
      -f, --favorite        Mark as favorite?

options:
  -h, --help          show this help message and exit
  -v, --version
```

## Installation

you can either install the raindropcli using:
```
$ ./setup.py install
$ raindropcli
```
or you can use it as it is.
```
$ pip install -r requirements.txt
$ python3 raindropcli.py
```

This script's primary objective is to integrate with other scripts.
show and list methods has `-r, --raw` and `-s, --sep` option wich you
can help you to achive this goal.

## TODO

- [ ] Support for child collections
- [ ] Update existing raindrop
- [ ] Remove raindrops using their id
- [ ] Add asciinema to the README

## License

The files and scripts in this repository are licensed under the MIT License, which
is a very permissive license allowing you to use, modify, copy, distribute, sell,
give away, etc. the software. In other words, do what you want with it. The only
requirement with the MIT License is that the license and copyright notice must be
provided with the software.

#### [License link](./LICENSE.txt)

> _Written by Itsnexn with <3_
