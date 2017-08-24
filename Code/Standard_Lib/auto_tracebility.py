#!/usr/bin/python
#
"""
    @author: MinhHT3
    @brief : Auto traceability
"""
import sys
import argparse
import logging
import subprocess
import threading
import _thread
import os

class TraceabilityUtils:
    """
    Helper class for running traceability
    """
    ''' Create_TraceabilityMatrix app '''
    TRACEABILITY_MATRIX_APP = 'Create_TraceabilityMatrix.exe'

    def __init__(self, driver_name, baseline, product_name, release_version, next_gen, traceability_path = '.'):
        self.__driver_name = driver_name
        self.__baseline = baseline
        self.__product_name = product_name
        self.__release_version = release_version
        self.__next_gen = next_gen
        self.__traceability_path = traceability_path

    def run(self):
        traceability_path = os.path.abspath(os.path.join(self.__traceability_path, self.TRACEABILITY_MATRIX_APP))
        trace_command = [traceability_path,
                         "-driver_name", self.__driver_name,
                         "-baseline", self.__baseline,
                         "-product_name", self.__product_name,
                         "-rel_version", self.__release_version,
                         "-next_gen" if self.__next_gen else ""
                        ]
       
        return TraceabilityUtils.run_subprocess(trace_command, stdout=True)

    @staticmethod
    def run_subprocess(command, stdout=True, env=None):
        print('Executing command: {0}'.format(command))
        proc = subprocess.Popen(command)#, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, shell=True, env=env)
        proc.wait()
        return proc.returncode               

def run():      
    """
    Run traceability matrix using command line args.
    The expected command line arguments are:
    -d <driver_name>
    -b <baseline>
    -pn <product_name>
    -rv <release_version>
    -ng <next_gen>
    """  
    product_name_list = ["S32K142", "S32K144", "S32K146", "S32K148", "MPC5746C", "MPC5748G"]

    parser = argparse.ArgumentParser()

    parser.add_argument("-d", dest='driver_name', help="Driver name", default='pins')
    parser.add_argument("-b", dest='baseline', help="Baseline", default='7.0 S32K14x_SDK_EAR_0.8.5_PINS')
    parser.add_argument("-pn", dest='product_name', help="Product name", choices=product_name_list, default='S32K146')
    parser.add_argument("-rv", dest='rel_version', help="Release version", default='S32K14x EAR 0.8.5')
    parser.add_argument("-ng", dest='next_gen', help="Next gen", choices=[True, False], default=True)
    parser.add_argument("-trace_path", dest='trace_path', help="Trace path", default=".")

    parser.add_argument('-v', "--verbose", help="Turn on verbose output", action='store_true')

    opts =parser.parse_args()

    if opts.verbose:
        logging.basicConfig(level=logging.DEBUG)

    logging.debug("Driver name: %s" % opts.driver_name)
    logging.debug("Baseline: %s" % opts.baseline)
    logging.debug("Product name: %s" % opts.product_name)
    logging.debug("Release version: %s" % opts.rel_version)
    logging.debug("Next gen: %s" % opts.next_gen)
    logging.debug("Trace path: %s" % opts.trace_path)

    traceability = TraceabilityUtils(opts.driver_name, opts.baseline, opts.product_name, opts.rel_version, opts.next_gen, opts.trace_path)
    print(traceability.run())

if __name__=="__main__":
    run()
