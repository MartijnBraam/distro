import os
import configparser
from distro.structs import *
import copy
import logging


def identify():
    logging.debug('Trying to identify Debian')
    possible_files = ['/etc/os-release', '/etc/debian_release', '/etc/debian_version']
    hit = ""
    for file in possible_files:
        if os.path.isfile(file):
            hit = file
    if hit == "":
        logging.debug('No debian release file found')
        return False

    logging.debug('Found debian release file: {}'.format(hit))

    with open(hit) as release_file:
        release_file_contents = release_file.read()

    if "debian" not in release_file_contents:
        logging.debug('Release file does not contain string "debian"')
        return False

    if hit == "/etc/os-release":
        logging.debug('Parsing /etc/os-release')
        return parse_os_release(release_file_contents)
    elif hit == "/etc/debian_release":
        logging.debug('Parsing /etc/debian_release')
        return parse_debian_release(release_file_contents)
    else:
        logging.debug('Trying to parse unknown format: {}'.format(hit))
        return parse_debian_version(release_file_contents)


def parse_os_release(contents):
    valid_config = "[debian]\n" + contents
    config = configparser.ConfigParser()
    config.read_string(valid_config)

    dist = LinuxDistro()
    dist.version_number = strip_quotes(config['debian']['VERSION_ID'])

    dist.name = config['debian']['ID']
    dist.name_pretty = strip_quotes(config['debian']['NAME'])

    dist.codename = get_codename(dist.version_number)
    dist.codename_pretty = dist.codename.title()

    dist.homepage = strip_quotes(config['debian']['HOME_URL'])

    if dist.name == "raspbian":
        parent_dist = copy.copy(dist)
        parent_dist.name = "debian"
        parent_dist.name_pretty = "Debian GNU/Linux"
        dist.parent = parent_dist

    if dist.version_number < 8:
        dist.command['service'] = COMMAND_SERVICE_SYSV
    else:
        dist.command['service'] = COMMAND_SERVICE_SYSTEMD

    dist.command['package'] = COMMAND_PACKAGE_APT
    return dist


def parse_debian_release(contents):
    return False


def parse_debian_version(contents):
    return False


def strip_quotes(value):
    return value.lstrip('"').rstrip('"')


def get_codename(version):
    version = int(version)
    version_dict = {
        4: "etch",
        5: "lenny",
        6: "squeeze",
        7: "wheezy",
        8: "jessie",
        9: "stretch",
        10: "buster"
    }
    if version in version_dict:
        return version_dict[version]
    else:
        return "unknown"
