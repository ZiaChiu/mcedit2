"""
    posix
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import logging
import os
import sys
from mcedit2.util import resources

log = logging.getLogger(__name__)


# no build scripts for linux yet. no idea if frozen apps will be built for linux.
# put user files in checkout dir when running from source checkout, otherwise ~/.mcedit2

# xxx for .whl or distro-specific distrib, put user files in ~/.mcedit2

def getUserFilesDirectory():
    """
    Get the directory where user files are stored on POSIX systems (Linux, etc.).
    The directory depends on whether the application is run from a source checkout
    or a regular installation.
    """

    # On Linux, the FS encoding is given by the current locale
    # Linux filenames are defined to be bytestrings.

    # We handle filenames internally as 'unicode', so decode 'sys.argv[0]'
    # If a Linux filename cannot be decoded with the current locale, ignore it.
    # If this filename is the script filename, you lose.

    if resources.isSrcCheckout():
        # Source checkouts don't use the same folder as regular installations.
        dataDir = os.path.join(os.path.dirname(resources.getSrcFolder()), "MCEdit 2 Files")
    else:
        dataDir = os.path.expanduser("~/.mcedit2")

    if not os.path.exists(dataDir):
        os.makedirs(dataDir)

    return dataDir
