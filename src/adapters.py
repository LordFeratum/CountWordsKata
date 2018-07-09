from json import dump as json_dump
from yaml import dump as yaml_dump


def csv_adapter(filename, data):
    with open(filename, 'w') as fp:
        fp.write("Word, Count\n")
        for word, count in data.items():
            fp.write(f"{word}, {count}\n")


def yaml_adapter(filename, data):
    _file_adapter(filename, data, yaml_dump)


def json_adapter(filename, data):
    _file_adapter(filename, data, json_dump)


def _file_adapter(filename, data, fnx):
    data_dict = {
        key: value
        for key, value in data.items()
    }
    with open(filename, 'w') as fp:
        fnx(data_dict, fp)
