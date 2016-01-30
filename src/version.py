from __future__ import print_function

__VERSION__ = (1, 0, 0)
__VERSION_STR__ = '.'.join(map(str, __VERSION__))


def print_version(args):
    print("powser version {0}".format(__VERSION_STR__))
