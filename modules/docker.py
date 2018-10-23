from os import environ
from fabric import tasks, Config, Connection

sudo_pass = environ.get('SUDO_PASS')
config = Config(overrides={'sudo': {'password': sudo_pass}})

@tasks.task
def docker_setup(c):
    c.config = config
    c.sudo('apt-get install -y apt-transport-https ca-certificates curl software-properties-common')
    c.run('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
    c.sudo('apt-key fingerprint 0EBFCD88')
    c.sudo('add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"')
    c.sudo('apt-get update')
    c.sudo('apt-get install -y docker-ce')

@tasks.task
def docker_verify(c, use_sudo=False):
    c.config = config
    if not use_sudo:
        c.run('docker run hello-world')
    else:
        c.sudo('docker run hello-world')

@tasks.task
def docker_without_sudo(c):
    c.config = config
    c.sudo('usermod -aG docker ${USER}')

@tasks.task
def docker_version(c, use_sudo=False):
    if not use_sudo:
        c.run('docker version')
    else:
        c.config = config
        c.sudo('docker version')
