#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# @Author: José Sánchez-Gallego (gallegoj@uw.edu)
# @Date: 2021-10-15
# @Filename: version.py
# @License: BSD 3-clause (http://www.opensource.org/licenses/BSD-3-Clause)

import os
import subprocess


# Modify this version only before tagging.
__version__ = "0.0.0"


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

    return __version__ + "+" + head.stdout.decode().strip()
