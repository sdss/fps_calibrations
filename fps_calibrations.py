#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-10-15
# @Filename: version.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

import os
import subprocess

__version__ = "APO.2022.04.21"


def get_version():
    """Returns the version as ``__version__+hash`` unless HEAD is tagged."""

    cwd = os.path.dirname(__file__)
    head = subprocess.run(
        "git rev-parse --short HEAD",
        shell=True,
        cwd=cwd,
        capture_output=True,
    )

    if head.returncode > 0:
        # It's not a Git repo.
        return __version__

    # Check if the HEAD is tagged.
    tag = subprocess.run(
        "git describe --exact-match --tags HEAD",
        shell=True,
        cwd=cwd,
        capture_output=True,
    )

    if tag.returncode == 0:
        return tag.stdout.decode().strip()

    # This is an untagged version in an active Git repo. Return
    # the current version plus the hash.

    # First get the latest tag.
    latest_tag_cmd = subprocess.run(
        "git describe --tags --abbrev=0",
        shell=True,
        cwd=cwd,
        capture_output=True,
    )
    if latest_tag_cmd.returncode == 0:
        latest_tag = latest_tag_cmd.stdout.decode().strip()
    else:
        latest_tag = "unknown"

    return latest_tag + "+" + head.stdout.decode().strip()
