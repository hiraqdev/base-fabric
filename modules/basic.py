from fabric import tasks

@tasks.task
def basic_hostname(c):
    c.run('hostname')

@tasks.task
def basic_uname(c):
    c.run('uname -a')
