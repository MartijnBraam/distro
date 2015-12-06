import os
import configparser
from distro.structs import LinuxDistro


def identify():
    possible_files = ['/etc/os-release', '/etc/debian_release', '/etc/debian_version']
    hit = ""
    for file in possible_files:
        if os.path.isfile(file):
            hit = file
    if hit == "":
        return False

    with open(hit) as release_file:
        release_file_contents = release_file.read()

    if hit == "/etc/os-release":
        return parse_os_release(release_file_contents)
    elif hit == "/etc/debian_release":
        return parse_debian_release(release_file_contents)
    else:
        return parse_debian_version(release_file_contents)


def parse_os_release(contents):
    valid_config = "[debian]\n" + contents
    config = configparser.ConfigParser()
    config.read_string(valid_config)

    dist = LinuxDistro()
    dist.pretty_name = strip_quotes(config['debian']['PRETTY_NAME'])
    dist.version_number = strip_quotes(config['debian']['VERSION_ID'])
    dist.name = config['debian']['ID']
    dist.codename = get_codename(dist.version_number)
    dist.homepage = strip_quotes(config['debian']['HOME_URL'])
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
        8: "jessie"
    }
    if version in version_dict:
        return version_dict[version]
    else:
        return "unknown"
