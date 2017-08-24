#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : arg parse
"""
import sys
import argparse
import logging

parser = argparse.ArgumentParser()

parser.add_argument("num1", help="The first number", type=int)
parser.add_argument("num2", help="The second number", type=int)

parser.add_argument("op", help="The desired arithmetic operation", choices=['add', 'sub', 'mul', 'div'])
parser.add_argument('-v', "--verbose", help="Turn on verbose output", action='store_true')

opts =parser.parse_args()

if opts.verbose:
    logging.basicConfig(level=logging.DEBUG)

logging.debug("First number: %d" % opts.num1)
logging.debug("Second number: %d" % opts.num2)
logging.debug("Operation: %s" % opts.op)

if opts.op == 'add':
    result = opts.num1 + opts.num2
elif opts.op == 'sub':
    result = opts.num1 - opts.num2
elif opts.op == 'mul':
    result = opts.num1 * opts.num2
elif opts.op == 'div':
    result = opts.num1 / opts.num2

print(result)

print(sys.argv)

