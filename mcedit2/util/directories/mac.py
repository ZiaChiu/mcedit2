"""
    mac
"""
from __future__ import absolute_import, division, print_function, unicode_literals
import logging
import os
import sys
from mcedit2.util import resources

log = logging.getLogger(__name__)

def getUserFilesDirectory():
    """
    Get the directory where user files are stored on macOS.
    The directory depends on whether the application is run from a source checkout
    or a regular installation.
    """

    # TODO if sys.getattr('frozen', False):
    # TODO os.getenv('RESOURCEPATH') or sys.getattr('_MEIPASS'), etc etc...

    # On macOS, the FS encoding is always UTF-8
    # macOS filenames are defined to be UTF-8 encoded.
    # We internally handle filenames as Unicode.

    if resources.isSrcCheckout():
        # Source checkouts don't use the same folder as regular installs.
        dataDir = os.path.join(os.path.dirname(resources.getSrcFolder()), "MCEdit 2 Files")
    else:
        dataDir = os.path.expanduser("~/Documents/MCEdit 2 Files")

    if not os.path.exists(dataDir):
        os.makedirs(dataDir)

    return dataDir
