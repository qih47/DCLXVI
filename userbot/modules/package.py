# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#

import os
import subprocess
import platform
from userbot import SUDO


def _start_instalation():
    package_managers = [
        "pacman",
        "apt-get",
        "yum",
        "brew",
        "yaourt",
        "dnf",
        "homebrew",
        "eopkg",
        "snap"]

    if "linux" in str(platform.system()).lower():
        for manager in package_managers:
            try:
                subprocess.check_call(f"which {manager}", shell=True,
                                      stderr=subprocess.STDOUT)
                install_package(manager)
                return
            except:
                continue


def install_package(package_manager):
    packages = []
    to_install = []
    with open("Aptfile") as file:
        for line in file:
            packages.append(line)

    for package in packages:
        try:
            subprocess.check_call(f"which {package}", shell=True, stderr=subprocess.STDOUT)
        except:
            to_install.append(package)

    if to_install:
        if SUDO:
            subprocess.Popen(f"echo {str(SUDO)} | sudo -S {str(package_manager)}" +
                             f" install -y {' '.join(to_install)}", shell=True)
        else:
            subprocess.Popen(f"{str(package_manager)} install -y \
                            {' '.join(to_install)}", shell=True)


try:
    if not 'heroku' in os.environ['PATH'] and \
            not os.uname().sysname.lower == 'windows':
        _start_instalation()

except:
    _start_instalation()
