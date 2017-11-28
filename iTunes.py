#!/usr/bin/python

''' Python Script to get the Track, Artist and Album from iTunes. '''

__author__ = "Christopher James Burke"
__copyright__ = ""
__credits__ = ["Christopher James Burke"]
__license__ = ""
__version__ = "1.0.0"
__maintainer__ = "Christopher James Burke"
__email__ = "christopherjamesburke@gmail.com"
__status__ = "Development"
__date__ = "2013/09/21 14:08:11"

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
