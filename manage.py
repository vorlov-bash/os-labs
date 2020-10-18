import argparse
import importlib

parser = argparse.ArgumentParser()
parser.add_argument('--lab', help='Which lab do you want to execute')
args = parser.parse_args()

importlib.import_module('lab' + args.lab)
