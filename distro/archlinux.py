import os
from distro.structs import *
import logging


def identify():
    logging.debug('Trying to identify Archlinux')
    if not os.path.isfile("/etc/os-release"):
        logging.debug('Release file not found: /etc/os-release')
        return False

    with open("/etc/os-release") as release_file:
        release_file_contents = release_file.read()

    if "ID=arch" not in release_file_contents:
        logging.debug('Realease file does not contain "ID=arch"')
        return False

    result = LinuxDistro()
    result.name = "arch"
    result.name_pretty = "Arch Linux"
    result.command['service'] = COMMAND_SERVICE_SYSTEMD
    result.command['package'] = COMMAND_PACKAGE_PACMAN

    # Arch doesn't have more information

    return result
