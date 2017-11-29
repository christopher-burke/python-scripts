#!/usr/bin/python

''' Python Script to get the Track, Artist and Album from iTunes. '''

from Foundation import *
from ScriptingBridge import *


def track_info(a):
    return {'name': a.name(), 'artist': a.artist(), 'album': a.album()}


if __name__ == "__main__":
    iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
    if iTunes.isRunning():
        d = track_info(iTunes.currentTrack())
        if (d['name'] and d['artist'] and d['album']) == None:
            print(d['name'] and d['artist'] and d['album'])

        else:
            print("Track\t:: %(name)s" % d)
            print("Artist\t:: %(artist)s" % d)
            print("Album\t:: %(album)s" % d)
    else:
        print("iTunes is closed")
