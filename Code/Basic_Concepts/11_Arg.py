#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: Arg
"""

import argparse
import os
import datetime


def run():
    """
    Run application using command line args.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('-w', dest = 'workingDir', required = True, help = 'Working directory (expected to [...]\sdk_codebase\)')
    parser.add_argument('-s', dest = "source", required = True, help = "Source file")
    parser.add_argument('-d', dest = "destination", required = False, help = "Destination file")

    groupParser = parser.add_mutually_exclusive_group()
    groupParser.add_argument('-c', dest = 'components', type=str, default='all', help = "The list of components to be inspected")

    parser.add_argument('-t', dest = 'types', type = str, default = 'all', help = 'The list of component types to be inspected (by default all component types will be inspected)')


    args = parser.parse_args()

    components = args.components.strip().split(',')
    types = args.types.strip().split(',')

    workingDir = os.path.abspath(args.workingDir)


    print(args)
    print(components)
    print(types)
    print(workingDir)

# Execute
run()