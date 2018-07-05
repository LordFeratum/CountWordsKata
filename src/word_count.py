from repository import filesystem_loader
from counter import simple_counter
from adapters import csv_adapter



if __name__ == '__main__':
    input = "romeoandjuliet.txt"
    output = "romeo_and_juliet_counter.csv"

    data = simple_counter(filesystem_loader(input))
    csv_adapter(output, data)
