from __future__ import print_function

import os
import requests

from .cdnjs import grab, select_default, asset_url

CHUNK_SIZE = 1024


def mkdirs(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)


def command(args, config):
    package_name = args.pkg
    result = grab(package_name)

    if result is None:
        print('Package {0!r} not found'.format(package_name))
        return -1

    versions = result['assets']
    package = select_default(versions)
    version = package['version']

    if not os.path.exists(package_name):
        os.mkdir(package_name)
    os.chdir(package_name)

    if not os.path.exists(version):
        os.mkdir(version)
    os.chdir(version)

    print('Installing {0} version {1}...'.format(package_name, version))
    print()
    for asset in package['files']:
        url = asset_url(package_name, version, asset)
        dirname = os.path.dirname(asset)
        if dirname:
            mkdirs(dirname)
        path = os.path.join(os.getcwd(), asset)
        short_name = path.split('powser_components')[-1]
        print('Downloading', short_name, '... ', end='')

        with open(asset, 'wb') as f:
            response = requests.get(url, stream=True)
            if not response.ok:
                print('Failed!')
                return -1
            for chunk in response.iter_content(CHUNK_SIZE):
                f.write(chunk)
            print('Done.')

    print()
    print('Successfully installed.')
