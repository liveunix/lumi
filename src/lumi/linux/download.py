from os.path import splitext
import requests
import distro_data
from devices import *


def download(name_id, arch, version, partition_fs, flavour="", dl_type="iso"):
    distro = distro_data.get_distro(name_id=name_id)
    if flavour == "":
        link = distro[dl_type][arch][version]
    else:
        link = distro[dl_type][arch][flavour][version]

    r = requests.get(link, stream=True)

    if r.status_code == 200:
        if dl_type == "iso":
            filename = name_id + "-" + arch + "-" + version + ".iso"
        elif dl_type == "stage3":
            filename = name_id + "-" + arch + "-" + version + splitext(link)[1]
        mountpoint = get_mountpoint(partition_fs)
        if mountpoint == None:
            # Replace with a custom type Exception
            raise Exception("Device not mounted")
        dl_path = Path(mountpoint + "/" + dl_type + "/" + name_id + "/")
        if not dl_path.exists():
            makedirs(dl_path)
        with open(str(dl_path) + "/" + filename, "wb") as f:
            total_length = r.headers.get("content-length")
            if total_length is None:  # no content length header
                f.write(r.content)
            else:
                dl = 0
                total_length = int(total_length)
                for chunk in r.iter_content(chunk_size=4096):
                    dl += len(chunk)
                    f.write(chunk)
                    done = int(50 * dl / total_length)


def add_distro_dl_status():
    pass


if __name__ == "__main__":
    mount("/dev/sdd1")
    download("arch", "x86_64", "2018.06.01", "/dev/sdd1")
