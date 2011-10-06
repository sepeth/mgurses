import gst, gobject, threading

player = None
playlist = []
currpls = iter(playlist)

def play():
    global player
    if not player:
        player = gst.element_factory_make("playbin2", "player")
        fakesink = gst.element_factory_make("fakesink", "fakesink")
        player.set_property("video-sink", fakesink)
        bus = player.get_bus()
        bus.add_signal_watch()
        bus.connect("message", on_message)

    loop = gobject.MainLoop()
    gobject.threads_init()
    play_file(currpls.next())
    threading.Thread(target=loop.run).start()

def append(path):
    playlist.append(path)

def on_message(bus, msg):
    t = msg.type
    if t == gst.MESSAGE_EOS:
        play_file(currpls.next())
        return True

def play_file(path):
    player.set_state(gst.STATE_NULL)
    player.set_property("uri", "file://" + path)
    player.set_state(gst.STATE_PLAYING)
