#!/usr/bin/python3

from argparse import ArgumentParser
import os
import re
import statistics

def parse_data(datapath):
    """Extracts bandwidth measurements from a directory of files containing 
    output from iperf3; returns a dictionary whose keys are the name of the 
    output files and whose values are the bandwidths contained in that file
    """
    data = {}
    for filename in os.listdir(datapath):
        filepath = os.path.join(datapath, filename)
        filedata = parse_file(filepath)
        data[filename] = filedata
    return data

def parse_file(filepath):
    """Parses a file containing output from iperf3 and returns an array of ints 
    containing the bandwidths output by iperf
    """
    # TODO
    return None

def output_summary(data):
    """Outputs the median bandwidth for each destination"""
    # TODO
    print("TODO")

def main():
    # Parse arguments
    arg_parser = ArgumentParser(description='Summarize bandwidth')
    arg_parser.add_argument('-d', '--datapath', dest='datapath', action='store',
            required=True, 
            help='Path to directory containing files with iperf3 output')
    settings = arg_parser.parse_args()

    data = parse_data(settings.datapath)
    output_summary(data)

if __name__ == '__main__':
    main()
