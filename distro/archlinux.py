import os
from distro.structs import LinuxDistro


def identify():
    if not os.path.isfile("/etc/os-release"):
        return False

    with open("/etc/os-release") as release_file:
        release_file_contents = release_file.read()

    if "ID=arch" not in release_file_contents:
        return False

    result = LinuxDistro()
    result.name = "arch"
    result.name_pretty = "Arch Linux"

    # Arch doesn't have more information

    return result