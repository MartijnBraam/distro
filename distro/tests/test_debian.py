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
        self.assertEqual(result.name_pretty, "Debian GNU/Linux")

        self.assertEqual(result.codename, "jessie"),
        self.assertEqual(result.codename_pretty, "Jessie"),

        self.assertEqual(result.version_number, "8")

    def test_parse_os_release_7(self):
        with open('fixtures/debian/os-release-7') as test_file:
            test_data = test_file.read()
        result = parse_os_release(test_data)
        self.assertIsInstance(result, LinuxDistro)
        self.assertEqual(result.name, "debian")
        self.assertEqual(result.name_pretty, "Debian GNU/Linux")

        self.assertEqual(result.codename, "wheezy"),
        self.assertEqual(result.codename_pretty, "Wheezy"),

        self.assertEqual(result.version_number, "7")