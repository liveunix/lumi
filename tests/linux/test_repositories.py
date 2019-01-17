import unittest
from pathlib import Path
from shutil import rmtree
from src.lumi.linux.repositories import *


class TestRepo(unittest.TestCase):
    def _remove_dirs(self, dirs):
        for dir in dirs:
            rmtree(dir, ignore_errors=True)

    def setUp(self):
        self._remove_dirs(["./grub", "./distro"])

    def tearDown(self):
        self._remove_dirs(["./grub", "./distro"])

    def test_clone_repos(self):
        sync("./")

        self.assertTrue(Path("./grub").exists())
        self.assertTrue(Path("./distro").exists())
