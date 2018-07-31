import sh
from pathlib import Path
from xdg.BaseDirectory import xdg_data_home

def sync():
    base_dir = xdg_data_home + '/lumi/'

    # Check for the git repo
    if not Path(base_dir + '/grub_cfg').exists():
        # Clone if it does not exists
        sh.git.clone('https://github.com/liveunix/limu-grub-cfg', 'grub-cfg')
    else:
        # Pull update if it exists
        sh.cd(base_dir + '/grub_cfg')
        sh.git.pull(rebase=True)

    # Same for distro data
    if not Path(base_dir + '/distro').exists():
        sh.git.clone('https://github.com/liveunix/liveunix-data', 'distro')
    else:
        sh.cd(base_dir + '/distro')
        sh.git.pull(rebase=True)

