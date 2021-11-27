#! /usr/bin/env python3

import argparse
from startcp import functions, printer

VERSION = "0.0.1"


def main():

    parser = argparse.ArgumentParser(
        description="A CLI for fetching covid19 info."
    )

    args = parser.parse_args()


def __get_version():
    return VERSION


if __name__ == '__main__':
    main()
