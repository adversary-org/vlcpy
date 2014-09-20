# A Python package, what a surprise!

# VLC and Python Version checker.
#
# Author: Ben McGinnes <ben@adversary.org>
#
# Provided to the VideoLAN Project under the terms of the LGPL 2.1 or
# any later version, may optionally be licensed under the terms of the
# GPL 3.0 or later (dual licensed).

import os
import os.path
import subprocess
import sys
import inspect

# Just in case people are using Python 3, sets VLC module path:

cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)


if sys.platform == "darwin":
    vlcx = "VLC"
    topdir = os.path.abspath("/Applications/")
elif sys.platform == "win32":
    vlcx = "vlc.exe"
    topdir = os.path.abspath("C:\\Program Files\\")
elif sys.platform == "linux2":
    topdir = os.path.abspath("/")
    vlcx = "vlc"
else:
    vlcx = "vlc"  # probably
    topdir = os.path.abspath("/")

def vlcpath(vlcx, topdir):
    for root, dirs, files in os.walk(topdir, topdown=False):
        if vlcx in files:
            return os.path.join(root, vlcx)

vlcexec = vlcpath(vlcx, topdir)
vlc_ver = subprocess.Popen([vlcexec, "--version"], stdout=subprocess.PIPE).communicate()[0]
vlcver = vlc_ver.split(" ")[2]

if vlcver.startswith(b"1.0"):
    from vlc_100 import *
elif vlcver.startswith(b"1.1"):
    from vlc_110 import *
elif vlcver.startswith(b"2.0"):
    from vlc_200 import *
elif vlcver.startswith(b"2.1"):
    from vlc_210 import *
else:
    from vlc_current import *
