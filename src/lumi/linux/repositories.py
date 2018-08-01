import sh
from pathlib import Path
from xdg.BaseDirectory import xdg_data_home

def sync():
    base_dir = xdg_data_home + '/lumi/'
    grub_dir = base_dir + 'grub'
    distro_dir = base_dir + 'distro'

    # Check for the git repo
    if not Path(grub_dir).exists():
        # Clone if it does not exists
        sh.contrib.git.clone('https://github.com/liveunix/lumi-grub.git', grub_dir)
    else:
        # Pull update if it exists
        sh.git.pull('origin', 'master', rebase=True, _cwd=grub_dir)

    # Same for distro data
    if not Path(distro_dir).exists():
        sh.git.clone('https://github.com/liveunix/liveunix-data', distro_dir)
    else:
        sh.git.pull('origin', 'master', rebase=True, _cwd=distro_dir)


