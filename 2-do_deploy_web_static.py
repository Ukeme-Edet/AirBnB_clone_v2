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
        archive_path (str): The file path of the compressed archive.

    Returns:
        bool: True if successful, False otherwise.
    """
    if exists(archive_path) is False:
        return False
    else:
        try:
            put(archive_path, "/tmp/")
            """ putting the file to .tgz """
            file_name = archive_path.split("/")[1]
            """ splitting .tgz """
            file_name2 = file_name.split(".")[0]
            """ spliting archivo """
            final_name = "/data/web_static/releases/" + file_name2 + "/"
            run("mkdir -p " + final_name)
            run("tar -xzf /tmp/" + file_name + " -C " + final_name)
            run("rm /tmp/" + file_name)
            run("mv " + final_name + "web_static/* " + final_name)
            run("rm -rf " + final_name + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + final_name + " /data/web_static/current")
            print("New version deployed!")
            return True
        except Exception:
            return False
