#! /opt/homebrew/bin/python3
# author: Justin Salsbery

import sys
import argparse

# constants
VERSION = "1.0"


# simplifies the default help format
class CustomHelpFormatter(argparse.HelpFormatter):
    def add_usage(self, usage, actions, groups, prefix=None):
        pass

    def _format_action_invocation(self, action):
        if action.option_strings:
            return ', '.join(action.option_strings)
        return super()._format_action_invocation(action)


# set up argument parser
parser = argparse.ArgumentParser(
    description="binary, decimal, and hexidecimal converter", formatter_class=CustomHelpFormatter)
parser.add_argument("value", nargs="?",
                    help="value to convert")
parser.add_argument("-t", "--type", nargs="?", type=str, default="d",
                    choices=["b", "d", "h"], help="[b, d, h] value")
parser.add_argument("-v", "--version", action="version",
                    version=f'%(prog)s {VERSION}', help="show version number and exit")

# parse command line arguments
args = parser.parse_args()

# accept piped in prompts
if not sys.stdin.isatty():
    args.value = sys.stdin.read()

# print examples if not valid
if args.value is None or args.type is None:
    print("convert --help\n")
    print("examples:")
    print("  convert -t=b 010101")
    print("  convert -t=h abcd")
    sys.exit(0)

if args.type == "b":
    value = int(args.value, 2)
elif args.type == "d":
    value = int(args.value, 10)
else:  # args.type == "h"
    value = int(args.value, 16)

print("Results:\n" +
      f"\tb={bin(value)[2:]} ; d={value} ; h={hex(value)[2:]}")
