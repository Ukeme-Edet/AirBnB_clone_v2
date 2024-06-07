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
            archive_path (str): The path to the .tgz archive to deploy.

    Returns:
            bool: True if the archive was successfully deployed, False\
                otherwise.
    """
    if not exists(archive_path):
        return False
    archive_name = archive_path.split("/")[-1]
    archive_folder = "/data/web_static/releases/" + archive_name.split(".")[0]
    put(archive_path, "/tmp/")
    run("mkdir -p {}".format(archive_folder))
    run("tar -xzf /tmp/{} -C {}".format(archive_name, archive_folder))
    run("rm /tmp/{}".format(archive_name))
    run("mv {}/web_static/* {}/".format(archive_folder, archive_folder))
    run("rm -rf {}/web_static".format(archive_folder))
    run("rm -rf /data/web_static/current")
    run("ln -s {} /data/web_static/current".format(archive_folder))
    return True
