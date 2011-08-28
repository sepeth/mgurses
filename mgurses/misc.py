import os, sys, socket

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
