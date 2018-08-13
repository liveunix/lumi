from pathlib import Path
from xdg.BaseDirectory import xdg_data_home
from repositories import *
import yaml

def get_distro(name_id=''):
    path = xdg_data_home + '/lumi/distro/'
    data = Path(path).glob('*/*.yaml')
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

