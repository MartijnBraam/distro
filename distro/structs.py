class LinuxDistro:
    def __init__(self):
        self.name = ""
        self.name_pretty = ""
        self.version_number = ""
        self.codename = ""
        self.codename_pretty = ""
        self.parent = None

        self.command = {
            'service': {},
            'package': {}
        }

    def __repr__(self):
        return "<LinuxDistro {} {}>".format(self.name, self.version_number)


COMMAND_SERVICE_SYSTEMD = {
    'start': 'systemctl start {}.service',
    'stop': 'systemctl stop {}.service',
    'restart': 'systemctl restart {}.service',
    'reload': 'systemctl reload-or-restart {}.service',
    'enable': 'systemctl enable {}.service',
    'disable': 'systemctl disable {}.service'
}

COMMAND_SERVICE_SYSV = {
    'start': 'service {} start',
    'stop': 'service {} stop',
    'restart': 'service {} restart',
    'reload': 'service {} reload',
    'enable': 'update-rc.d {} enable',
    'disable': 'update-rc.d {} disable'
}

COMMAND_PACKAGE_APT = {
    'install': 'apt-get -y install --no-install-recommends {}',
    'uninstall': 'apt-get -y remove {}',
    'purge': 'apt-get -y purge {}',
    'search': 'apt-cache search {}',
    'is-installed': 'dpkg -s {}'
}

COMMAND_PACKAGE_PACMAN = {
    'install': 'pacman -S --noconfirm {}',
    'uninstall': 'pacman -Rs --noconfirm {}',
    'purge': 'pacman -Rsn --noconfirm {}',
    'search': 'pkgfile {}',
    'is-installed': 'pacman -Q {}'
}
