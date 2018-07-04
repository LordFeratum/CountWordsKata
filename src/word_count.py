from repository import filesystem_loader
from counter import Counter

from pprint import pprint



if __name__ == '__main__':
    c = Counter(filesystem_loader('romeoandjuliet.txt'))
    data = c.count()
    pprint(data)
