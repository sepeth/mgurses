import os, getpass, time
from misc import start_proc, unix_socket
import daemon

def main():
    sockfile = "/tmp/mg-" + getpass.getuser()
    if not os.path.exists(sockfile):
        start_proc(daemon.main, args=(sockfile,), daemon=True)
        time.sleep(1)
    sock = unix_socket()
    sock.connect(sockfile)

if __name__ == '__main__':
    main()
