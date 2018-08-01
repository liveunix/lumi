from pathlib import Path
from xdg.BaseDirectory import xdg_data_home
from repositories import *
import yaml

def get_distro():
    path = xdg_data_home + '/lumi/distro/'
    data = Path(path).glob('*/*.yaml')
    distro_list = []
    for d in data:
        with open(d, 'r') as stream:
            distro = yaml.load(stream)
            distro_list.append({'id': d.stem, 'distro': distro})

    return distro_list

