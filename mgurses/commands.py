import logging as log
import player

def play(args):
    log.info('play')
    player.play()

def pause(args):
    log.info('pause')
    player.pause()

def add(args):
    path = args[0]
    log.info('add ' + path)
    player.append(path)
