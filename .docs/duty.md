---
title: DUTY
hide:
    - navigation
---

#

For using predefined task please install package

```py
pip3 install skyant-tools
```

then make a file ```duties.py``` in root of your project

```py linenums='1' title='duties.py'
# pylint: disable=W0401,W0614,C0114

from skyant.tools.duty.general import *  # noqa=F403
from skyant.tools.duty.venv import *  # noqa=F403
from skyant.tools.duty.pypi import *  # noqa=F403
```

It's all. You can use our predefined tasks & add yours. For getting a list of an available
tasks please run

=== "command"
    ```bash
    duty -l
    ```

=== "result"
    ```bash
    activate              Activate environment from .venv/{name}. Default name=dev. You can use "duty activate name"
    freeze                Freeze current environment to .venv/{name}.req. Default name=dev. You can use "duty freeze name"
    init                  Initialize environment in .venv/{name}. Default name=dev. You can use "duty init name"
    install               Install the current package locality from source.
    login2gcp             Login to Google Cloud Platform.
    mkdocs                Build & Serv the [MkDocs Documentation](https://www.mkdocs.org/) on 0.0.0.0:8008.
    uninstall             Uninstalling current package from an activate environment.
    ```

## General

Contains ```mkdocs``` and ```login2gcp`` commands.

### mkdocs

Builds & serve a documentation which was made with [MkDocs](https://www.mkdocs.org/).

This command needs a ```.mkdocs.yml``` file in root of your projects and saves a static content
in .html directory.

### login2gcp

Run pipeline to login your local Google SDK. Set Application Default Credentials & Quota
projects. Provide access to Google Drive.

If environment variable GCP_PROJECT is empty send request to you for input Google Project ID.


## Venv

Tasks for manipulating a local virtual environments. Contains: ```init```, ```activate```,
```freeze```.

All commands in this module executed in directory ```.venv```.

!!!note
    All commands in this module have a parameter "name" which define a subfolder in the
    directory ```.venv``` & name of requirements file. __Default name=dev__

    For example if name is "test", then requirements file will be ".venv/test.req" and virtual
    environment folder will be ".venv/test"

    ```bash
    duty init test
    ```


!!!warning
    Please don't forget to add ```.venv/*/``` in your ```.gitignore```.


### init

Initialize virtual environment, upgrade pip, install ```wheel pylint isort ipykernel``` & 
{name}.req requirements and activating the new environment.

Also this command upgrade your {name}.req file because was be upgraded pip & installed some
default packages.


### activate

Activating a specified environment.


### freeze

Write your current environment to a {name}.req file.

!!!note
    Default value of an argument "name" is "dev", so if you run command ```duty freeze```
    in environment different than "dev" you rewrite .venv/dev.req file. In this case you
    should run ```duty freeze somename```.


## Pypi

Commands for working python packages source code.


### install

Installing current source as package in a current environment.


### uninstall
