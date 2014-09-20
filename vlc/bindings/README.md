This is a meta-note about this repository more than about the code
itself (that's further down the directory paths).

Since the VLC public repo only covers the media player and other
primarily graphical interfaces, there is no public access to the
libvlc bindings repo.  In particular this one:

git://git.videolan.org/vlc/bindings/python.git

As a consequence a work-around was required.  So the master branch for
the adversarial fork contains no updates.  The libvlc-bindings branch
created the bindings directory as a subdirectory of the master VLC
branch, this file and the submodule data for the python/ subdirectory.

To get to the python/ subdirectory and submodule you must switch to
the libvlc-bindings branch and then switch to the bindings/python/
directory.  At this point you will find yourself back in a master
branch, but now the master branch for that submodule, NOT the master
branch of VLC itself.

My updates are in the agnostic-mod branch (so named because the code
is intended to be platform, CPython version and VLC version agnostic).
