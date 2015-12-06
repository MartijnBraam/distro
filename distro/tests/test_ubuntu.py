from unittest import TestCase
from distro.ubuntu import parse_os_release
from distro.structs import LinuxDistro


class TestUbuntu(TestCase):
    def test_parse_os_release_8(self):
        with open('fixtures/ubuntu/os-release-1404') as test_file:
            test_data = test_file.read()
        result = parse_os_release(test_data)
        self.assertIsInstance(result, LinuxDistro)
        self.assertEqual(result.name, "ubuntu")
        self.assertEqual(result.name_pretty, "Ubuntu")

        self.assertEqual(result.codename, "trusty"),
        self.assertEqual(result.codename_pretty, "Trusty Tahr"),

        self.assertEqual(result.version_number, "14.04")

        self.assertIsInstance(result.parent, LinuxDistro)
        self.assertEqual(result.parent.name, "debian")
        self.assertEqual(result.parent.name_pretty, "Debian GNU/Linux")
