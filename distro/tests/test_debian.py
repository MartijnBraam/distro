from unittest import TestCase
from distro.debian import parse_os_release
from distro.structs import LinuxDistro


class TestDebian(TestCase):
    def test_parse_os_release_8(self):
        with open('fixtures/debian/os-release-8') as test_file:
            test_data = test_file.read()
        result = parse_os_release(test_data)
        self.assertIsInstance(result, LinuxDistro)
        self.assertEqual(result.name, "debian")
        self.assertEqual(result.version_number, "8")
        self.assertEqual(result.codename, "jessie"),
        self.assertEqual(result.pretty_name, "Debian GNU/Linux 8 (jessie)")

    def test_parse_os_release_7(self):
        with open('fixtures/debian/os-release-7') as test_file:
            test_data = test_file.read()
        result = parse_os_release(test_data)
        self.assertIsInstance(result, LinuxDistro)
        self.assertEqual(result.name, "debian")
        self.assertEqual(result.version_number, "7")
        self.assertEqual(result.codename, "wheezy"),
        self.assertEqual(result.pretty_name, "Debian GNU/Linux 7 (wheezy)")