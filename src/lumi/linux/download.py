import requests
import distro_data

def download(name, arch, version, partition_fs, flavour='', type='iso'):
    distro = distro_data.get_distro()
    print(distro)
    # if distro['name']
    r = requests.get('https://archlinux.beccacervello.it/archlinux/iso/2018.07.01/archlinux-2018.07.01-x86_64.iso', stream=True)
    if r.status_code == 200:
        with open('/tmp/archlinux.iso', 'wb') as f:
            total_length = r.headers.get('content-length')
            if total_length is None: # no content length header
                f.write(r.content)
            else:
                dl = 0
                total_length = int(total_length)
                for chunk in r.iter_content(chunk_size=4096):
                    dl += len(chunk)
                    f.write(chunk)
                    done = int(50 * dl / total_length)

if __name__ == '__main__':
    download('arch', 'amd64', '0', '/dev/sdc1')
