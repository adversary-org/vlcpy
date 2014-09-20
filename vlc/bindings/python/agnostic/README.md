This code addresses the core aspects of the second point in the
current TODO list:

* Support multiple VLC versions: define a front-end module which will
   load the appropriate versionned module from a subdirectory.

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
site-packages directory.
