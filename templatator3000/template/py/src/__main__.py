"""
Main module
"""

import argparse
import logging


def main():
    """Entry point"""
    logging.basicConfig(
        format="[%(levelname)s] %(message)s", level=logging.INFO
    )
    arguments = parse_command_line_arguments()


def parse_command_line_arguments() -> argparse.Namespace:
    """Parses command line arguments

    See also:
        https://docs.python.org/3/library/argparse.html
    """
    argument_parser = argparse.ArgumentParser(description="templatator3000")
    argument_parser.add_argument(
        "-p",
        "--project-name",
        action="store",
        required=True,
        type=str,
    )
    return argument_parser.parse_args()


main()
