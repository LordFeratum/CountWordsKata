import logger

from logging import getLogger, DEBUG

from argparse import ArgumentParser

from repository import filesystem_loader
from counter import simple_counter
from adapters import csv_adapter, yaml_adapter, json_adapter


logger = getLogger("wordcounter")


def _adapt(output, data, format):
    dispatcher = {
        'csv': csv_adapter,
        'yaml': yaml_adapter,
        'json': json_adapter,
    }
    dispatcher.get(format, csv_adapter)(output, data)


def word_count(inputs, output, format):
    data = None
    for input in inputs:
        logger.info("Procesing: %s...", input)
        data = simple_counter(filesystem_loader(input), data=data)

    _adapt(output, data, format)


if __name__ == '__main__':
    parser = ArgumentParser("A Word Counter Software")
    parser.add_argument("-f", "--file",
                        dest="input", nargs="*", default=[], required=True)
    parser.add_argument("-o", "--output", default="output.csv")
    parser.add_argument("--format", choices=["csv", "yaml", "json"],
                        default="csv")

    args = parser.parse_args()
    word_count(args.input, args.output, args.format)
