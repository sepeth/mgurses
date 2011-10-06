import socket, os, atexit
import logging as log
from misc import unix_socket

def get_command(sock):
    buf = sock.recv(4096)
    while True:
        if "\n" in buf:
            (line, buf) = buf.split("\n", 1)
            yield line
        else:
            more = sock.recv(4096)
            if not more:
                break
            else:
                buf = buf + more

def do(cmd):
    import commands
    words = cmd.split(' ', 1)
    act = words[0]
    args = words[1:]
    try:
        getattr(commands, act)(args)
    except KeyError:
        log.warning('No such action: ' + act)

def main(sockfile):
    log.basicConfig(filename='/tmp/mgd.log', level=log.INFO)
    sock = unix_socket()
    sock.bind(sockfile)
    atexit.register(os.remove, sockfile)
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        for cmd in get_command(conn):
            do(cmd)

if __name__ == '__main__':
    main()
