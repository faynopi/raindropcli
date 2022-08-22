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

This script's primary objective is to integrate with other scripts.
show and list methods has `-r, --raw` and `-s, --sep` option wich you
can help you to achive this goal.

## Installation
**NOTE:** Before you run the program make sure you create [configuration](#configuration) file.

you can either install the raindropcli using:
```
$ pip install git+https://github.com/itsnexn/raindropcli.git@master
```
or you can clone it and use it as it is.
```
$ git clone https://github.com/itsnexn/raindropcli.git
$ cd raindropcli
$ pip install -r requirements.txt
$ python3 raindropcli.py
```

## Configuration

Make sure you create a configuration file under `$HOME/.raindropcli.conf`
or `$XDG_CONFIG_HOME/raindropcli.conf`.

go to [Settings > Integration](https://app.raindrop.io/settings/integrations).
Click on the "Create new app" you may name it whatever you want but I
recommend "raindropcli". following the creation of your new app, click
on it to generate a new test token which you should include in your
configuration file.

Your configuration file should look something like this:
```
# vim: syntax=toml
token = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
```
you don't actually need the vim command. its just for syntax highlighting
for vim.

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
