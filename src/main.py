from __future__ import print_function

import argparse
import os
import sys

from .install import command as install
from .search import command as search
from .show import command as show
from .version import print_version


def main():
    # static config for now
    config = {
        'directory': 'powser_components',
        'histfile': 'powser.json'
    }

    parser = argparse.ArgumentParser(
        description='cdnjs package fetcher',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    subparsers = parser.add_subparsers()

    #####################
    # COMMANDS
    #####################
    # Version command
    parser_version = subparsers.add_parser(
        'version', help='Print version and quit')
    parser_version.set_defaults(f=print_version)
    # Search command
    parser_search = subparsers.add_parser('search', help='Search cdnjs')
    parser_search.add_argument('query', help='Search string')
    parser_search.add_argument('--all', action='store_true')
    parser_search.set_defaults(f=search)
    # Show command
    parser_show = subparsers.add_parser('show', help='show pkg')
    parser_show.add_argument('pkg', help='Show package details')
    parser_show.set_defaults(f=show)
    # Install command
    parser_install = subparsers.add_parser('install', help='Install pkg')
    parser_install.add_argument('pkg', help='Package to install')
    parser_install.set_defaults(f=install, mkdir=True, chdir=True)
    #####################
    # End commands
    #####################

    args = parser.parse_args()

    # If this command forces the dir to exist, mkdir it
    if 'mkdir' in args:
        if not os.path.exists(config['directory']):
            print('Initializing directory', config['directory'])
            os.mkdir(config['directory'])

    # If this commands request to chdir into powser_components
    if 'chdir' in args:
        os.chdir(config['directory'])

    # Run the callback specified above
    result = args.f(args, config)

    # Return with error code if one is specified
    if result is not None:
        sys.exit(result)


if __name__ == '__main__':
    main()
