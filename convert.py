#! /opt/homebrew/bin/python3
# author: Justin Salsbery

import sys
import argparse

# constants
VERSION = "2.0.1"


# simplifies the default error format
class CustomErrorParser(argparse.ArgumentParser):
    def error(self, message):
        print("convert --help\n")
        print("examples:")
        print("\tconvert -b2 0101")
        print("\tconvert -b10 2023")
        print("\tconvert -b16 abcd")
        sys.exit(1)


# simplifies the default help format
class CustomHelpFormatter(argparse.HelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        pass

    def _format_action_invocation(self, action):
        if action.option_strings:
            return ', '.join(action.option_strings)
        return super()._format_action_invocation(action)


# set up argument parser
parser = CustomErrorParser(description="binary, decimal, and hexadecimal converter",
                           formatter_class=CustomHelpFormatter)
group = parser.add_mutually_exclusive_group(required=True)

# add arguments
parser.add_argument("-v", "--version", action="version",
                    version=f'%(prog)s {VERSION}', help="show version number and exit")
group.add_argument("-b2", "--binary", help="base 2")
group.add_argument("-b10", "--decimal", help="base 10")
group.add_argument("-b16", "--hexadecimal", help="base 16")

# parse arguments
args = parser.parse_args()

if args.binary is not None:
    value = int(args.binary, 2)
elif args.decimal is not None:
    value = int(args.decimal, 10)
else:  # args.hexadecimal is not None:
    value = int(args.hexadecimal, 16)

print("Results:\n" +
      f"\tb2={bin(value)[2:]} ; b10={value} ; b16={hex(value)[2:]}")
