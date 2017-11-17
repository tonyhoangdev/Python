#!/usr/bin/env python3

import os
import re
import sys
import json

def parse(text):
    try:
        return json.load(text)
    except ValueError as e:
        print('invalid json: %s' % e)
        return None # or: raise

file = sys.argv[1]
if (file != ""):
    with open(file) as f_in:
        json_data = parse(f_in)
        f_in.close()

    if (json_data):
        with open(file, 'w', newline='\n') as f_out:
            json.dump(json_data, f_out, indent=4)
            f_out.close()

        print("-------- xong.hehe --------")
