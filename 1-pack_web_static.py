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


def do_pack():
    """
    Compresses the web_static folder into a .tgz archive.

    The compressed archive is stored in the "versions" directory with a\
        timestamped filename.

    Returns:
        str: The file path of the compressed archive.
    """
    local("mkdir -p versions")
    archive_name = "versions/web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S")
    )
    local("tar -cvzf {} web_static".format(archive_name))
    return archive_name
