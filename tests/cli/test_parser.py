import unittest
from lumi.cli.parser import parse_args


class TestParser(unittest.TestCase):
    """Tests CLI arguments parser"""

    def test_distro_mode(self):
        parser = parse_args(["install", "/dev/sdb"], offset=0)
        self.assertFalse(parser.stage_three)

    def test_stage_three_mode(self):
        parser = parse_args(["install", "/dev/sdb", "--stage3"], offset=0)
        self.assertTrue(parser.stage_three)

    def test_install_lumi(self):
        parser = parse_args(["install", "/dev/sdb2"], offset=0)
        self.assertEqual("/dev/sdb2", parser.device)

    def test_inspect_lumi(self):
        parser = parse_args(["inspect", "/dev/sdb2"], offset=0)
        self.assertEqual("/dev/sdb2", parser.device)

    def test_install_without_device_arg(self):
        func = lambda: parse_args(["install"], offset=0)
        self.assertRaises(SystemExit, func)

    def test_try_to_add_distro_without_device(self):
        func = lambda: parse_args(["add", "ubuntu:1084", "--arch=x86_64"], offset=0)
        self.assertRaises(SystemExit, func)

    def test_add_distro_to_device(self):
        parser = parse_args(
            ["add", "ubuntu:18.04", "/dev/sdb", "--arch=x86_64"], offset=0
        )
        self.assertEqual("ubuntu:18.04", parser.target)
        self.assertEqual("/dev/sdb", parser.device)
        self.assertEqual("x86_64", parser.architecture)

    def test_list_all_distro_versions(self):
        parser = parse_args(["list", "ubuntu"], offset=0)
        self.assertTrue("ubuntu", parser.name)

    def test_list_all_distros(self):
        parser = parse_args(["list-all", "-3"], offset=0)
        self.assertTrue(parser.stage_three)

    def test_suffix_flags(self):
        parser = parse_args(["list-all", "--stage3", "-a", "i686"], offset=0)
        self.assertTrue(parser.stage_three)
        self.assertEqual("i686", parser.architecture)


if __name__ == "__main__":
    unittest.main()
