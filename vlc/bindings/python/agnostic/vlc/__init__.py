# A Python package, what a surprise!

# VLC and Python Version checker.
#
# Author:  Ben McGinnes <ben@adversary.org>
# GPG Key:  0x321E4E2373590E5D
#
# This code is provided under the terms of the LGPL 2.1 or any later
# version (for compliance with existing VLC licencing), it may
# optionally be licensed under the terms of the GPL 3.0 or or any
# later version and the WTFNMFPL 1.0 or later (multi-licensing).
# Also, some code has been incorporated from stackoverflow.com
# (multiple authors and threads) and is thus attributable to the
# Creative Commons CC BY-SA 2.5 license.

import os
import os.path
import subprocess
import sys
import inspect

# Just in case people are using Python 3, sets VLC module path:

inspector = inspect.getfile(inspect.currentframe())
cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspector)[0]))
if cmd_folder not in sys.path:
    sys.path.insert(0, cmd_folder)

# The above code block was adapted from posts to stackoverflow.com,
# but may have its origins elsewhere and so may or may not be
# addressed with a Creative Commons license.
#
# The origin for this code is *believed* (not certain, it's spread
# pretty far now, but this is where I got it) to be:
#
# http://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path/6098238#6098238


if sys.platform == "darwin":
    vlcx = "VLC"
    topdir = os.path.abspath("/Applications/")
elif sys.platform == "win32" or "cygwin":
    vlcx = "vlc.exe"
    topdir = os.path.abspath("C:\\Program Files\\")
elif sys.platform == "linux" or "linux2":
    topdir = os.path.abspath("/")
    vlcx = "vlc"
else:
    vlcx = "vlc"  # probably (includes Solaris, SunOS and assorted BSDs)
    topdir = os.path.abspath("/")

def vlcpath(vlcx, topdir):
    for root, dirs, files in os.walk(topdir, topdown=False):
        if vlcx in files:
            return os.path.join(root, vlcx)

vlcexec = vlcpath(vlcx, topdir)
vlcepath = vlcexec[0:(len(vlcexec) - len(vlcx))]

# Include this along witn Windows lib locations when dir structure
# confirmed for Windows systems.  Linux and others should already be
# using shared libraries.
#
#if sys.platform == "darwin":
#    sys.path.insert(0, vlcepath)
#    sys.path.insert(0, vlcepath + "include/vlc/")
#    sys.path.insert(0, vlcepath + "lib/")
#    sys.path.insert(0, vlcepath + "plugins/")

vlc_ver = subprocess.Popen([vlcexec, "--version"],
                           stdout=subprocess.PIPE).communicate()[0]
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
