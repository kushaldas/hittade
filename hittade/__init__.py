"""Command line tool to find and gather system information."""

__version__ = "0.0.1"
import argparse


def main():
    "Command line entry point."
    parser = argparse.ArgumentParser(prog="hittade", description=__doc__)
    parser.add_argument("-v", "--version", action="version", version=__version__)
    args = parser.parse_args()