import socket, getpass, time, os, sys, atexit

def start_proc(fn, args, daemon=False):
    if os.fork() == 0:
        if daemon:
            os.setsid()
            os.chdir("/")
            os.umask(0)
            sys.stdin.close()
            sys.stdout.close()
            sys.stderr.close()
        try:
            fn(*args)
        finally:
            sys.exit()

def unix_socket():
    return socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

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

def do_command(cmd):
    pass

def daemon(sockfile):
    sock = unix_socket()
    sock.bind(sockfile)
    atexit.register(os.remove, sockfile)
    sock.listen(1)
    while True:
        conn, addr = sock.accept()
        for cmd in get_command(conn):
            do_command(cmd)

def client():
    sockfile = "/tmp/mg-" + getpass.getuser()
    if not os.path.exists(sockfile):
        start_proc(daemon, args=(sockfile,), daemon=True)
        time.sleep(1)
    sock = unix_socket()
    sock.connect(sockfile)

if __name__ == '__main__':
    client()
