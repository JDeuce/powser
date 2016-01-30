from __future__ import print_function

from .cdnjs import grab, select_default


def command(args, config):
    pkg = args.pkg
    result = grab(pkg)

    if result is None:
        print('Package {0!r} not found')
        return -1

    versions = result['assets']
    default = select_default(versions)

    print(result['name'])
    print('\tdefault:', default['version'])

    print('versions:')
    for vresult in versions:
        version = vresult['version']
        files = vresult['files']

        print('+', version)
        for f in files:
            print('\t-', f)
