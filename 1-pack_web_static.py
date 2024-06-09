#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder of your
AirBnB Clone repo, using
the function do_pack."""

from datetime import datetime
import os
from fabric import task

@task
def do_pack(c):
    """Function to generate a .tgz archive from the contents of the web_static
    folder."""

    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = "versions/web_static_{}.tgz".format(time_stamp)

    # Create the versions directory if it doesn't exist
    os.makedirs("versions", exist_ok=True)

    # Run the tar command to create the archive
    result = c.run("tar -cvzf {} web_static".format(archive_path), warn=True)

    # Check if the archive was created successfully
    if result.ok and os.path.exists(archive_path):
        return archive_path
    else:
        return None
