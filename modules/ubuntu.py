from os import environ
from fabric import tasks, Config, Connection

sudo_pass = environ.get('SUDO_PASS')
config = Config(overrides={'sudo': {'password': sudo_pass}})

@tasks.task
def ubuntu_update(c):
    c.config = config
    c.sudo('apt-get update')

@tasks.task
def ubuntu_upgrade(c):
    c.config = config
    c.sudo('apt-get upgrade')
