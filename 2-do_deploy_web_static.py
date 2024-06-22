#!/usr/bin/python3
"""
This script deploys the web_static folder to the web servers.

Usage:
    Run this script to deploy the web_static folder to the web servers.
"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ["100.26.229.8", "3.89.160.250"]


def do_deploy(archive_path):
    """
    Deploys the web_static folder to the web servers.

    Args:
        archive_path (str): The path to the compressed archive of the web_static\
            folder.

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
