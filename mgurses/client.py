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
    # sock.send("add /home/sepeth/music/kotor1/01_-_startup_screen.mp3\n")
    # sock.send("add /home/sepeth/music/kotor1/02_-_main_theme.mp3\n")
    # sock.send("add /home/sepeth/music/kotor1/03_-_the_old_republic.mp3\n")
    # sock.send("play\n")

if __name__ == '__main__':
    main()
