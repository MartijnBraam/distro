import os
import configparser
from distro.structs import *
import copy


def identify():
    possible_files = ['/etc/os-release']
    hit = ""
    for file in possible_files:
        if os.path.isfile(file):
            hit = file
    if hit == "":
        return False

    with open(hit) as release_file:
        release_file_contents = release_file.read()

    if "ubuntu" not in release_file_contents:
        return False

    if hit == "/etc/os-release":
        return parse_os_release(release_file_contents)
    else:
        return False


def parse_os_release(contents):
    valid_config = "[ubuntu]\n" + contents
    config = configparser.ConfigParser()
    config.read_string(valid_config)

    dist = LinuxDistro()
    dist.version_number = strip_quotes(config['ubuntu']['VERSION_ID'])

    dist.name = config['ubuntu']['ID']
    dist.name_pretty = strip_quotes(config['ubuntu']['NAME'])

    dist.codename = get_codename(dist.version_number)[0]
    dist.codename_pretty = get_codename(dist.version_number)[1]

    dist.homepage = strip_quotes(config['ubuntu']['HOME_URL'])

    dist.parent = LinuxDistro()
    dist.parent.name = "debian"
    dist.parent.name_pretty = "Debian GNU/Linux"

    dist.command['package'] = COMMAND_PACKAGE_APT
    dist.command['service'] = COMMAND_SERVICE_SYSV
    return dist


def parse_debian_release(contents):
    return False


def parse_debian_version(contents):
    return False


def strip_quotes(value):
    return value.lstrip('"').rstrip('"')


def get_codename(version):
    version_dict = {
        "10.04": ("lucid", "Lucid Lynx"),
        "10.10": ("maverick", "Maverick Meerkat"),
        "11.04": ("natty", "Natty Narwhal"),
        "11.10": ("oneiric", "Oneiric Ocleot"),
        "12.04": ("precise", "Precise Pangolin"),
        "12.10": ("quantal", "Quantal Quetzal"),
        "13.04": ("raring", "Raring Ringtail"),
        "13.10": ("saucy", "Saucy Salamander"),
        "14.04": ("trusty", "Trusty Tahr"),
        "14.10": ("utopic", "Utopic Unicorn"),
        "15.04": ("vivid", "Vivid Vervet"),
        "15.10": ("wily", "Wily Werewolf"),
        "16.04": ("xenial", "Xenial Xerus")
    }
    if version in version_dict:
        return version_dict[version]
    else:
        return ("unknown", "unknown")
