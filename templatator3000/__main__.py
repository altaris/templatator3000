"""
Main module
"""

import argparse
from datetime import datetime
import logging
import os
from pathlib import Path

from jinja2 import Environment, FileSystemLoader, Template


def main():
    """Entry point"""
    logging.basicConfig(
        format="[%(levelname)s] %(message)s", level=logging.INFO
    )

    arguments = parse_command_line_arguments()
    project_type = arguments.type
    project_path = Path(arguments.path)
    project_context = arguments.__dict__
    del project_context["type"]
    del project_context["path"]

    template_path = Path(__file__).parent / "template" / project_type
    if not template_path.is_dir():
        logging.fatal(f'Invalid project type "%s"', project_type)
        exit()

    logging.info("Setting up new project at %s", project_path.absolute())
    environment = Environment(
        loader=FileSystemLoader(str(template_path)),
    )
    for from_path in template_path.glob("**/*"):
        if from_path.is_file() and from_path.name == ".DS_Store":
            continue
        from_path_relative = from_path.relative_to(template_path)
        to_path = project_path / from_path_relative
        if from_path.is_file():
            logging.info("Rendering %s", to_path)
            template = environment.get_template(str(from_path_relative))
            template.stream(project_context).dump(str(to_path))
        elif from_path.is_dir():
            logging.info("Creating %s", to_path)
            to_path.mkdir(exist_ok=True, parents=True)


def parse_command_line_arguments() -> argparse.Namespace:
    """Parses command line arguments"""
    argument_parser = argparse.ArgumentParser(description="templatator3000")
    argument_parser.add_argument(
        "path",
        metavar="PATH",
        type=str,
    )
    argument_parser.add_argument(
        "type",
        metavar="TYPE",
        type=str,
    )
    argument_parser.add_argument(
        "-a",
        "--author",
        action="store",
        default=os.environ["USER"],
        type=str,
    )
    argument_parser.add_argument(
        "-d",
        "--date",
        action="store",
        default=datetime.now().strftime("%Y-%m-%d"),
        type=str,
    )
    argument_parser.add_argument(
        "-p",
        "--project-name",
        action="store",
        required=True,
        type=str,
    )
    argument_parser.add_argument(
        "-t",
        "--title",
        action="store",
        type=str,
    )
    argument_parser.add_argument(
        "-v",
        "--version",
        action="store",
        default="0.0.0",
        type=str,
    )
    return argument_parser.parse_args()


main()
