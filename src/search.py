from __future__ import print_function

from .cdnjs import search


def command(args, config):
    results = search(args.query)

    # Only display the first 20 unless --all is specified
    if args.all:
        slice = results
    else:
        slice = results[0:20]
    for result in slice:
        print(result['name'])
