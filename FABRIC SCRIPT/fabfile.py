from fabric import task, Connection

HOST = "ubuntu@your-ec2-ip"


@task
def uptime(c):
    conn = Connection(HOST)
    result = conn.run("uptime", hide=True)
    print(result.stdout)


@task
def disk(c):
    conn = Connection(HOST)
    result = conn.run("df -h", hide=True)
    print(result.stdout)