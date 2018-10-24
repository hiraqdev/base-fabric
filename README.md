# base-fabric
Skeleton for python fabric

Dependencies:

- Programming Language: Python >= 3.7.x
- Automate Tools: [Fabric 2.4](http://docs.fabfile.org/en/2.4/index.html)
- Package Manager: [Pipenv](http://pipenv.org/)

```
OBJECTIVE

Provide basic skeleton to working using Fabric. What is Fabric ? Fabric is just
like Ansible but more simpler. We can manage our automation flows with just simple
python's script.  By the way, you can use this skeleton to create custom automate script
and run it using GoCD or maybe Jenkins too.
---

NOTE

- Fabric 1.x is different than 2.x.
- Fabric 1.x does not support python 3.x, Fabric 2.x does.
```

## Installations

```
pipenv shell
pipenv install
```

If you are found some errors relate with pipenv, try to run this

```
pipenv run pip install pip==18.0
```

## Usage

```
fab --list
```

By default, i just provide all basic things with an assumption that you are using Ubuntu.

Example:

```
fab --host user@<your.server.ip> docker-setup
```

Automate running on multiple hosts:

```
fab --host user@<your.server.ip>,user2@<your.server.ip2> docker-setup
```

## Custom Module

Just follow example from `modules/`, example from `./modules/basic.py`:

```python
from fabric import tasks

@tasks.task
def basic_hostname(c):
    c.run('hostname')

@tasks.task
def basic_uname(c):
    c.run('uname -a')

```

Register your module to `./modules/__init__.py`
