import yaml
from lumi.core.action import *
from lumi.core.statushandler import *
from lumi.core.buffer import g_buf
from pathlib import Path
from sh.contrib import git
from xdg.BaseDirectory import xdg_data_home

BASE_DIR = xdg_data_home + '/lumi/'
DISTRO_REPO_URL = 'https://github.com/liveunix/liveunix-data.git'
GRUB_REPO_URL = 'https://github.com/liveunix/lumi-grub.git'


def sync_repo(uri, dir, buf):
    """Synchronize a single repository"""
    repo_exists = Path(dir).exists()

    if repo_exists is False:
        g_buf().write("Cloning the repository {}.\n".format(uri))
        g_buf().flush()
        return git.clone(uri, dir, _out=buf)

    g_buf().write("Updating the repository {} to the latest commit.\n".format(uri))
    g_buf().flush()
    return git.pull('origin', 'master', _cwd=dir, _out=buf)


def sync(base_dir=BASE_DIR):
    """Synchronize the LUMI repositories.

    If the repositories are not on the system, clone them.
    Otherwise, it pulls the updates from the remote repositories.
    """
    GRUB_DIR = base_dir + 'grub'
    DISTRO_DIR = base_dir + 'distro'

    sync_repo(GRUB_REPO_URL, GRUB_DIR, g_buf())

    sync_repo(DISTRO_REPO_URL, DISTRO_DIR, g_buf())


def get_distro_info(name_id='', base_dir=BASE_DIR):
    data = Path(base_dir + 'distro').glob('*/*.yaml')
    distro_list = []
    for d in data:
        with open(d, 'r') as stream:
            distro = yaml.load(stream)
            distro_list.append({'id': d.stem, 'distro': distro})

    if name_id != '':
        for d in distro_list:
            if d['id'] == name_id:
                return d['distro']

    return distro_list


def get_distro_list(base_dir=BASE_DIR):
    data = Path(base_dir + 'distro').glob('*/*.yaml')
    distro_list = []
    for d in data:
        pass
    return distro_list


def initialize(mountpoint):
    pass
