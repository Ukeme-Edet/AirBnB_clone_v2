#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir

env.hosts = ["100.26.229.8", "3.89.160.250"]


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


def do_deploy(archive_path):
    """
    Deploys the web_static folder to the web servers.

    Args:
        archive_path (str): The path to the compressed archive of the\
            web_static folder.

    Returns:
        bool: True if the deployment was successful, False otherwise.
    """
    if not exists(archive_path):
        return False
    archive_name = archive_path.split("/")[-1]
    archive_name_no_ext = archive_name.split(".")[0]
    archive_dir = "/data/web_static/releases/{}/".format(archive_name_no_ext)
    put(archive_path, "/tmp/")
    run("mkdir -p {}".format(archive_dir))
    run("tar -xzf /tmp/{} -C {}".format(archive_name, archive_dir))
    run("rm /tmp/{}".format(archive_name))
    run("mv {}web_static/* {}".format(archive_dir, archive_dir))
    run("rm -rf {}web_static".format(archive_dir))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(archive_dir))
    return True


def deploy():
    """
    Creates and distributes an archive to the web servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
