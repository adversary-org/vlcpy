This code addresses the core aspects of the second point in the
current TODO list:

* Support multiple VLC versions: define a front-end module which will
   load the appropriate versionned module from a subdirectory.

That's heading in the right direction, but it is just as readily
achieved with all the vlc.py versions in one directory and the correct
one for the platform selected when the module is initialised.

The files beginning with vlc_ are existing versions of the vlc.py
module, with no changes at all.  As of September, 2014 vlc_current.py
and vlc_210.py are identical.  Should work with both Python 2 and
Python 3, with the same requirements as the original modules.

The __init__.py file detects the operating system, locates the VLC
executable for that operating system, extracts the version information
and then imports the relevent VLC code.

From the directory above vlc/__init__.py a Python instance should be
able to import vlc and observe identical behaviour as with current
versions of the module.  Alternatively copy the vlc/ directory to the
site-packages directory or add it to PYTHONPATH.

Current testing with PyPy indicates that the original vlc.py files
from VLC 2.0 onward do not work (the older ones probably don't either,
but testing has not been extensive).  While the VLC code is asserted
to be pure Python, many of the dependencies, particularly ctypes
(unsurprisingly) are not.  So it doesn't deal terribly well with that.
There has been no testing of IronPython with Mono, too much of an edge
case to really bother with especially when there's an alternative for
Mono to use native CPython 2.7.x anyway.  This should enable VLC
support in Unity game development, for example.

One point to note for future dev: the os.walk code to locate the VLC
executables could be readily adapted to more easily locate and load
all those lib files which many of the error reports on the forum and
elsewhere consist of.  In the case of OS X those libraries are in
subdirectories of the samedirectory the binary is in.  If the Windows
situation is similar then it's a simple matter to add those to the
PYTHONPATH in advance of the libvlc code being imported.  Preparations
to include that are already underway with some code in place and some
commented out in __init__.py.  Alternatively these directories could
be written to a list and simply checked sequentially when loading the
DLLs or dylibs.
