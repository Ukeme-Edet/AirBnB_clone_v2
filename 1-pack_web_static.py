#!/usr/bin/python3
"""
This script compresses the web_static folder into a .tgz archive.

The compressed archive is stored in the "versions" directory with a\
    timestamped filename.

Usage:
    Run this script to create a compressed archive of the web_static folder.

Returns:
    str: The file path of the compressed archive.
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Compresses the web_static folder into a .tgz archive.

    The compressed archive is stored in the "versions" directory with a\
        timestamped filename.

    Returns:
        str: The file path of the compressed archive.
    """
    # Create the versions directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create the filename of the archive
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(timestamp)

    # Compress the web_static folder into a .tgz archive
    local("tar -cvzf {} web_static".format(archive_path))

    return archive_path if os.path.exists(archive_path) else None
