class LinuxDistro:
    def __init__(self):
        self.name = ""
        self.name_pretty = ""
        self.version_number = ""
        self.codename = ""
        self.codename_pretty = ""
        self.parent = None

    def __repr__(self):
        return "<LinuxDistro {} {}>".format(self.name, self.version_number)
