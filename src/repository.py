from os.path import join as path_join


def filesystem_loader(bookname):
    path = path_join('src/texts/', bookname)
    with open(path) as fp:
        for line in fp.readlines():
            for token in line.split():
                yield token
