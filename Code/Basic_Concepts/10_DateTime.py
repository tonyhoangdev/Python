#!/usr/bin/python
"""
    @author: MinhHT3
    @brief: DateTime
"""

import datetime

NIGHTLY_BUILD_SUFFIX = 'NB_'

def addTag():
    ''' Nightly build suffix'''

    suffix = "{0}{1}".format(NIGHTLY_BUILD_SUFFIX, datetime.datetime.now().strftime("%y%m%d"))

    return suffix

suffix = addTag()
print("tag:", suffix)

